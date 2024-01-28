from django.contrib.auth.models import User
from django.db.models import Count, Sum
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from authentication.serializers import UserSerializer, UserProfileSerializer
from authentication.models import UserProfile
from gameplay.models import Order
from server.models import BalanceTransaction, APIResponse
from datetime import datetime, timedelta
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
# @permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_user_statistical(request):
    try:
        transaction_counts = BalanceTransaction.objects.filter(status=1).values('user_id', 'transaction_type').annotate(
            transaction_count=Count('transaction_type')
        )

        balance_transaction_sums = BalanceTransaction.objects.filter(
            transaction_type=1,
            status=1
        ).values('user_id').annotate(
            total_amount=Sum('amount')
        )

        balance_transaction_sums_withdraw = BalanceTransaction.objects.filter(
            transaction_type=2,
            status=1
        ).values('user_id').annotate(
            total_amount=Sum('amount')
        )

        user_data = {}

        for item in transaction_counts:
            user_id = item['user_id']
            transaction_type = item['transaction_type']
            count = item['transaction_count']

            if user_id not in user_data:
                user_data[user_id] = {
                    'user': user_id,
                    'deposit': 0,
                    'amount_deposit': 0,
                    'withdraw': 0,
                    'amount_withdraw': 0,
                }

            if transaction_type == '1':
                user_data[user_id]['deposit'] = count
            elif transaction_type == '2':
                user_data[user_id]['withdraw'] = count

        for item in balance_transaction_sums:
            user_id = item['user_id']
            total_amount = item['total_amount']

            if user_id not in user_data:
                user_data[user_id] = {
                    'user': user_id,
                    'deposit': 0,
                    'amount_deposit': 0,
                    'withdraw': 0,
                    'amount_withdraw': 0,
                }

            user_data[user_id]['amount_deposit'] = total_amount

        for item in balance_transaction_sums_withdraw:
            user_id = item['user_id']
            total_amount = item['total_amount']

            if user_id not in user_data:
                user_data[user_id] = {
                    'user': user_id,
                    'deposit': 0,
                    'amount_deposit': 0,
                    'withdraw': 0,
                    'amount_withdraw': 0,
                }

            user_data[user_id]['amount_withdraw'] = total_amount

        user_data_list = list(user_data.values())

        for user_info in user_data_list:
            user_profile = UserProfileSerializer(get_object_or_404(UserProfile, pk=user_info['user'])).data
            user_info['user_profile'] = user_profile

        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(user_data_list, request)

        return Response(APIResponse(success=True, data=result_page, message="").__dict__())
    except Exception as ex:
        print(str(ex))
        return Response(APIResponse(success=False, data={}, message="Không thể lấy dữ liệu").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_statistical_by_date(request):
    try:
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)
        if start_date:
            start_date = datetime.fromisoformat(start_date.rstrip("Z")).date()  # Get the first parameter
        else:
            start_date = datetime.now().date()
        if end_date:
            end_date = datetime.fromisoformat(end_date.rstrip("Z")).date()  # Get the first parameter
        else:
            end_date = start_date + timedelta(days=1)
        return_data = {'date': start_date.strftime("%Y-%m-%d")}
        print(return_data)
        sum_deposit = BalanceTransaction.objects.filter(
            transaction_type=1,
            status=1,
            created_at__gte=start_date,
            created_at__lte=end_date
        ).aggregate(Sum('amount'))
        print(sum_deposit)
        sum_withdraw = BalanceTransaction.objects.filter(
            transaction_type=2,
            status=1,
            created_at__gte=start_date,
            created_at__lte=end_date
        ).aggregate(Sum('amount'))
        print(sum_withdraw)
        return_data['sum_deposit'] = sum_deposit['amount__sum'] if sum_deposit['amount__sum'] is not None else 0
        return_data['withdraw_deposit'] = sum_withdraw['amount__sum'] if sum_withdraw[
                                                                             'amount__sum'] is not None else 0

        total_win = Order.objects.filter(
            order_date__gte=start_date,
            order_date__lte=end_date,
            win=True
        ).count()

        total_lost = Order.objects.filter(
            order_date__gte=start_date,
            order_date__lte=end_date,
            win=False
        ).count()

        return_data['total_win'] = total_win
        return_data['total_lost'] = total_lost

        return Response(APIResponse(success=True, data=return_data, message="").__dict__())
    except Exception as ex:
        return Response(APIResponse(success=False, data=str(ex), message="Không thể lấy dữ liệu").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)
