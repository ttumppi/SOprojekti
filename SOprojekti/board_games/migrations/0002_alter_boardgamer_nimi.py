# Generated by Django 4.1.3 on 2022-12-07 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgamer',
            name='nimi',
            field=models.CharField(default='', max_length=20),
        ),
    ]
