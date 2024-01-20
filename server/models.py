from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    feature = models.IntegerField(default=0)
    time_release = models.CharField(max_length=8)
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
    min_amount = models.IntegerField(default=0)
    max_amount = models.BigIntegerField(default=0)
    multi = models.IntegerField(default=0)
    code = models.CharField(max_length=255)
    max = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    max_number = models.IntegerField(default=0)

    class Meta:
        db_table = 'subgames'

    def __str__(self):
        return self.name


class Rate(models.Model):
    rate = models.DecimalField(max_digits=5, default=0.0, decimal_places=2)
    group_id = models.IntegerField(default=1)
    category_id = models.IntegerField(default=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'rates'


class Banking(models.Model):
    bank_name = models.CharField(max_length=255, default='VIB')
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
    description = models.CharField(max_length=100, default='', blank=True)
    amount = models.BigIntegerField(default=0)
    status = models.CharField(max_length=20,
                              choices=[(0, 'Chờ xử lí'), (2, 'Hủy'), (1, 'Thành công')],
                              default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'balance_transactions'



