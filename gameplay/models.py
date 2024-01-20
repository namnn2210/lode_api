from django.db import models
from server.models import City, Subgame, BalanceTransaction
from datetime import datetime
from django.contrib.auth.models import User
from django.dispatch import receiver


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.TextField(null=False, default=datetime.today().date().strftime("%Y-%m-%d"))
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False)
    mode = models.ForeignKey(Subgame, on_delete=models.CASCADE, null=False)
    numbers = models.TextField(null=False, default="")
    pay_number = models.BigIntegerField(null=False, default=1000)
    total = models.BigIntegerField(null=False, default=1000)
    win = models.BooleanField(null=False, default=False)
    result = models.TextField(null=False, default="")
    note = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        db_table = 'orders'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, null=False, unique=True)
    balance = models.BigIntegerField(default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_profile'


@receiver(models.signals.post_save, sender=BalanceTransaction)
def update_balance_withdraw_deposit(sender, instance, **kwargs):
    user_profile = UserProfile.objects.get(user=instance.user)
    if instance.transaction_type == 1 and instance.status == 1:
        # Assuming you have a Banking object for the user
        user_profile.balance += instance.amount
        user_profile.save()
    if instance.transaction_type == 2 and instance.status == 1:
        # Assuming you have a Banking object for the user
        user_profile.balance -= instance.amount
        user_profile.save()


@receiver(models.signals.post_save, sender=Order)
def update_balance_order(sender, instance, **kwargs):
    user_profile = UserProfile.objects.get(user=instance.user)
    if instance.status == 1:
        # Assuming you have a Banking object for the user
        user_profile.balance -= instance.total
        user_profile.save()
