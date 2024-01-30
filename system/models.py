from django.db import models


# Create your models here.
class SystemModel(models.Model):
    hotline = models.TextField()
    zalo = models.TextField()
    viber = models.TextField()
    telegram = models.TextField()
    google_code = models.TextField(max_length=1000, null=True)
    web_title = models.TextField(max_length=500, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'system'
