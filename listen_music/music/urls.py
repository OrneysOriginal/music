from django.urls import path
from music import views


app_name = "music"

urlpatterns = [
    path("add_music/", views.AddMusicView.as_view(), name="add_music"),
    path("search/", views.SearchPageView.as_view(), name="search"),
    path("", views.MainPageMusic.as_view(), name="mainpage"),
]
