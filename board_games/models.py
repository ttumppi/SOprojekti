from django.db import models

# Create your models here.

class Boardgame(models.Model):
    """A boardgame"""
    selitys = models.CharField(max_length=200)

    def __str__(self):
        return self.selitys