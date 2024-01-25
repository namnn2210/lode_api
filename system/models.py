from django.db import models


# Create your models here.
class SystemModel(models.Model):
    hotline = models.TextField()
    zalo = models.TextField()
    viber = models.TextField()
    telegram = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'system'
