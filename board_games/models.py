from django.db import models

# Create your models here.

class Boardgame(models.Model):
    """A boardgame"""
    nimi = models.CharField(max_length=20, default='')
    selitys = models.CharField(max_length=200)

    def __str__(self):
        return self.nimi

class Boardgamer(models.Model):
    """Gamer"""
    nimi = models.CharField(max_length=20, default='')
    varaukset = models.IntegerField()

    def __str__(self):
        return self.nimi