# Generated by Django 5.0.1 on 2024-01-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_city_result_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subgame',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='subgame',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]