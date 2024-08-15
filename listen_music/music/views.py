from django.core.paginator import Paginator
from django.shortcuts import render, reverse, redirect
from django.views import View
from django.contrib.messages import error, success
from music.models import Music

from music.forms import MusicUploadForm

from core.views import DataMixin


class MainPageMusic(DataMixin):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated or self.request.session.get(
            "username"
        ):
            paginator = Paginator(
                Music.objects.get_queryset(), self.paginate_by
            )
            page = self.request.GET.get("page") or 1
            context = {
                "titile": "Главная страница",
                "content": paginator.page(page),
            }
            return render(self.request, "mainpage/main.html", context=context)

        error(self.request, "Вы не аутентифицированы")
        return redirect(reverse("person:login"))


class SearchPageView(DataMixin):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated or self.request.session.get(
            "username"
        ):
            content = self.request.GET.get("text") or self.request.GET.get(
                "search"
            )
            paginator = Paginator(
                Music.objects.filter(name__contains=content), self.paginate_by
            )
            page = self.request.GET.get("page") or 1
            context = {
                "title": "",
                "content": paginator.page(page),
                "text": content,
            }
            return render(
                self.request, "mainpage/search_page.html", context=context
            )

        error(self.request, "Вы не аутентифицированы")
        return redirect(reverse("person:login"))


class AddMusicView(View):
    def get(self, *args, **kwargs):
        if self.request.session.get("username"):
            error(self.request, "Чтобы добавлять музыку нужно войти в аккаунт")
            return redirect(reverse("music:mainpage"))

        if self.request.user.is_authenticated:
            context = {
                "title": "",
                "form": MusicUploadForm,
            }
            return render(
                self.request, "mainpage/add_music.html", context=context
            )

        error(self.request, "Вы не аутентифицированы")
        return redirect(reverse("person:login"))

    def post(self, *args, **kwargs):
        if self.request.session.get("username"):
            error(self.request, "Чтобы добавлять музыку нужно войти в аккаунт")
            return redirect(reverse("music:mainpage"))

        if self.request.user.is_authenticated:
            music_form = MusicUploadForm(self.request.POST, self.request.FILES)
            if music_form.is_valid():
                music_form.save()
                success(self.request, "Успешно добавлено")
                return redirect(reverse("music:add_music"))

            error(self.request, "Введите корректные данные")
            return redirect(reverse("person:login"))

        error(self.request, "Вы не аутентифицированы")
        return redirect(reverse("person:login"))
