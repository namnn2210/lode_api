from django.db import models
from django.contrib.auth.models import User
from banks.models import Bank
from datetime import datetime


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    feature = models.IntegerField(default=0)
    time_release = models.CharField(max_length=8)
    result_domain = models.CharField(max_length=50, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'cities'

    def __str__(self):
        return self.name


class Game(models.Model):
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255, default='bac')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'games'

    def __str__(self):
        return self.name


class Subgame(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    guide = models.TextField(max_length=255)
    rate = models.IntegerField(default=0)
    pay_number = models.IntegerField(default=0)
    min_amount = models.IntegerField(default=1000)
    max_amount = models.BigIntegerField(default=10000000000)
    multi = models.IntegerField(default=0)
    code = models.CharField(max_length=255)
    max = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    max_number = models.IntegerField(default=0)

    class Meta:
        db_table = 'subgames'

    def __str__(self):
        return self.name


class Rate(models.Model):
    rate = models.DecimalField(max_digits=5, default=0.0, decimal_places=2)
    group_id = models.IntegerField(default=1)
    category_id = models.IntegerField(default=1)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'rates'


class Banking(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=255, default='DO VAN NINH')
    bank_number = models.CharField(max_length=255, default='563633686')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'banking'


class BalanceTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=[(1, 'Nạp'), (2, 'Rút')])
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=255, default='DO VAN NINH')
    bank_number = models.CharField(max_length=255, default='563633686')
    description = models.TextField(max_length=255, default='')
    amount = models.BigIntegerField(default=0)
    status = models.CharField(max_length=20,
                              choices=[(0, 'Chờ xử lí'), (2, 'Hủy'), (1, 'Thành công')],
                              default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'balance_transactions'


class APIResponse:
    def __init__(self, success, data, message):
        self.success = success
        self.data = data
        self.message = message

    def __dict__(self):
        return {
            'success': self.success,
            'data': self.data,
            'message': self.message
        }
