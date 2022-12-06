from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from passlib.hash import pbkdf2_sha256

# Create your models here.

class Boardgame(models.Model):
    """A boardgame"""
    nimi = models.CharField(max_length=20, default='')
    selitys = models.CharField(max_length=200)
    boardgamer = models.ForeignKey('Boardgamer', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nimi

class Boardgamer(models.Model):
    """Gamer validaattoreilla"""
    nimi = models.CharField(max_length=20, default='')
    varaukset = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(3),
        MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.nimi

class Passwords(models.Model):

    salasana = models.CharField(max_length=20)
    username = models.OneToOneField(Boardgamer, 
    on_delete=models.CASCADE, primary_key=True)
    
    def verify_password(self, raw_salasana):
        return pbkdf2_sha256.verify(raw_salasana, self.salasana)

# class User_Info(models.Model):
#     username = models.CharField(max_length=20)
#     gamer_id = models.IntegerField()