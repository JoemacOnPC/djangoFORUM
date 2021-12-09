from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    # required email
    email = forms.EmailField()
    # email = forms.EmailField(required='false')
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']