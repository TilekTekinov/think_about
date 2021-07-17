from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, label='Username', help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
