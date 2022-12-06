# Generated by Django 4.1.3 on 2022-12-05 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board_games', '0003_alter_boardgame_edit_date_alter_boardgame_loan_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgame',
            name='owner',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='board_games.boardgamer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='boardgame',
            name='edit_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='boardgame',
            name='loan_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='boardgamer',
            name='nimi',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]
