from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 


class UserRegistrationForm(UserCreationForm):
    password2 = forms.CharField(label ='Confirm password',widget= forms.PasswordInput)
    class Meta:
        model = User
     
        fields=['username','email']
        labels = {'email' : 'Email'}