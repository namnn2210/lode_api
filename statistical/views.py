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
@permission_classes([IsAuthenticated])
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

        win_counts = Order.objects.values('user_id', 'win').annotate(
            win_count=Count('win')
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
                    'win': 0,
                    'lost': 0
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
                    'win': 0,
                    'lost': 0
                }

            user_data[user_id]['amount_deposit'] = total_amount

        for item in win_counts:
            user_id = item['user_id']
            win_status = item['win']
            count = item['win_count']

            if user_id not in user_data:
                user_data[user_id] = {
                    'user': user_id,
                    'deposit': 0,
                    'amount_deposit': 0,
                    'withdraw': 0,
                    'win': 0,
                    'lost': 0
                }

            # Update win counts
            if win_status:
                user_data[user_id]['win'] = count
            else:
                user_data[user_id]['lost'] = count

        user_data_list = list(user_data.values())

        for user_info in user_data_list:
            user_profile = UserProfileSerializer(get_object_or_404(UserProfile, pk=user_info['user'])).data
            user_info['user'] = user_profile

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
        date = request.query_params.get('date', None)
        if date:
            start_date = datetime.strptime(date,
                                           "%Y-%m-%d").date()  # Get the first parameter
        else:
            start_date = datetime.now().date()
        end_date = start_date + timedelta(days=1)
        return_data = {'date': start_date.strftime("%Y-%m-%d")}
        print(return_data)
        sum_deposit = BalanceTransaction.objects.filter(
            transaction_type=1,
            status=1,
            created_at__gte=start_date,
            created_at__lt=end_date
        ).aggregate(Sum('amount'))
        withdraw_deposit = BalanceTransaction.objects.filter(
            transaction_type=2,
            status=1,
            created_at__gte=start_date,
            created_at__lt=end_date
        ).aggregate(Sum('amount'))
        return_data['sum_deposit'] = sum_deposit['amount__sum'] if sum_deposit['amount__sum'] is not None else 0
        return_data['withdraw_deposit'] = withdraw_deposit['amount__sum'] if withdraw_deposit[
                                                                                 'amount__sum'] is not None else 0

        order_stats = Order.objects.filter(
            order_date__gte=start_date,
            order_date__lt=end_date
        ).aggregate(
            total_win=Sum('win', filter=Q(win=True)),
            total_lost=Sum('win', filter=Q(win=False))
        )
        return_data['total_win'] = order_stats['total_win'] if order_stats['total_win'] is not None else 0
        return_data['total_lost'] = order_stats['total_lost'] if order_stats['total_lost'] is not None else 0

        return Response(APIResponse(success=True, data=return_data, message="").__dict__())
    except Exception as ex:
        return Response(APIResponse(success=False, data={}, message="Không thể lấy dữ liệu").__dict__(),
                        status=status.HTTP_400_BAD_REQUEST)