from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserAssociate


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = UserAssociate
        fields = ('email', 'username', 'password1', 'password2')


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = UserAssociate
        fields = ('email', 'username')
