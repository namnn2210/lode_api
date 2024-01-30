from django.db import models
from server.models import City, Subgame, BalanceTransaction
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.TextField(null=False, default=datetime.today().date().strftime("%Y-%m-%d"))
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False)
    mode = models.ForeignKey(Subgame, on_delete=models.CASCADE, null=False)
    numbers = models.JSONField()
    bet_amount = models.IntegerField(default=1000)
    pay_number = models.BigIntegerField(null=False, default=1000)
    total = models.BigIntegerField(null=False, default=1000)
    win = models.BooleanField(default=None)
    result = models.TextField(null=False, default="")
    note = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'
