# Generated by Django 5.0.1 on 2024-01-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0010_balancetransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balancetransaction',
            name='amount',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='balancetransaction',
            name='status',
            field=models.CharField(choices=[(0, 'Chờ xử lí'), (2, 'Hủy'), (1, 'Thành công')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='balancetransaction',
            name='transaction_type',
            field=models.CharField(choices=[(1, 'Nạp'), (2, 'Rút')], max_length=20),
        ),
    ]