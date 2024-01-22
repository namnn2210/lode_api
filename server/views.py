from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from authentication.models import UserProfile
from .models import City, Game, Subgame, Rate, Banking
from server.models import APIResponse
from gameplay.models import Order, BalanceTransaction
from banks.models import Bank
from datetime import date, datetime
from .serializer import GameSerializer, SubGameSerializer, CitySerializer, RateSerializer, BankingSerializer, \
    BalanceTransactionSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
import pytz
import requests
import json
import jwt

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
# @permission_classes([IsAuthenticated])
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
# @permission_classes([IsAuthenticated])
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
        cities = CitySerializer(City.objects.filter(Q(date__contains=str(weekday)) | Q(date='') & Q(region=region)),
                                many=True).data
    else:
        cities = CitySerializer(City.objects.filter(Q(date__contains=str(weekday)) | Q(date='')), many=True).data
    return Response(APIResponse(success=True, data=cities, message="").__dict__())


# @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# def get_all_cities(request, region=None):
#     if region:
#         cities = CitySerializer(City.objects.filter(region=region), many=True).data
#     else:
#         cities = CitySerializer(City.objects.all(), many=True).data
#     return Response(APIResponse(success=True, data=cities, message="").__dict__())


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_balance_transactions(request):
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
            return Response(APIResponse(success=False, data={}, message="Không xác thực được người dùng").__dict__())
    else:
        return Response(APIResponse(success=False, data={}, message="Thiếu token").__dict__())
