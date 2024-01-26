from django.db import models
from django.contrib.auth.models import User


class NotificationCategoryModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notification_category'

    def __str__(self):
        return self.name


# Create your models here.
class NotificationModel(models.Model):
    category = models.ForeignKey(NotificationCategoryModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.TextField(max_length=255)
    content = models.TextField(max_length=500)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notification'
