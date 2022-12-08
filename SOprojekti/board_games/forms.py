from django.forms import ModelForm
from .models import Boardgamer
from .models import Passwords
from .models import Boardgame
from django import forms

class BoardgamerForm(ModelForm):
    class Meta:
        model = Boardgamer
        fields = ['nimi', 'bio', 'puh']

class PasswordsForm(ModelForm):
    class Meta:
        model = Passwords
        fields = ['salasana']
        widgets = {'salasana':forms.PasswordInput}

class Login_Form(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput)

class BoardgameForm(forms.ModelForm):
    class Meta:
        model = Boardgame
        fields = ['nimi','selitys']

        