from http import HTTPStatus

from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.test import TestCase
from parameterized import parameterized

from person.forms import UserRegistrationForm, UserLoginForm, GuestLoginForm

from core.tests import ModifySessionMixin


class RegistrationTest(TestCase, ModifySessionMixin):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tmp1", password="ttookkyy1"
        )
        self.create_session()

    @parameterized.expand([(reverse("person:registration"), HTTPStatus.OK)])
    def test_unlogin_user_Get(self, url, status_code):
        response = self.client.get(url)
        self.assertEqual(response.status_code, status_code)

    @parameterized.expand([(reverse("person:registration"), HTTPStatus.FOUND)])
    def test_login_user_get(self, url, status_code):
        self.client.login(username="tmp1", password="ttookkyy1")
        response = self.client.get(url, follow=False)
        self.assertEqual(response.status_code, status_code)

    @parameterized.expand(
        [
            ("tmp2", "ttookkyy1", "youremail@yandex.com", True),
            ("tmp3", "ttoo", "youremail@yandex.com", False),
            ("tmp4", "ttookkyy1", "youremailyandex.com", False),
            ("tmp5", "ttookkyy1", "youremail@yandex", False),
            ("tmp6", "ttookkyy1", "@yandex.com", False),
        ]
    )
    def test_UserRegistrationForm(self, username, password, email, is_valid):
        form_data = {
            "username": username,
            "password": password,
            "email": email,
        }
        form = UserRegistrationForm(data=form_data)
        if is_valid:
            self.assertTrue(form.is_valid())
        else:
            self.assertFalse(form.is_valid())

    @parameterized.expand(
        [
            ("tmp2", "ttookkyy1", "youremail@yandex.com", HTTPStatus.OK),
        ]
    )
    def test_registration_view_post(
        self, username, password, email, status_code
    ):
        form_data = {
            "username": username,
            "password": password,
            "email": email,
        }
        response = self.client.post(
            reverse("person:registration"), data=form_data, follow=True
        )
        self.assertEqual(response.status_code, status_code)


class UserLoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tmp1", password="ttookkyy1"
        )
        self.client.logout()

    @parameterized.expand(
        [
            ("tmp1", "ttookkyy1", True),
            ("tmp2", "ttookkyy1", True),
            ("tmp1", "ttookkyy", True),
            ("tmp", "ttookkyy1", True),
            ("", "ttookkyy1", False),
            ("tmp1", "", False),
        ]
    )
    def test_UserLoginForm(self, username, password, is_valid):
        data_form = {
            "username": username,
            "password": password,
        }
        form = UserLoginForm(data=data_form)
        if is_valid:
            self.assertTrue(form.is_valid())
        else:
            self.assertFalse(form.is_valid())

    @parameterized.expand(
        [
            ("tmp1", "ttookkyy1", reverse("music:mainpage")),
            ("tmp2", "ttookkyy1", reverse("person:login")),
            ("tmp1", "ttookkyy", reverse("person:login")),
            ("tmp", "ttookkyy1", reverse("person:login")),
        ]
    )
    def test_login_view_post(self, username, password, rev):
        data_form = {
            "username": username,
            "password": password,
        }
        response = self.client.post(
            reverse("person:login"), data=data_form, follow=True
        )
        self.assertRedirects(response, rev)


class UserGuestLoginTest(TestCase):
    @parameterized.expand(
        [
            ("Anton", True),
            ("", False),
            ("@", False),
            (chr(2000), False),
        ]
    )
    def test_GuestLoginForm(self, username, is_valid):
        form_data = {
            "username": username,
        }
        form = GuestLoginForm(data=form_data)
        if is_valid:
            self.assertTrue(form.is_valid())
        else:
            self.assertFalse(form.is_valid())

    @parameterized.expand(
        [
            ("tmp1", reverse("music:mainpage")),
            ("@", reverse("person:guest")),
            (chr(2000), reverse("person:guest")),
            ("", reverse("person:guest")),
        ]
    )
    def test_session_user_guest_get(self, username, rev):
        form_data = {
            "username": username,
        }
        response = self.client.post(
            reverse("person:guest"), data=form_data, follow=True
        )
        self.assertRedirects(response, rev)
