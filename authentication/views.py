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
    first_name = body.get('first_name', '')
    password = body.get('password')
    password2 = body.get('password2')
    email = body.get('email')
    phone = body.get('phone')

    print(phone, password)

    if password != password2:
        return Response(APIResponse(success=False, data={}, message="Mật khẩu không trùng khớp").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    print('step1')

    if not phone or not password:
        return Response(APIResponse(success=False, data={}, message="Tên đăng nhập và mật khẩu là bắt buộc").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)
    print('step2')
    try:
        User.objects.get(email=email)
        return Response(APIResponse(success=False, data={}, message="Email đã được sử dụng").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        pass
    print('step3')
    print(UserProfile.objects.filter(phone=phone).exists())
    if UserProfile.objects.filter(phone=phone).exists():
        return Response(APIResponse(success=False, data={}, message="Số điện thoại đã được sử dụng").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    print('step4')
    user = User.objects.create_user(username=phone, password=password, email=email.lower(), first_name=first_name)
    user_profile = UserProfile(user=user, phone=phone)
    user_profile.save()

    django_login(request, user)

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    user_profile_serializer = UserProfileSerializer(get_object_or_404(UserProfile, user=user)).data
    user_serializer = UserSerializer(user).data
    user_profile_serializer.update(user_serializer)

    return Response(APIResponse(success=True, data={'access_token': access_token, 'user': user_profile_serializer},
                                message="").__dict__(),
                    status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    body = json.loads(request.body.decode('utf-8'))
    print(body)
    phone = body['phone']
    password = body['password']

    if not phone or not password:
        return Response(APIResponse(success=False, data={}, message="Tên đăng nhập và mật khẩu là bắt buộc").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    try:
        user_profile = UserProfile.objects.get(phone=phone)
    except UserProfile.DoesNotExist:
        return Response(APIResponse(success=False, data={}, message="Thông tin đăng nhập không chính xác").__dict__(),
                        status=status.HTTP_404_NOT_FOUND)

    user = user_profile.user

    if not user.check_password(password):
        return Response(APIResponse(success=False, data={}, message="Thông tin đăng nhập không chính xác").__dict__(),
                        status=status.HTTP_401_UNAUTHORIZED)
    if not user.is_active:
        return Response(APIResponse(success=False, data={},
                                    message="Tài khoản bị khóa. Vui lòng liên hệ để biết thêm chi tiết").__dict__(),
                        status=status.HTTP_401_UNAUTHORIZED)

    django_login(request, user)

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    # logged_account = UserSerializer(user).data
    user_profile_serializer = UserProfileSerializer(user_profile).data

    user_serializer = UserSerializer(user).data
    user_profile_serializer.update(user_serializer)
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

            return Response(APIResponse(success=True, data={'user': user_profile_serializer}, message="").__dict__(),
                            status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(APIResponse(success=False, data={}, message="Token hết hạn hoặc không hợp lệ").__dict__(),
                            status=status.HTTP_401_UNAUTHORIZED)
    else:
        # Handle invalid or missing Authorization header
        return Response(APIResponse(success=False, data={}, message="Thiếu token").__dict__(),
                        status=status.HTTP_401_UNAUTHORIZED)
