from django.db import models


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


class Game(models.Model):
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255, default='bac')

    class Meta:
        db_table = 'games'


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


class Rate(models.Model):
    rate = models.DecimalField(max_digits=5, default=0.0, decimal_places=2)
    group_id = models.IntegerField(default=1)
    category_id = models.IntegerField(default=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'rates'
