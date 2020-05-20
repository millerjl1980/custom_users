from django import forms
from homepage.models import MyUser
from django.forms import modelform_factory
from django.contrib.auth.forms import UserCreationForm

from homepage.models import MyUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

# AddUserForm = modelform_factory(MyUser, exclude=[])
class AddUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'display_name', 
                  'age', 'username', 'password1', 'password2')