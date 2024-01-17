# Generated by Django 5.0.1 on 2024-01-17 16:10

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('server', '0006_rate_alter_game_table_alter_subgame_table'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(default=datetime.date(2024, 1, 17))),
                ('numbers', models.TextField(default='')),
                ('pay_number', models.IntegerField(default=1000)),
                ('total', models.IntegerField(default=1000)),
                ('win', models.BooleanField(default=False)),
                ('result', models.TextField(default='')),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.city')),
                ('mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.subgame')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
