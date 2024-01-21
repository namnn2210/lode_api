from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken, Token
from django.contrib.auth import login as django_login
import json
import jwt
from .serializers import UserSerializer
from authentication.models import UserProfile
from gameplay.serializers import UserProfileSerializer
from server.models import APIResponse


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    body = json.loads(request.body.decode('utf-8'))
    first_name = body.get('first_name')
    last_name = body.get('last_name')
    username = body.get('username')
    password = body.get('password')
    email = body.get('email')
    phone = body.get('phone')

    print(username, password)

    if not username or not password:
        return Response(APIResponse(success=False, data={}, message="Tên đăng nhập và mật khẩu là bắt buộc").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response(APIResponse(success=False, data={}, message="Tên đăng nhập đã được sử dụng").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                    last_name=last_name)
    user_profile = UserProfile(user=user, phone=phone)
    user_profile.save()

    django_login(request, user)

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    return Response(APIResponse(success=True, data={'access_token': access_token}, message="").__dict__(),
                    status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    body = json.loads(request.body.decode('utf-8'))
    print(body)
    username = body['username']
    password = body['password']

    if not username or not password:
        return Response(APIResponse(success=False, data={}, message="Tên đăng nhập và mật khẩu là bắt buộc").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(username=username).first()

    if user is None:
        return Response(APIResponse(success=False, data={}, message="Thông tin đăng nhập không chính xác").__dict__(),
                        status=status.HTTP_401_UNAUTHORIZED)

    if not user.check_password(password):
        return Response(APIResponse(success=False, data={}, message="Thông tin đăng nhập không chính xác").__dict__(),
                        status=status.HTTP_401_UNAUTHORIZED)

    django_login(request, user)

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    # logged_account = UserSerializer(user).data
    user_profile_serializer = UserProfileSerializer(get_object_or_404(UserProfile, user=user)).data

    user_serializer = UserSerializer(user).data
    user_profile_serializer.update(user_serializer)
    del user_profile_serializer['password']
    print(user_profile_serializer)

    return Response(APIResponse(success=True, data={'access_token': access_token, 'user': user_profile_serializer},
                                message="").__dict__(), status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header.startswith('Bearer '):
        token_key = auth_header[len('Bearer '):]
        secret_key = '!@lode@@!!123'
        try:
            print('=================================')
            # Manually decode the token without checking for expiration
            decoded_token = jwt.decode(token_key, secret_key, algorithms=["HS256"])
            print('=================================')
            # 'decoded_token' is now a dictionary containing the payload data
            user_id = decoded_token['user_id']
            user = get_object_or_404(User, pk=user_id)
            user_profile_serializer = UserProfileSerializer(get_object_or_404(UserProfile, user=user)).data

            user_serializer = UserSerializer(user).data
            user_profile_serializer.update(user_serializer)

            print(user_profile_serializer)

            return Response(APIResponse(success=True, data={'user': user_profile_serializer}, message="").__dict__(), status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(APIResponse(success=False, data={}, message="Token hết hạn hoặc không hợp lệ").__dict__(), status=status.HTTP_401_UNAUTHORIZED)
    else:
        # Handle invalid or missing Authorization header
        return Response(APIResponse(success=False, data={}, message="Thiếu token").__dict__(), status=status.HTTP_401_UNAUTHORIZED)


