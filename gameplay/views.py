from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order
from authentication.models import UserProfile
from server.models import City, Subgame, APIResponse, BalanceTransaction
from django.db.models import Q
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .serializers import OrderSerializer
from authentication.serializers import UserSerializer, UserProfileSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django.db.models import Count
import json


@permission_classes([IsAuthenticated])
class OrderView(APIView):
    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        user = get_object_or_404(User, pk=body['user_id'])
        city = get_object_or_404(City, pk=body['city_id'])
        mode = get_object_or_404(Subgame, pk=body['mode_id'])
        user_profile = get_object_or_404(UserProfile, user=user)

        pay_number = mode.pay_number * 1000
        len_number = len(body['numbers'])
        total = pay_number * len_number

        # Check du so du trong tai khoan hay khong
        if total > user_profile.balance:
            return Response(APIResponse(success=False, data={}, message="Không đủ số dư trong tài khoản").__dict__())

        # Check da nap du 100k hay khong
        balance_transactions = BalanceTransaction.objects.filter(user=user, transaction_type=1, status=1)
        total_deposit = 0
        for transaction in balance_transactions:
            total_deposit += transaction.amount
        if total_deposit < 100000:
            return Response(APIResponse(success=False, data={},
                                        message="Không thể đặt cược nếu chưa nạp đủ 100.000 VND").__dict__())

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

            # Kiem tra da post do so luong number len chua
            numbers= body['numbers']
            if mode.max_number != 0:
                if len(numbers) > mode.max_number:
                    return Response(APIResponse(success=False, data={}, message="Thành phố và chế độ chơi không hợp lệ").__dict__())

            order = Order(user=user, city=city, mode=mode, order_date=order_date_obj.strftime("%Y-%m-%d"),
                          numbers=body['numbers'],
                          pay_number=pay_number, total=total)
            order_dict = OrderSerializer(order).data
            order.save()
            return Response(APIResponse(success=True, data=order_dict, message="").__dict__())
        else:
            return Response(
                APIResponse(success=False, data={}, message="Thành phố và chế độ chơi không hợp lệ").__dict__())

    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        if request.query_params.get('start_date') and request.query_params.get('end_date'):
            start_date = datetime.strptime(request.query_params.get('start_date'), "%Y-%m-%d").date()
            end_date = datetime.strptime(request.query_params.get('end_date'),
                                         "%Y-%m-%d").date()  # Get the second parameter

            print(start_date, end_date)
            records = Order.objects.filter(
                Q(created_at__gte=start_date) & Q(created_at__lte=end_date)).select_related('city', 'mode', 'user')
        else:
            records = Order.objects.all().select_related('city', 'mode', 'user')
        result_page = paginator.paginate_queryset(records, request)
        serialized_data = OrderSerializer(result_page, many=True).data
        for data in serialized_data:
            data['user_profile'] = UserProfileSerializer(
                get_object_or_404(UserProfile, user_id=data['user']['id'])).data
            del data['user']
        return Response(
            APIResponse(success=True, data=serialized_data, message="").__dict__())

    def put(self, request, order_id):
        try:
            order = Order.objects.get(pk=order_id, status=True)
        except Order.DoesNotExist:
            return Response(APIResponse(success=False, data={}, message="Không tìm thấy lệnh").__dict__(),
                            status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(APIResponse(success=True, data=serializer.data, message="").__dict__())
        return Response(APIResponse(success=False, data=serializer.errors, message="Validation error").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)
