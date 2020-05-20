from django import forms
from django.forms import modelform_factory

from homepage.models import MyUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

AddUserForm = modelform_factory(MyUser, exclude=[])