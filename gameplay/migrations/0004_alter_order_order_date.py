# Generated by Django 5.0.1 on 2024-01-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0003_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.TextField(default='2024-01-26'),
        ),
    ]