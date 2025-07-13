from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUsers

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=40 , required=True)
    last_name = forms.CharField(max_length=40 , required=True)
    
    class Meta:
        model = CustomUsers
        fields = ["first_name", "last_name", "username", "password1", "password2",]
