from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CustomRegisterForm(UserCreationForm):
    email_Id = forms.EmailField()  # by default it is mandatory, ie, required = True

    class Meta:
        model = User
        fields = ["email_Id", "username", "password1", "password2"]
