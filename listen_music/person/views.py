from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, reverse, redirect
from django.views import View
from django.contrib.messages import error, success

from person.forms import UserRegistrationForm, UserLoginForm, GuestLoginForm


class RegistrationView(View):
    def get(self, *args, **kwargs):
        if (
            not self.request.user.is_authenticated
            and not self.request.session.get("username")
        ):
            context = {
                "title": "Регистрация",
                "form": UserRegistrationForm,
            }
            return render(
                self.request, "person/registration.html", context=context
            )

        error(self.request, "Вы аутентифицированы")
        return redirect(reverse("music:mainpage"))

    def post(self, *args, **kwargs):
        if (
            not self.request.user.is_authenticated
            and not self.request.session.get("username")
        ):
            form = UserRegistrationForm(self.request.POST or None)
            if form.is_valid():
                User.objects.create_user(
                    username=self.request.POST.get("username"),
                    password=self.request.POST.get("password"),
                    email=self.request.POST.get("email"),
                )
                success(self.request, "Вы успешно зарегистрированы")
                return redirect(reverse("person:login"))

            error(self.request, "Введите корректные данные")
            return redirect(reverse("person:login"))

        error(self.request, "Вы аутентифицированы")
        return redirect(reverse("music:mainpage"))


class LoginView(View):
    def get(self, *args, **kwargs):
        if (
            not self.request.user.is_authenticated
            and not self.request.session.get("username")
        ):
            context = {
                "title": "Логин",
                "form": UserLoginForm,
            }
            return render(self.request, "person/login.html", context=context)

        error(self.request, "Вы аутентифицированы")
        return redirect(reverse("music:mainpage"))

    def post(self, *args, **kwargs):
        if (
            not self.request.user.is_authenticated
            and not self.request.session.get("username")
        ):
            form = UserLoginForm(self.request.POST or None)
            if form.is_valid():
                username = self.request.POST.get("username")
                try:
                    user = User.objects.get(username=username)
                except ObjectDoesNotExist:
                    error(
                        self.request,
                        "Пользователя с таким именем не существует",
                    )
                    return redirect(reverse("person:login"))
                else:
                    password = self.request.POST.get("password")
                    user = User.objects.get(username=username)
                    if user.check_password(password):
                        login(self.request, user)
                        success(self.request, "Вы успешно вошли в аккаунт")
                        return redirect(reverse("music:mainpage"))

                    error(self.request, "Неверный пароль")
                    return redirect(reverse("person:login"))

            error(self.request, "Введите корректные данные")
            return redirect(reverse("person:login"))

        error(self.request, "Вы аутентифицированы")
        return redirect(reverse("music:mainpage"))


class LoginGuestView(View):
    def get(self, *args, **kwargs):
        if (
            not self.request.user.is_authenticated
            and not self.request.session.get("username")
        ):
            context = {
                "title": "Вход Гостя",
                "form": GuestLoginForm,
            }
            return render(
                self.request, "person/guest_login.html", context=context
            )

        error(self.request, "Вы аутентифицированы")
        return redirect(reverse("music:mainpage"))

    def post(self, *args, **kwargs):
        if (
            not self.request.user.is_authenticated
            and not self.request.session.get("username")
        ):
            guest = GuestLoginForm(self.request.POST)
            if guest.is_valid():
                self.request.session["username"] = self.request.POST.get(
                    "username"
                )
                success(self.request, "Вы успешно зашли как гость")
                return redirect(reverse("music:mainpage"))

            error(self.request, "Введите корректные данные")
            return redirect(reverse("person:login"))

        error(self.request, "Вы аутентифицированы")
        return redirect(reverse("music:mainpage"))


class LogoutView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated or self.request.session.get(
            "username"
        ):
            return self.post()
        error(self.request, "Вы не аутентифицированы")
        return redirect(reverse("person:login"))

    def post(self, *args, **kwargs):
        if self.request.session.get("username"):
            del self.request.session["username"]
            return redirect(reverse("person:login"))

        if self.request.user.is_authenticated:
            logout(self.request)
            success(self.request, "Вы вышли из аккаунта")
            return redirect(reverse("person:login"))

        error(self.request, "Вы не аутентифицированы")
        return redirect(reverse("music:mainpage"))
