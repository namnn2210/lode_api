# Generated by Django 5.0.1 on 2024-01-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_alter_subgame_guide_alter_subgame_max_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balancetransaction',
            name='bank_number',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='balancetransaction',
            name='user_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
