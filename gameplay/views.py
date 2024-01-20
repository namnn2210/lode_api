from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order
from server.models import City, Subgame
from django.db.models import Q
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .serializers import OrderSerializer
from rest_framework.pagination import PageNumberPagination
import json


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_order(request):
    body = json.loads(request.body.decode('utf-8'))
    user = get_object_or_404(User, pk=body['user_id'])
    city = get_object_or_404(City, pk=body['city_id'])
    mode = get_object_or_404(Subgame, pk=body['mode_id'])
    time_release = city.time_release
    time_release_object = datetime.strptime(time_release, "%H:%M:%S").time()
    order_date = body['order_date']
    order_date_obj = datetime.strptime(order_date, "%Y-%m-%d").date()
    today_date = datetime.now().date()

    print(order_date_obj, today_date)

    # Kiểm tra trò chơi có đúng vùng hay không
    if mode.region == city.region:
        # Kiểm tra thời gian đặt lệnh đã quá thời gian có kết quả chưa
        if today_date == order_date_obj and datetime.now().time() > time_release_object:
            order_date = today_date + timedelta(days=1)
        elif today_date > order_date_obj:
            order_date = today_date

        order = Order(user=user, city=city, mode=mode, order_date=order_date.strftime("%Y-%m-%d"),
                      numbers=body['numbers'],
                      pay_number=body['pay_number'], total=body['total'])
        order_dict = OrderSerializer(order).data
        order.save()
        return Response({
            "success": True,
            "rows": order_dict,
            "attrs": []
        })
    else:
        return Response({
            "success": False,
            "rows": {},
            "attrs": ['Invalid city and game mode']
        })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_orders(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    if request.query_params.get('start_date'):
        start_date = datetime.strptime(request.query_params.get('start_date'),
                                       "%Y-%m-%d").date()  # Get the first parameter
    else:
        start_date = datetime.now().date()
    if request.query_params.get('end_date'):
        end_date = datetime.strptime(request.query_params.get('end_date'),
                                     "%Y-%m-%d").date()  # Get the second parameter
    else:
        end_date = datetime.now().date() + timedelta(days=1)
    print(start_date, end_date)
    filtered_records = Order.objects.filter(Q(created_at__gte=start_date) & Q(created_at__lte=end_date))
    result_page = paginator.paginate_queryset(filtered_records, request)
    serialized_data = OrderSerializer(result_page, many=True).data
    return Response({
        "success": True,
        "rows": serialized_data,
        "attrs": []
    })


