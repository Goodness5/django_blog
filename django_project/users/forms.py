from dataclasses import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User #form data will be saved in the User model
        fields = ['email','username','password1','password2']