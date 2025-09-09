from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["name","username", "email", "password"]
