# Generated by Django 5.0.1 on 2024-01-27 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bet_amount',
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.TextField(default='2024-01-28'),
        ),
    ]