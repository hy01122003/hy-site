from django.forms import ModelForm
from django.db import models
import django.forms as forms_
from .models import *


class cookie(forms_.Form):
    Write = forms_.CharField(max_length=20)

class Login(ModelForm):
    class Meta:
        model = Account
        fields = ['Username', 'Password']
        widgets = {
            'Password' : forms_.PasswordInput,
            }

class Sign(ModelForm):
    class Meta:
        model = Account
        fields = ['Username', 'Password', 'FullName']
        widgets = {
            'Password' : forms_.PasswordInput,       
            }
