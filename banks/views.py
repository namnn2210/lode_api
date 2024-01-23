from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Bank
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from server.models import APIResponse
from rest_framework import status
from .serializer import BankSerializer
import requests


@api_view(['GET'])
@permission_classes([AllowAny])
def fetch_banks(request):
    response = requests.get('https://qr.sepay.vn/banks.json').json()['data']
    for data in response:
        print(data)
        bank = Bank(name=data['name'], code=data['code'], bin=data['bin'], short_name=data['short_name'])
        bank.save()
    return response


@permission_classes([IsAuthenticated])
class BankView(APIView):
    def get(self, request):
        all_banks = Bank.objects.all()
        bank_serializers = BankSerializer(all_banks, many=True).data
        return Response(APIResponse(success=True, data=bank_serializers, message="").__dict__())

    def post(self, request):
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(APIResponse(success=True, data=serializer.data, message="").__dict__(),
                            status=status.HTTP_201_CREATED)
        return Response(APIResponse(success=False, data={}, message="Lưu thông tin thất bại").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, bank_id):
        try:
            bank = Bank.objects.get(pk=bank_id, status=True)
        except Bank.DoesNotExist:
            return Response(APIResponse(success=False, data={}, message="Dữ liệu không tồn tại").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)

        serializer = BankSerializer(bank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())
        return Response(APIResponse(success=False, data={}, message="Lưu thông tin thất bại").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, bank_id):
        try:
            bank = Bank.objects.get(pk=bank_id, status=True)
        except Bank.DoesNotExist:
            return Response(APIResponse(success=False, data={}, message="Dữ liệu không tồn tại").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)

        bank.status = False
        bank.save()
        return Response(APIResponse(success=True, data={}, message="Xóa thành công").__dict__())
