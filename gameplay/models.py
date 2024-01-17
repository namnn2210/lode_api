from django.db import models
from server.models import City, Subgame
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField(null=False, default=date.today())
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False)
    mode = models.ForeignKey(Subgame, on_delete=models.CASCADE, null=False)
    numbers = models.TextField(null=False, default="")
    pay_number = models.IntegerField(null=False, default=1000)
    total = models.IntegerField(null=False, default=1000)
    win = models.BooleanField(null=False, default=False)
    result = models.TextField(null=False, default="")
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'
