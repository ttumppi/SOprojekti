from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from passlib.hash import pbkdf2_sha256 as handler

# Create your models here.

class Boardgame(models.Model):
    """A boardgame"""
    nimi = models.CharField(max_length=20, default='')
    selitys = models.CharField(max_length=200)
    boardgamer = models.ForeignKey('Boardgamer', on_delete=models.CASCADE, null=True)
    date  =models.DateTimeField(auto_now_add=True)
    loan_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    edit_date = models.DateTimeField(auto_now = False, auto_now_add= False)
    owner = models.ForeignKey('Boardgamer', on_delete=models.CASCADE, null=True, related_name='owner')
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
    bio = models.CharField(max_length=50)
    puh = models.IntegerField(default=0)

    def __str__(self):
        return self.nimi

class Passwords(models.Model):

    salasana = models.CharField(max_length=150)
    username = models.OneToOneField(Boardgamer, 
    on_delete=models.CASCADE, primary_key=True)

    def hash(password_object, user_object):

        password_object.salasana = handler.hash(password_object.salasana)
        password_object.username = user_object
        user_object.save()
        password_object.save()
        return user_object.id
    def hash_check(input, passwords):
        password_object = Passwords.objects.get(username=passwords)
        if handler.verify(input, password_object.salasana) == True:
            return True
        else:
            return False


# class User_Info(models.Model):
#     username = models.CharField(max_length=20)
#     gamer_id = models.IntegerField()