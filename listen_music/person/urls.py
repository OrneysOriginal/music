from django.urls import path
from person import views


app_name = "person"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path(
        "registration", views.RegistrationView.as_view(), name="registration"
    ),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("guest/", views.LoginGuestView.as_view(), name="guest"),
]
