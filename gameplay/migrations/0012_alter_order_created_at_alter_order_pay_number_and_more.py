# Generated by Django 5.0.1 on 2024-01-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0011_order_status_alter_order_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default='2024-01-20 22:26:03'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pay_number',
            field=models.BigIntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.BigIntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(default='2024-01-20 22:26:03'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='balance',
            field=models.BigIntegerField(default=0),
        ),
    ]
