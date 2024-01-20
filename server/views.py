from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import City, Game, Subgame, Rate, Banking
from gameplay.models import Order, BalanceTransaction
from datetime import date
from .serializer import GameSerializer, SubGameSerializer, CitySerializer, RateSerializer, BankingSerializer, BalanceTransactionSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import requests
import json


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_cities(request):
    regions = ['bac', 'trung', 'nam']
    current_date = date.today().strftime('%m-%d-%Y')
    data = []
    for region in regions:
        url = f'https://api-sg.quayso1.com/lotte/cities?date={current_date}&region={region}'
        response = requests.get(url)
        if response.status_code == 200:
            data += response.json()['rows']
    for item in data:
        city = City(id=item['id'], name=item['name'], region=item['region'], date=item['date'], feature=item['feature'],
                    time_release=item['time_release'], status=item['status'], created_at=item['created_at'],
                    updated_at=item['updated_at'])
        city.save()
    return Response({'cities': data})


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

    return Response({
        "success": True,
        "rows": list_games,
        "attrs": []
    })


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_cities(request, region):
    cities = CitySerializer(City.objects.filter(region=region), many=True).data
    return Response({
        "success": True,
        "rows": cities,
        "attrs": []
    })


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_cities(request, region=None):
    if region:
        cities = CitySerializer(City.objects.filter(region=region), many=True).data
    else:
        cities = CitySerializer(City.objects.all(), many=True).data
    return Response({
        "success": True,
        "rows": cities,
        "attrs": []
    })


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_rates(request):
    rates = RateSerializer(Rate.objects.all(), many=True).data
    return Response({
        "success": True,
        "rows": rates,
        "attrs": []
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_banking(request):
    banking = BankingSerializer(Banking.objects.filter(status=True)).data
    return Response({
        "success": True,
        "rows": banking,
        "attrs": []
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def withdraw(request):
    """
    :body request:
    {
        "user_id":1
        "amount":27000
    }
    :return:
    """
    body = json.loads(request.body.decode('utf-8'))
    user = get_object_or_404(User, pk=body['user_id'])
    amount = body['amount']
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
        return Response({
            "success": False,
            "rows": {},
            "attrs": ['Số tiền đặt cược ít hơn số tiền đã nạp vào']
        })

    withdraw = BalanceTransaction(user=user, transaction_type=2, status=0, amount=amount)
    withdraw.save()

    withdraw_serializer = BalanceTransactionSerializer(withdraw).data

    return Response({
        "success": True,
        "rows": withdraw_serializer,
        "attrs": []
    })

