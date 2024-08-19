from django import forms
from django.core.validators import validate_email, validate_slug


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        label="Введите имя пользователя",
        widget=forms.TextInput(),
        validators=[validate_slug],
    )
    password = forms.CharField(
        min_length=8,
        max_length=64,
        widget=forms.PasswordInput(),
        label="Введите пароль",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(),
        label="введите электронную почту",
        validators=[validate_email],
    )


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        label="Введите имя пользователя",
        widget=forms.TextInput(),
        validators=[validate_slug],
    )
    password = forms.CharField(
        max_length=64, widget=forms.PasswordInput(), label="Введите пароль"
    )


class GuestLoginForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        label="Введите имя пользователя",
        widget=forms.TextInput(),
        validators=[validate_slug],
    )
