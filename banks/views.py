from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Bank
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from server.models import APIResponse

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
