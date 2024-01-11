# Generated by Django 5.0.1 on 2024-01-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_game_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('group_id', models.IntegerField(default=1)),
                ('category_id', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'rates',
            },
        ),
        migrations.AlterModelTable(
            name='game',
            table='games',
        ),
        migrations.AlterModelTable(
            name='subgame',
            table='subgames',
        ),
    ]
