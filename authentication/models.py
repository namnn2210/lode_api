from django.db import models
from server.models import BalanceTransaction
from gameplay.models import Order
from notification.models import NotificationModel
from django.contrib.auth.models import User
from django.dispatch import receiver

import random
import string


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, null=False, unique=True)
    balance = models.BigIntegerField(default=0)
    code = models.CharField(max_length=15, unique=True, null=True, blank=True)
    ip_address = models.TextField(max_length=50, null=True)
    read_noti = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_profile'

    def save(self, *args, **kwargs):
        if not self.code:
            prefix = "LD"
            random_digits = ''.join(random.choices(string.digits, k=10))
            code = prefix + random_digits
            self.code = code
        super().save(*args, **kwargs)


@receiver(models.signals.post_save, sender=NotificationModel)
def update_noti_status(sender, instance, **kwargs):
    user_profile = UserProfile.objects.get(user=instance.user)
    if not user_profile.read_noti:
        user_profile.read_noti = True
        user_profile.save()


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
    if instance.status == 0:
        # Assuming you have a Banking object for the user
        user_profile.balance -= instance.pay_number
        if user_profile.balance < 0:
            user_profile.balance = 0
        user_profile.save()
