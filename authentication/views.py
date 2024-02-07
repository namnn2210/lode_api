from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken, Token
from django.contrib.auth import login as django_login
from .serializers import UserSerializer
from authentication.models import UserProfile
from gameplay.serializers import UserProfileSerializer
from server.models import APIResponse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.http import Http404
from rest_framework.views import APIView
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from .serializers import PasswordResetSerializer
from django.core.mail import send_mail

import json
import jwt


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    body = json.loads(request.body.decode('utf-8'))
    first_name = body.get('first_name', '')
    password = body.get('password')
    password2 = body.get('password2')
    email = body.get('email')
    phone = body.get('phone')

    print('Checking match password')
    if password != password2:
        return Response(APIResponse(success=False, data={}, message="Mật khẩu không trùng khớp").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    print('Checking enough info')

    if not phone or not password:
        return Response(APIResponse(success=False, data={}, message="Tên đăng nhập và mật khẩu là bắt buộc").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    print('Checking duplicate email')

    try:
        User.objects.get(email=email)
        return Response(APIResponse(success=False, data={}, message="Email đã được sử dụng").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        pass

    print('Checking duplicate phone')
    if UserProfile.objects.filter(phone=phone).exists():
        return Response(APIResponse(success=False, data={}, message="Số điện thoại đã được sử dụng").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=phone, password=password, email=email.lower(), first_name=first_name)
    user_profile = UserProfile(user=user, phone=phone, ip_address=get_client_ip(request))
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def password_change(request):
    user_id = request.data.get('user_id')
    current_password = request.data.get('current_password')
    new_password = request.data.get('new_password')
    new_password2 = request.data.get('new_password2')
    if not user_id or not current_password or not new_password or not new_password2:
        return Response(APIResponse(success=False, data={}, message="Hãy nhập đầy đủ thông tin").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    if new_password != new_password2:
        return Response(APIResponse(success=False, data={}, message="Mật khẩu mới không trùng khớp").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(pk=user_id)
        # user_profile = UserProfile.objects.get(user=user)
    except User.DoesNotExist:
        return Response(APIResponse(success=False, data={}, message="Thông tin người dùng không chính xác").__dict__(),
                        status=status.HTTP_404_NOT_FOUND)

    # user = user_profile.user

    if not user.check_password(current_password):
        return Response(APIResponse(success=False, data={}, message="Thông tin đăng nhập không chính xác").__dict__(),
                        status=status.HTTP_401_UNAUTHORIZED)

    user.set_password(new_password)
    user.save()

    return Response(APIResponse(success=True, data={}, message="Mật khẩu thay đổi thành công").__dict__(),
                    status=status.HTTP_200_OK)


def send_reset_email(email, reset_url):
    subject = 'Lode 100 - Đặt lại mật khẩu'
    message = f'Bạn vui lòng truy cập đường dẫn dưới đây và thao tác để cấp lại mật khẩu:\n\n{reset_url}'
    from_email = 'your@email.com'  # Replace with your email address
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)


class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = get_user_model().objects.filter(email=email).first()

            if user:
                # Generate and send the password reset token via email
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_url = f"https://110lode.com/reset-password/{uid}/{token}/"

                # Send reset URL to the user via email (implement this)
                send_reset_email(email, reset_url)

                # For demonstration purposes, we'll return the reset URL in the response
                return Response(APIResponse(success=True, data={'reset_url': reset_url},
                                            message="Email đặt lại mật khẩu đã gửi thành công").__dict__(),
                                status=status.HTTP_200_OK)

            else:
                return Response(
                    APIResponse(success=False, data={}, message="Thông tin email không chính xác").__dict__(),
                    status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    def post(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            raise Http404

        if default_token_generator.check_token(user, token):
            # Token is valid, allow the user to reset the password
            # You can implement password reset logic here
            # For simplicity, we'll return a success message in this example
            new_password = request.POST.get('new_password')
            user.set_password(new_password)
            user.save()

            return Response(APIResponse(success=True, data={}, message="Mật khẩu đặt lại thành công").__dict__(),
                            status=status.HTTP_200_OK)
        else:
            return Response(APIResponse(success=False, data={}, message="Token không hợp lệ").__dict__(),
                            status=status.HTTP_400_BAD_REQUEST)
