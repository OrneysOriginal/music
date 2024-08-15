from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        label="Введите имя пользователя",
        widget=forms.TextInput(),
    )
    password = forms.CharField(
        max_length=64, widget=forms.PasswordInput(), label="Введите пароль"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(), label="введите электронную почту"
    )


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        label="Введите имя пользователя",
        widget=forms.TextInput(),
    )
    password = forms.CharField(
        max_length=64, widget=forms.PasswordInput(), label="Введите пароль"
    )


class GuestLoginForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        label="Введите имя пользователя",
        widget=forms.TextInput(),
    )
