from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from server.models import APIResponse
from .models import SystemModel
from .serializer import SystemModelSerializer


# Create your views here.
class SystemModelListCreateView(generics.ListCreateAPIView):
    queryset = SystemModel.objects.filter(status=True)
    serializer_class = SystemModelSerializer


class SystemModelRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = SystemModel.objects.filter(status=True)
    serializer_class = SystemModelSerializer
    lookup_field = 'id'


# @permission_classes([IsAuthenticated])
class SystemAPIView(APIView):
    def get(self, request):
        try:
            system = SystemModel.objects.filter(status=True)
            serializer = SystemModelSerializer(system, many=True).data
            return Response(APIResponse(success=True, data=serializer, message="").__dict__())
        except Exception as ex:
            return Response(
                APIResponse(success=False, data={}, message="Thiếu token").__dict__(),
                status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            system = SystemModel.objects.get(pk=id, status=True)
        except SystemModel.DoesNotExist:
            return Response(
                APIResponse(success=False, data={}, message="Không tìm thấy dữ liệu").__dict__(),
                status=status.HTTP_404_NOT_FOUND)
        try:
            hotline = request.data.get('hotline', '')
            zalo = request.data.get('zalo', '')
            viber = request.data.get('viber', '')
            telegram = request.data.get('telegram', '')
            google_code = request.data.get('google_code', '')
            web_title = request.data.get('web_title', '')

            system.hotline = hotline
            system.zalo = zalo
            system.viber = viber
            system.telegram = telegram
            system.google_code = google_code
            system.web_title = web_title
            system.save()
            serializer = SystemModelSerializer(system).data

            return Response(APIResponse(success=True, data=serializer, message="").__dict__())
        except Exception as ex:
            return Response(
                APIResponse(success=False, data=str(ex), message="Lưu thông tin thất bại").__dict__(),
                status=status.HTTP_400_BAD_REQUEST)
