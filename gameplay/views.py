from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order, UserProfile
from server.models import City, Subgame, APIResponse
from django.db.models import Q
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .serializers import OrderSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
import json


@permission_classes([IsAuthenticated])
class OrderView(APIView):
    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        user = get_object_or_404(User, pk=body['user_id'])
        city = get_object_or_404(City, pk=body['city_id'])
        mode = get_object_or_404(Subgame, pk=body['mode_id'])
        user_profile = get_object_or_404(UserProfile, user=user)

        if body['total'] > user_profile.balance:
            return Response(APIResponse(success=False, data={}, message="Không đủ số dư trong tài khoản").__dict__())

        time_release = city.time_release
        time_release_object = datetime.strptime(time_release, "%H:%M:%S").time()
        order_date = body['order_date']
        order_date_obj = datetime.strptime(order_date, "%Y-%m-%dT%H:%M:%S.%fZ").date()
        today_date = datetime.now().date()
        current_time = datetime.strptime(datetime.now().time().strftime("%H:%M:%S"), "%H:%M:%S").time()

        print(order_date_obj, today_date)
        print(current_time, time_release_object)

        # Kiểm tra trò chơi có đúng vùng hay không
        if mode.region == city.region:
            # Kiểm tra thời gian đặt lệnh đã quá thời gian có kết quả chưa
            if today_date == order_date_obj and current_time > time_release_object:
                order_date_obj = today_date + timedelta(days=1)
            elif today_date > order_date_obj:
                order_date_obj = today_date

            order = Order(user=user, city=city, mode=mode, order_date=order_date_obj.strftime("%Y-%m-%d"),
                          numbers=body['numbers'],
                          pay_number=body['pay_number'], total=body['total'])
            order_dict = OrderSerializer(order).data
            order.save()
            return Response(APIResponse(success=True, data=order_dict, message="").__dict__())
        else:
            return Response(
                APIResponse(success=False, data={}, message="Thành phố và chế độ chơi không hợp lệ").__dict__())

    def get(self, request):
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
        filtered_records = Order.objects.filter(
            Q(created_at__gte=start_date) & Q(created_at__lte=end_date)).select_related('city', 'mode')
        result_page = paginator.paginate_queryset(filtered_records, request)
        serialized_data = OrderSerializer(result_page, many=True).data
        return Response(
            APIResponse(success=True, data=serialized_data, message="").__dict__())
