# Generated by Django 5.0.1 on 2024-01-20 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='code',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
