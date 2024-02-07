from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from authentication.models import UserProfile
from authentication.serializers import UserSerializer, UserProfileSerializer
from .models import City, Game, Subgame, Rate, Banking
from server.models import APIResponse
from gameplay.models import Order, BalanceTransaction
from notification.models import NotificationModel
from banks.models import Bank
from datetime import datetime
from .serializer import GameSerializer, SubGameSerializer, CitySerializer, RateSerializer, BankingSerializer, \
    BalanceTransactionSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import status
from django.utils.timezone import now
import random
import pytz
import requests
import json
import jwt
import time
import re

desired_timezone = pytz.timezone('Asia/Bangkok')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_games(request):
    regions = ['bac', 'trung', 'nam']
    data = []
    for region in regions:
        url = f'https://api-sg.quayso1.com/lotte/categories/{region}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()['rows']
            for item in data:
                game = Game(type=item['type'], name=item['name'], region=region)
                game.save()
                sub_games = item['children']
                for sub_game in sub_games:
                    sub_game = Subgame(id=sub_game['id'], name=sub_game['name'], region=sub_game['region'],
                                       type=sub_game['type'], guide=sub_game['guide'], rate=sub_game['rate'],
                                       pay_number=sub_game['pay_number'], min_amount=sub_game['min_amount'],
                                       max_amount=sub_game['max_amount'], multi=sub_game['multi'],
                                       code=sub_game['code'],
                                       max=sub_game['max'], active=sub_game['active'],
                                       created_at=sub_game['created_at'],
                                       updated_at=sub_game['updated_at'], max_number=sub_game['max_number'])
                    sub_game.save()

    return Response({'games': data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_rates(request):
    data = []
    url = f'https://api-sg.quayso1.com/rates'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['rows']
        for item in data:
            rate = Rate(id=item['id'], rate=item['rate'], group_id=item['group_id'], category_id=item['category_id'],
                        created_at=item['created_at'], updated_at=item['updated_at'])
            rate.save()

    return Response({'rates': data})


@api_view(['GET'])
@permission_classes([AllowAny])
def get_games(request, region):
    games = GameSerializer(Game.objects.filter(region=region), many=True).data
    list_games = []
    for game in games:
        game_obj = {
            'type': game['type'],
            'name': game['name']
        }
        sub_games = SubGameSerializer(Subgame.objects.filter(type=game['type'], region=game['region']), many=True).data
        game_obj['children'] = sub_games
        list_games.append(game_obj)

    return Response(APIResponse(success=True, data=list_games, message="").__dict__())


@api_view(['GET'])
@permission_classes([AllowAny])
def get_cities(request):
    query_date = request.query_params.get('date', None)
    region = request.query_params.get('region', None)
    weekday = None
    if not query_date:
        print('no params -> get today cities')
        today = datetime.now(desired_timezone).date()
        print('today', today)
        weekday = today.isoweekday()
        print('day of week', weekday)
    else:
        date_object = datetime.fromisoformat(query_date)
        weekday = date_object.isoweekday()
    if region:
        print('region', region)
        cities = CitySerializer(City.objects.filter((Q(date__contains=str(weekday)) | Q(date='')) & Q(region=region)),
                                many=True).data
    else:
        cities = CitySerializer(City.objects.filter(Q(date__contains=str(weekday)) | Q(date='')), many=True).data
    return Response(APIResponse(success=True, data=cities, message="").__dict__())


def extract_data(regex, response):
    results = re.findall(regex, response, re.DOTALL)
    if len(results) > 0:
        return results[0]
    return ''


@api_view(['GET'])
@permission_classes([AllowAny])
def get_result(request):
    query_date = request.query_params.get('date', None)
    city = request.query_params.get('city', None)
    if city:
        if query_date:
            str_date = f'/{query_date}'
        else:
            str_date = ''
        current_timestamp = int(time.time())
        url = f'https://www.xoso.net/getkqxs/{city}{str_date}.js_={current_timestamp}'
        html_response = requests.get(url).text.replace('\t', '').replace('nowrap', '')
        title_regex = r'<div class="title">(.*?)</div>'
        weekday_regex = r'<td\s{0,}class="thu"\s{0,}>\s{0,}(.*?)<\/td>'
        if city == 'mien-bac':
            date_regex = r'<td\s{0,}class="ngay">\s{0,}Ng&agrave;y:\s(.*?)\s<\/td>'
        else:
            date_regex = r'<td class="ngay">Ngày:\s(.*?)<\/td>'
        db_regex = r'<td class="giaidb">\s{0,}(.*?)<\/td>'
        giai1_regex = r'<td class="giai1">\s{0,}(.*?)<\/td>'
        giai2_regex = r'<td class="giai2">\s{0,}(.*?)<\/td>'
        giai3_regex = r'<td class="giai3">\s{0,}(.*?)<\/td>'
        giai4_regex = r'<td class="giai4">\s{0,}(.*?)<\/td>'
        giai5_regex = r'<td class="giai5">\s{0,}(.*?)<\/td>'
        giai6_regex = r'<td class="giai6">\s{0,}(.*?)<\/td>'
        giai7_regex = r'<td class="giai7">\s{0,}(.*?)<\/td>'
        giai8_regex = r'<td class="giai8">\s{0,}(.*?)<\/td>'

        title_data = extract_data(title_regex, html_response)
        weekday_data = extract_data(weekday_regex, html_response)
        date_data = extract_data(date_regex, html_response)
        db_data = extract_data(db_regex, html_response)
        giai1_data = extract_data(giai1_regex, html_response)
        giai2_data = extract_data(giai2_regex, html_response)
        giai3_data = extract_data(giai3_regex, html_response)
        giai4_data = extract_data(giai4_regex, html_response)
        giai5_data = extract_data(giai5_regex, html_response)
        giai6_data = extract_data(giai6_regex, html_response)
        giai7_data = extract_data(giai7_regex, html_response)
        giai8_data = extract_data(giai8_regex, html_response)

        if city == 'mien-bac' or city == 'dak-lak' or city == 'quang-nam' or city == 'khanh-hoa' or city == 'da-nang' or city == 'binh-dinh' or city == 'quang-binh' or city == 'quang-tri' or city == 'ninh-thuan' or city == 'gia-lai':
            # formatted_date_data = date_data.replace('/', '-')
            title = f'{title_data} {date_data}'
        else:
            title = title_data
        data = {
            'title': title,
            'result': {
                "special": db_data,
                "prize1": giai1_data,
                "prize2": giai2_data,
                "prize3": giai3_data,
                "prize4": giai4_data,
                "prize5": giai5_data,
                "prize6": giai6_data,
                "prize7": giai7_data,
                "prize8": giai8_data,
            }
        }

        return Response(APIResponse(success=True, data=data, message="").__dict__())
    else:
        return Response(APIResponse(success=False, data={}, message="Thông tin đài không hợp lệ").__dict__())


# @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# def get_all_cities(request, region=None):
#     if region:
#         cities = CitySerializer(City.objects.filter(region=region), many=True).data
#     else:
#         cities = CitySerializer(City.objects.all(), many=True).data
#     return Response(APIResponse(success=True, data=cities, message="").__dict__())


@api_view(['GET'])
@permission_classes([AllowAny])
def get_rates(request):
    rates = RateSerializer(Rate.objects.all(), many=True).data
    return Response(APIResponse(success=True, data=rates, message="").__dict__())


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_banking(request):
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
            user_profile = get_object_or_404(UserProfile, user=user)
            content = {'content': user_profile.code}

            banking = BankingSerializer(Banking.objects.get(status=True)).data
            banking.update(content)
            return Response(APIResponse(success=True, data=banking, message="").__dict__())
        except jwt.ExpiredSignatureError as ex:
            print(str(ex))
            return Response(APIResponse(success=False, data={}, message="Không xác thực được người dùng").__dict__())
    else:
        return Response(APIResponse(success=False, data={}, message="Thiếu token").__dict__())


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def deposit(request):
    body = json.loads(request.body.decode('utf-8'))
    banking = Banking.objects.get(status=True)
    if body['transferType'] == 'in':
        user_profile = UserProfile.objects.get(code=body['content'])
        if user_profile:
            # Tao giao dich trong DB
            deposit_transaction = BalanceTransaction(user=user_profile.user, transaction_type=1, status=1,
                                                     bank=banking.bank, user_name=banking.user_name,
                                                     bank_number=banking.bank_number,
                                                     amount=body['transferAmount'], description=body['content'])
            deposit_transaction.save()

            # Add notification
            notification = NotificationModel(category_id=1, title='Nạp tiền thành công',
                                             content='Quý khách đã nạp thành công {} VNĐ với mã giao dịch {}'.format(
                                                 body['transferAmount'], body['content']), user=user_profile.user)
            notification.save()

            deposit_transaction_serializer = BalanceTransactionSerializer(deposit_transaction).data
            return Response(APIResponse(success=True, data=deposit_transaction_serializer, message="").__dict__())
        else:
            return Response(APIResponse(success=False, data={}, message="Người dùng không hợp lệ").__dict__())
    else:
        return Response(APIResponse(success=False, data={}, message="Giao dịch không hợp lệ").__dict__())


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def withdraw(request):
    """
    :body request:
    {
        "user_id":1
        "amount":27000
        "bank_id":23,
        "user_name":"do van ninh",
        "bank_number":"39389383"
    }
    :return:
    """
    body = json.loads(request.body.decode('utf-8'))
    user = get_object_or_404(User, pk=body['user_id'])
    user_profile = get_object_or_404(UserProfile, user=user)
    amount = body['amount'] * 1000
    bank_id = body['bank_id']
    user_name = body['user_name']
    bank_number = body['bank_number']
    bank = get_object_or_404(Bank, pk=bank_id)

    if amount < 200000:
        return Response(
            APIResponse(success=False, data={}, message="Số tiền rút tối thiểu là 200.000 VNĐ").__dict__())
    if int(amount) > user_profile.balance:
        return Response(
            APIResponse(success=False, data={}, message="Số dư không đủ").__dict__())
    print('amount withdraw', amount)

    # Get all orders
    orders = Order.objects.filter(user=user)
    total_amount_order = 0
    for order in orders:
        total_amount_order += order.pay_number
    print('total_amount_order', total_amount_order)
    # Get all deposit
    deposits = BalanceTransaction.objects.filter(user=user, transaction_type=1, status=1)
    total_amount_deposit = 0
    for deposit in deposits:
        total_amount_deposit += deposit.amount
    print('total_amount_deposit', total_amount_deposit)
    if (total_amount_order < total_amount_deposit) or total_amount_order == 0:
        return Response(
            APIResponse(success=False, data={},
                        message="Tổng số tiền đặt cược ít hơn tổng số tiền đã nạp vào").__dict__())

    withdraw = BalanceTransaction(user=user, transaction_type=2, status=0, amount=amount, bank=bank,
                                  user_name=user_name, bank_number=bank_number)
    withdraw.save()

    withdraw_serializer = BalanceTransactionSerializer(withdraw).data

    return Response(APIResponse(success=True, data=withdraw_serializer, message="").__dict__())


####################################### ADMIN RESTAPI ##############################################################

####################################### GAME RESTAPI ##############################################################
@permission_classes([IsAuthenticated])
class GameAPIView(APIView):
    def get(self, request):
        games = Game.objects.filter(status=True)
        serializer = GameSerializer(games, many=True)

        return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())

    def post(self, request):
        """
        :param request: {
            'type':'a',
            'name':'b',
            'region':'bac/trung/nam'
        }
        :return:
        """
        body = json.loads(request.body.decode('utf-8'))
        region = ['bac', 'trung', 'nam']
        serializer = GameSerializer(data=body)
        if body['region'] in region:
            if serializer.is_valid():
                serializer.save()
                return Response(APIResponse(success=True, data=serializer.data, message="").__dict__(),
                                status=status.HTTP_201_CREATED)
        else:
            return Response(APIResponse(success=False, data={}, message="Khu vực không hợp lệ").__dict__(),
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(APIResponse(success=False, data={}, message="Lưu thông tin thất bại").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, game_id):
        body = json.loads(request.body.decode('utf-8'))
        region = ['bac', 'trung', 'nam']
        if body['region'] in region:
            try:
                game = Game.objects.get(pk=game_id, status=True)
            except Subgame.DoesNotExist:
                return Response(APIResponse(success=False, data={}, message="Dữ liệu không tồn tại").__dict__(),
                                status=status.HTTP_404_NOT_FOUND)
            serializer = GameSerializer(game, data=body)
            if serializer.is_valid():
                serializer.save()
                return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())
        else:
            return Response(APIResponse(success=False, data={}, message="Khu vực không hợp lệ").__dict__(),
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(APIResponse(success=False, data={}, message="Lưu thông tin thất bại").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, game_id):
        try:
            game = Game.objects.get(pk=game_id, status=True)
        except Game.DoesNotExist:
            return Response(APIResponse(success=False, data={}, message="Dữ liệu không tồn tại").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)

        game.status = False
        game.save()
        return Response(APIResponse(success=True, data={}, message="Xóa thành công").__dict__())


####################################### SUBGAME RESTAPI ##############################################################
@permission_classes([IsAuthenticated])
class SubgameAPIView(APIView):
    def get(self, request, subgame_id=None):
        if subgame_id is None:
            # Get all Subgames
            subgames = Subgame.objects.filter(active=True)
            serializer = SubGameSerializer(subgames, many=True)
        else:
            # Get a specific Subgame by ID
            try:
                subgame = Subgame.objects.get(pk=subgame_id)
                serializer = SubGameSerializer(subgame)
            except Subgame.DoesNotExist:
                return Response(APIResponse(success=False, data={}, message="Dữ liệu không tồn tại").__dict__(),
                                status=status.HTTP_404_NOT_FOUND)

        return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())

    def post(self, request):
        serializer = SubGameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(APIResponse(success=True, data=serializer.data, message="").__dict__(),
                            status=status.HTTP_201_CREATED)
        return Response(APIResponse(success=False, data=serializer.errors, message="Lưu thông tin thất bại").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, subgame_id):
        try:
            subgame = Subgame.objects.get(pk=subgame_id, active=True)
        except Subgame.DoesNotExist:
            return Response(APIResponse(success=False, data={}, message="Dữ liệu không tồn tại").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)

        serializer = SubGameSerializer(subgame, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())
        return Response(APIResponse(success=False, data=serializer.errors, message="Lưu thông tin thất bại").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, subgame_id):
        try:
            subgame = Subgame.objects.get(pk=subgame_id, active=True)
        except Subgame.DoesNotExist:
            return Response(APIResponse(success=False, data={}, message="Dữ liệu không tồn tại").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)

        subgame.active = 0
        subgame.save()
        return Response(APIResponse(success=True, data={}, message="Xóa thành công").__dict__())


####################################### USER RESTAPI ##############################################################
@permission_classes([IsAuthenticated])
class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        list_users = []
        for user in users:
            user_profile = UserProfile.objects.get(user=user)
            serializer = UserProfileSerializer(user_profile).data
            list_users.append(serializer)
            # serializer = UserSerializer(users, many=True)
        return Response(APIResponse(success=True, data=list_users, message="").__dict__())

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(APIResponse(success=True, data=serializer.data, message="").__dict__(),
                            status=status.HTTP_201_CREATED)
        return Response(APIResponse(success=False, data=serializer.errors, message="Lưu thông tin thất bại").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(APIResponse(success=False, data={}, message="Dữ liệu không tồn tại").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)

        try:

            request_data_first_name = request.data.get("first_name")
            request_data_is_active = request.data.get("is_active")
            if request_data_first_name is not None:
                user.first_name = request_data_first_name
                user.save()
                serializer = UserSerializer(user)
                # if serializer.is_valid():
                #     serializer.save()
                return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())
            if request_data_is_active is not None:
                user.is_active = request_data_is_active
                user.save()
                serializer = UserSerializer(user)
                # if serializer.is_valid():
                #     serializer.save()
                return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())
        except Exception:
            return Response(APIResponse(success=False, data={}, message="Lưu thông tin thất bại").__dict__(),
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(APIResponse(success=False, data={}, message="Dữ liệu không tồn tại").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)

        user.is_active = 0
        user.save()
        return Response(APIResponse(success=True, data={}, message="").__dict__(),
                        status=status.HTTP_204_NO_CONTENT)


####################################### USER PROFILE RESTAPI ##############################################################

@permission_classes([IsAuthenticated])
class UserProfileAPIView(APIView):
    def get(self, request):
        user_profiles = UserProfile.objects.filter(status=True).select_related('user')
        serializer = UserProfileSerializer(user_profiles, many=True)
        return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(APIResponse(success=True, data=serializer.data, message="").__dict__(),
                            status=status.HTTP_201_CREATED)
        return Response(APIResponse(success=False, data=serializer.errors, message="Lưu thông tin thất bại").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_profile_id):
        try:
            user_profile = UserProfile.objects.get(pk=user_profile_id, status=True)
        except UserProfile.DoesNotExist:
            return Response(APIResponse(success=False, data={}, message="Dữ liệu không tồn tại").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)

        try:

            request_data_balance = request.data.get("balance")
            if int(request_data_balance) > 0:

                # Tao giao dich ao trong db de tracking thong ke
                if request_data_balance > user_profile.balance:
                    remaining_amount = request_data_balance - user_profile.balance
                    deposit_transaction = BalanceTransaction(user=user_profile.user, amount=remaining_amount,
                                                             transaction_type=1, status=1)
                    deposit_transaction.save()
                if request_data_balance < user_profile.balance:
                    remaining_amount = user_profile.balance - request_data_balance
                    withdraw_transaction = BalanceTransaction(user=user_profile.user, amount=remaining_amount,
                                                              transaction_type=2, status=1)
                    withdraw_transaction.save()

                user_profile.balance = request_data_balance
                user_profile.save()
                serializer = UserProfileSerializer(user_profile)
                # if serializer.is_valid():
                #     serializer.save()
                return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())
            else:
                return Response(APIResponse(success=False, data={}, message="Số dư phải lớn hơn 0").__dict__(),
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(APIResponse(success=False, data=str(ex), message="Lưu thông tin thất bại").__dict__(),
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_profile_id):
        try:
            user_profile = UserProfile.objects.get(pk=user_profile_id, status=True)
        except UserProfile.DoesNotExist:
            return Response(APIResponse(success=False, data={}, message="Dữ liệu không tồn tại").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)

        user_profile.status = False
        user_profile.save()
        return Response(APIResponse(success=True, data={}, message="").__dict__(),
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile_by_phone(request):
    phone = request.GET.get('phone', None)
    if phone:
        user_profile = UserProfile.objects.filter(Q(phone__contains=phone) & Q(status=True))
        serializer = UserProfileSerializer(user_profile, many=True).data
        return Response(APIResponse(success=True, data=serializer, message="").__dict__())
    else:
        return Response(APIResponse(success=True, data=[], message="").__dict__())


####################################### BALANCE TRANSACTIONS RESTAPI ##############################################################
# @permission_classes([IsAuthenticated])
class BalanceTransactionsAPIView(APIView):

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

                if user.is_superuser or user.is_staff:
                    balance_transactions = BalanceTransaction.objects.all().order_by('-created_at').select_related(
                        'bank')
                else:
                    balance_transactions = BalanceTransaction.objects.filter(user=user).order_by(
                        '-created_at').select_related('bank')
                serialized_data = BalanceTransactionSerializer(balance_transactions, many=True).data
                for data in serialized_data:
                    data['user_profile'] = UserProfileSerializer(
                        get_object_or_404(UserProfile, user_id=data['user'])).data
                    del data['user']
                return Response(APIResponse(success=True, data=serialized_data, message="").__dict__())
            except jwt.ExpiredSignatureError as ex:
                print(str(ex))
                return Response(
                    APIResponse(success=False, data={}, message="Không xác thực được người dùng").__dict__())
        else:
            return Response(APIResponse(success=False, data={}, message="Thiếu token").__dict__())

    def put(self, request, transaction_id):
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
                    # balance_transactions = BalanceTransaction.objects.all().select_related('bank')
                    try:
                        balance_transaction = BalanceTransaction.objects.get(pk=transaction_id, status=0)
                    except BalanceTransaction.DoesNotExist:
                        return Response(
                            APIResponse(success=False, data={}, message="Không tìm thấy dữ liệu").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)

                    try:
                        transaction_status = request.data.get('status')
                        transaction_description = request.data.get('description')
                        if transaction_status is None:
                            return Response(
                                APIResponse(success=False, data={},
                                            message="Trạng thái giao dịch không hợp lệ").__dict__(),
                                status=status.HTTP_400_BAD_REQUEST)
                        else:
                            if transaction_status not in [0, 1, 2]:
                                return Response(
                                    APIResponse(success=False, data={},
                                                message="Trạng thái giao dịch không hợp lệ").__dict__(),
                                    status=status.HTTP_400_BAD_REQUEST)
                        if transaction_status == 2 and transaction_description is None:
                            return Response(
                                APIResponse(success=False, data={},
                                            message="Thiếu lí do hủy").__dict__(),
                                status=status.HTTP_400_BAD_REQUEST)
                        balance_transaction.status = transaction_status
                        balance_transaction.description = transaction_description
                        balance_transaction.save()

                        # Add notification

                        if transaction_status == 2:
                            notification = NotificationModel(category_id=3, title='Rút tiền không thành công',
                                                             content='Lí do: {}'.format(transaction_description),
                                                             user=balance_transaction.user)
                            notification.save()

                        serializer = BankingSerializer(balance_transaction)

                        return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())
                    except Exception as ex:
                        return Response(
                            APIResponse(success=False, data=str(ex), message="Lưu thông tin thất bại").__dict__(),
                            status=status.HTTP_400_BAD_REQUEST)
                else:
                    Response(
                        APIResponse(success=False, data={}, message="Không có quyền chỉnh sửa").__dict__(),
                        status=status.HTTP_403_FORBIDDEN)
            except jwt.ExpiredSignatureError as ex:
                print(str(ex))
                return Response(
                    APIResponse(success=False, data={}, message="Không xác thực được người dùng").__dict__())
        else:
            return Response(APIResponse(success=False, data={}, message="Thiếu token").__dict__())


####################################### BANKING RESTAPI ##############################################################

@permission_classes([IsAuthenticated])
class BankingAPIView(APIView):
    def get(self, request):
        banking = Banking.objects.get(status=True)
        serialized_data = BankingSerializer(banking).data
        return Response(
            APIResponse(success=True, data=serialized_data, message="").__dict__())

    def put(self, request, banking_id):
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
                        banking = Banking.objects.get(pk=banking_id, status=True)
                    except Banking.DoesNotExist:
                        return Response(
                            APIResponse(success=False, data={}, message="Không tìm thấy dữ liệu").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)

                    try:
                        bank_id = request.data.get('bank_id', 1)
                        bank = Bank.objects.get(pk=bank_id)
                        if bank is None:
                            Response(
                                APIResponse(success=False, data={},
                                            message="Thông tin ngân hàng không hợp lệ").__dict__(),
                                status=status.HTTP_400_BAD_REQUEST)
                        else:
                            banking.bank_id = bank_id
                            banking.user_name = request.data.get('user_name', '')
                            banking.bank_number = request.data.get('bank_number', '')
                            banking.save()
                            serializer = BankingSerializer(banking)
                            return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())
                    except Exception as ex:
                        return Response(
                            APIResponse(success=False, data=str(ex), message="Lưu thông tin thất bại").__dict__(),
                            status=status.HTTP_400_BAD_REQUEST)
                else:
                    Response(
                        APIResponse(success=False, data={}, message="Không có quyền chỉnh sửa").__dict__(),
                        status=status.HTTP_403_FORBIDDEN)
            except jwt.ExpiredSignatureError as ex:
                print(str(ex))
                return Response(
                    APIResponse(success=False, data={}, message="Không xác thực được người dùng").__dict__())
        else:
            return Response(
                APIResponse(success=False, data={}, message="Thiếu token").__dict__(),
                status=status.HTTP_404_NOT_FOUND)


# Initial values
START_VALUE = 0
MIN_INCREASE = 50000000  # Minimum increase amount
MAX_INCREASE = 100000000  # Maximum increase amount

# Initialize counters and last reset time
last_reset_time = now()
total_deposit = START_VALUE
total_order_amount = START_VALUE
total_withdraw = START_VALUE


@api_view(['GET'])
@permission_classes([AllowAny])
def count_total(request):
    global last_reset_time, total_deposit, total_order_amount, total_withdraw

    current_time = now()

    # Reset daily at 00:00
    if current_time.date() > last_reset_time.date():
        last_reset_time = current_time
        total_deposit = START_VALUE
        total_order_amount = START_VALUE
        total_withdraw = START_VALUE

    # Calculate minutes since last reset
    minutes_since_reset = (current_time - last_reset_time).total_seconds() / 60

    # Update each counter by a random amount within the range for each minute passed
    total_deposit += int(minutes_since_reset) * random.randint(MIN_INCREASE, MAX_INCREASE)
    total_order_amount += int(minutes_since_reset) * random.randint(MIN_INCREASE, MAX_INCREASE)
    total_withdraw += int(minutes_since_reset) * random.randint(MIN_INCREASE, MAX_INCREASE)

    # Reset the last reset time to current time to avoid multiple increases within the same minute
    last_reset_time = current_time

    return Response(APIResponse(success=True, data={
        'time': current_time.strftime('%Y-%m-%d %H:%M:%S'),
        'total_deposit': total_deposit,
        'total_order_amount': total_order_amount,
        'total_withdraw': total_withdraw
    }, message="").__dict__())
