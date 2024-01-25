import jwt

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import NotificationSerializer, NotificationCategorySerializer
from .models import NotificationModel, NotificationCategoryModel
from server.models import APIResponse


@permission_classes([IsAuthenticated])
# Create your views here.
class NotificationAPIView(APIView):
    def get(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header.startswith('Bearer '):
            token_key = auth_header[len('Bearer '):]
            print(token_key)
            secret_key = '!@lode@@!!123'
            try:
                # Decode the JWT
                decoded_token = jwt.decode(token_key, secret_key, algorithms=["HS256"])
                user_id = decoded_token['user_id']
                user = get_object_or_404(User, pk=user_id)
                if user.is_staff or user.is_superuser:
                    notifications = NotificationModel.objects.filter(status=True)
                else:
                    notifications = NotificationModel.objects.filter(Q(user=user) | Q(user=None) & Q(status=True))

                serializer = NotificationSerializer(notifications, many=True).data
                return Response(APIResponse(success=True, data=serializer, message="").__dict__())
            except Exception as ex:
                print(str(ex))
                return Response(
                    APIResponse(success=False, data={}, message="Lấy dữ liệu thất bại").__dict__())
        else:
            return Response(
                APIResponse(success=False, data={}, message="Thiếu token").__dict__(),
                status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header.startswith('Bearer '):
            token_key = auth_header[len('Bearer '):]
            print(token_key)
            secret_key = '!@lode@@!!123'
            try:
                # Decode the JWT
                decoded_token = jwt.decode(token_key, secret_key, algorithms=["HS256"])
                user_id = decoded_token['user_id']
                user = get_object_or_404(User, pk=user_id)
                if user.is_superuser or user.is_staff:
                    serializer = NotificationSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())
                    return Response(
                        APIResponse(success=False, data=serializer.errors, message="Lưu thông tin thất bại").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)
                else:
                    Response(
                        APIResponse(success=False, data={}, message="Không có quyền").__dict__(),
                        status=status.HTTP_403_FORBIDDEN)
            except jwt.ExpiredSignatureError as ex:
                print(str(ex))
                return Response(
                    APIResponse(success=False, data={}, message="Không xác thực được người dùng").__dict__())
        else:
            return Response(
                APIResponse(success=False, data={}, message="Thiếu token").__dict__(),
                status=status.HTTP_404_NOT_FOUND)

    def put(self, request, notification_id):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header.startswith('Bearer '):
            token_key = auth_header[len('Bearer '):]
            print(token_key)
            secret_key = '!@lode@@!!123'
            try:
                # Decode the JWT
                decoded_token = jwt.decode(token_key, secret_key, algorithms=["HS256"])
                user_id = decoded_token['user_id']
                user = get_object_or_404(User, pk=user_id)
                if user.is_superuser or user.is_staff:
                    try:
                        notification = NotificationModel.objects.get(pk=notification_id, status=True)
                    except NotificationModel.DoesNotExist:
                        return Response(
                            APIResponse(success=False, data={}, message="Không tìm thấy dữ liệu").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)

                    serializer = NotificationSerializer(notification, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())
                    return Response(
                        APIResponse(success=False, data=serializer.errors, message="Lưu thông tin thất bại").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)
                else:
                    Response(
                        APIResponse(success=False, data={}, message="Không có quyền").__dict__(),
                        status=status.HTTP_403_FORBIDDEN)
            except jwt.ExpiredSignatureError as ex:
                print(str(ex))
                return Response(
                    APIResponse(success=False, data={}, message="Không xác thực được người dùng").__dict__())
        else:
            return Response(
                APIResponse(success=False, data={}, message="Thiếu token").__dict__(),
                status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, notification_id):
        try:
            notification = NotificationModel.objects.get(pk=notification_id, status=True)
        except NotificationModel.DoesNotExist:
            return Response(APIResponse(success=False, data={}, message="Dữ liệu không tồn tại").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)

        notification.status = False
        notification.save()
        return Response(APIResponse(success=True, data={}, message="").__dict__(),
                        status=status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
# Create your views here.
class NotificationCategoryAPIView(APIView):
    def get(self, request):
        pass
