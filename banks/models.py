from django.db import models


# Create your models here.
class Bank(models.Model):
    name = models.TextField(max_length=255, null=False)
    code = models.CharField(max_length=20, null=False)
    bin = models.CharField(max_length=10, null=False)
    short_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'banks'

    def __str__(self):
        return self.short_name
