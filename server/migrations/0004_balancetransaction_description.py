# Generated by Django 5.0.1 on 2024-01-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_remove_balancetransaction_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='balancetransaction',
            name='description',
            field=models.TextField(default='', max_length=255),
        ),
    ]