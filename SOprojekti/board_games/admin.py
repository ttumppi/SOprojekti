from django.contrib import admin
from .models import Boardgame, Boardgamer, Passwords

admin.site.register(Boardgame)
admin.site.register(Boardgamer)
admin.site.register(Passwords)
# Register your models here.
