# Generated by Django 5.0.1 on 2024-01-30 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0008_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.TextField(default='2024-01-31'),
        ),
        migrations.AlterField(
            model_name='order',
            name='win',
            field=models.BooleanField(default=None),
        ),
    ]
