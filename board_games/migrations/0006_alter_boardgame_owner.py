# Generated by Django 4.1.3 on 2022-12-05 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board_games', '0005_alter_boardgame_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgame',
            name='owner',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='board_games.boardgamer'),
            preserve_default=False,
        ),
    ]