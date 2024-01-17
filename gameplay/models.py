from django.db import models
from server.models import City
from datetime import date

# Create your models here.
class Order(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False)
    order_date = models.DateField(null=False, default=date.today())

