import jwt

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from authentication.models import UserProfile
from .serializer import NotificationSerializer, NotificationCategorySerializer
from .models import NotificationModel, NotificationCategoryModel
from server.models import APIResponse
from gameplay.serializers import UserProfileSerializer


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
                    notifications = NotificationModel.objects.filter(
                        Q(user=user) | Q(user=None) & Q(status=True) & Q(read=False))

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
                    try:
                        category_id = request.data.get('category_id', None)
                        user_ids = request.data.get('user_id', [])
                        title = request.data.get('title', '')
                        content = request.data.get('content', '')
                        list_noti_saved = []
                        if category_id:
                            category = NotificationCategoryModel.objects.get(pk=category_id)
                            if user_ids and len(user_ids) > 0:
                                for user_id in user_ids:
                                    if user_id:
                                        to_user = User.objects.get(pk=user_id)
                                    else:
                                        to_user = None
                                    noti = NotificationModel(category=category, user=to_user, title=title,
                                                             content=content)
                                    noti.save()
                                    serializer = NotificationSerializer(noti).data
                                    if user_id:
                                        user_profile = UserProfileSerializer(
                                            UserProfile.objects.get(user_id=user_id)).data
                                        del user_profile['user']
                                        serializer['user'] = user_profile
                                    list_noti_saved.append(serializer)
                            else:
                                noti = NotificationModel(category=category, user=None, title=title, content=content)
                                noti.save()
                                serializer = NotificationSerializer(noti).data
                                if user_id:
                                    user_profile = UserProfileSerializer(UserProfile.objects.get(user_id=user_id)).data
                                    del user_profile['user']
                                    serializer['user'] = user_profile
                                list_noti_saved.append(serializer)

                            return Response(APIResponse(success=True, data=list_noti_saved, message="").__dict__())
                        else:
                            Response(
                                APIResponse(success=False, data={},
                                            message="Danh mục thông báo không hợp lệ").__dict__(),
                                status=status.HTTP_400_BAD_REQUEST)
                    except Exception as ex:
                        return Response(
                            APIResponse(success=False, data=str(ex), message="Lưu thông tin thất bại").__dict__(),
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
                    try:
                        category_id = request.data.get('category_id', 1)
                        user_id = request.data.get('user_id', None)
                        # to_user = User.objects.get(pk=user_id)
                        title = request.data.get('title', '')
                        content = request.data.get('content', '')
                        category = NotificationCategoryModel.objects.get(pk=category_id)
                        if category:
                            if user_id:
                                to_user = User.objects.get(pk=user_id)
                            else:
                                to_user = None
                            notification.category = category
                            notification.user = to_user
                            notification.title = title
                            notification.content = content
                            notification.save()
                            serializer = NotificationSerializer(notification).data
                            user_profile = UserProfileSerializer(UserProfile.objects.get(user_id=user_id)).data
                            del user_profile['user']
                            serializer['user'] = user_profile
                            return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())
                        else:
                            Response(
                                APIResponse(success=False, data={},
                                            message="Danh mục thông báo không hợp lệ").__dict__(),
                                status=status.HTTP_400_BAD_REQUEST)
                    except Exception as ex:
                        return Response(
                            APIResponse(success=False, data=str(ex), message="Lưu thông tin thất bại").__dict__(),
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
        return Response(APIResponse(success=True, data={}, message="").__dict__())


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def read_notifications(request):
    print('===========================')
    user_id = request.data.get('user_id', None)
    print(user_id)
    if user_id is not None:
        print('==========================')
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(
                APIResponse(success=False, data={}, message="Không tìm thấy dữ liệu").__dict__(),
                status=status.HTTP_404_NOT_FOUND)
        user_profile = UserProfile.objects.get(user=user)
        user_profile.read_noti = True
        user_profile.save()
        Response(APIResponse(success=True, data={}, message="").__dict__())
    else:
        Response(APIResponse(success=False, data={}, message="Dữ liệu không hợp lệ").__dict__())


@permission_classes([IsAuthenticated])
# Create your views here.
class NotificationCategoryAPIView(APIView):
    def get(self, request):
        categories = NotificationCategoryModel.objects.all()
        serializer = NotificationCategorySerializer(categories, many=True).data
        return Response(APIResponse(success=True, data=serializer, message="").__dict__())

    def post(self, request):
        serializer = NotificationCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(APIResponse(success=True, data=serializer.data, message="").__dict__(),
                            status=status.HTTP_201_CREATED)
        else:
            return Response(APIResponse(success=False, data={}, message="Lưu thông tin thất bại").__dict__(),
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, cat_id):
        try:
            game = NotificationCategoryModel.objects.get(pk=cat_id, status=True)
        except NotificationCategoryModel.DoesNotExist:
            return Response(APIResponse(success=False, data={}, message="Dữ liệu không tồn tại").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)
        serializer = NotificationCategorySerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())
        else:
            return Response(APIResponse(success=False, data={}, message="Lưu thông tin thất bại").__dict__(),
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cat_id):
        try:
            game = NotificationCategoryModel.objects.get(pk=cat_id, status=True)
        except NotificationCategoryModel.DoesNotExist:
            return Response(APIResponse(success=False, data={}, message="Dữ liệu không tồn tại").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)

        game.status = False
        game.save()
        return Response(APIResponse(success=True, data={}, message="Xóa thành công").__dict__())
