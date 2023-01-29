from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
        )


class OwnerCreationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.NumberInput()
    email = forms.EmailField()
    password = forms.PasswordInput()