from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from authentication.models import UserProfile
from authentication.serializers import UserSerializer, UserProfileSerializer
from .models import City, Game, Subgame, Rate, Banking
from server.models import APIResponse
from gameplay.models import Order, BalanceTransaction
from banks.models import Bank
from datetime import datetime
from .serializer import GameSerializer, SubGameSerializer, CitySerializer, RateSerializer, BankingSerializer, \
    BalanceTransactionSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework import status
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
        weekday = today.weekday()
        print('day of week', weekday)
    else:
        date_object = datetime.fromisoformat(query_date)
        weekday = date_object.weekday()
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
        html_response = requests.get(url).text
        weekday_regex = r'<td class="thu"\s>\s{0,}(.*?)<\/td>'
        date_regex = r'<td class="ngay">\s{0,}Ng&agrave;y:\s(.*?)\s<\/td>'
        db_regex = r'<td class="giaidb">\s{0,}(.*?)<\/td>'
        giai1_regex = r'<td class="giai1">\s{0,}(.*?)<\/td>'
        giai2_regex = r'<td class="giai2">\s{0,}(.*?)<\/td>'
        giai3_regex = r'<td class="giai3">\s{0,}(.*?)<\/td>'
        giai4_regex = r'<td class="giai4">\s{0,}(.*?)<\/td>'
        giai5_regex = r'<td class="giai5">\s{0,}(.*?)<\/td>'
        giai6_regex = r'<td class="giai6">\s{0,}(.*?)<\/td>'
        giai7_regex = r'<td class="giai7">\s{0,}(.*?)<\/td>'
        giai8_regex = r'<td class="giai8">\s{0,}(.*?)<\/td>'

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

        print(weekday_data)
        formatted_date_data = date_data.replace('/', '-')

        title = f'{weekday_data} ngày {formatted_date_data}'
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
@permission_classes([IsAuthenticated])
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
    amount = body['amount']
    bank_id = body['bank_id']
    user_name = body['user_name']
    bank_number = body['bank_number']
    bank = get_object_or_404(Bank, pk=bank_id)
    if int(amount) > user_profile.balance:
        return Response(
            APIResponse(success=False, data={}, message="Số dư không đủ").__dict__())
    # Get all orders
    orders = Order.objects.filter(user=user)
    total_amount_order = 0
    for order in orders:
        total_amount_order += order.total
    # Get all deposit
    deposits = BalanceTransaction.objects.filter(user=user, transaction_type=1, status=1)
    total_amount_deposit = 0
    for deposit in deposits:
        total_amount_deposit += deposit.amount

    if total_amount_order < total_amount_deposit:
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
# @permission_classes([IsAuthenticated])
class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.filter(is_active=1)
        serializer = UserSerializer(users, many=True)
        return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())

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
            user = User.objects.get(pk=user_id, is_active=1)
        except User.DoesNotExist:
            return Response(APIResponse(success=False, data={}, message="Dữ liệu không tồn tại").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)

        try:
            request_data_first_name = request.data.get("first_name")
            user.first_name = request_data_first_name
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
            user = User.objects.get(pk=user_id, is_active=1)
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

        serializer = UserProfileSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())
        return Response(APIResponse(success=False, data=serializer.errors, message="Lưu thông tin thất bại").__dict__(),
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


####################################### BALANCE TRANSACTIONS RESTAPI ##############################################################
@permission_classes([IsAuthenticated])
class BalanceTransactionsAPIView(APIView):

    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10
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
                balance_transactions = BalanceTransaction.objects.filter(user=user).select_related('bank')
                result_page = paginator.paginate_queryset(balance_transactions, request)
                serialized_data = BalanceTransactionSerializer(result_page, many=True).data
                return Response(APIResponse(success=True, data=serialized_data, message="").__dict__())
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

                    serializer = BankingSerializer(banking, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())
                    return Response(
                        APIResponse(success=False, data=serializer.errors, message="Lưu thông tin thất bại").__dict__(),
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
