from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from parameterized import parameterized
from http import HTTPStatus


class MusicMainPageTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tmp1", password="ttookkyy1"
        )
        self.client.login(username="tmp1", password="ttookkyy1")

    def test_mainpage_get(self):
        response = self.client.get(reverse("music:mainpage"))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @parameterized.expand([(reverse("music:mainpage"), "content")])
    def test_mainpage_context(self, url, key):
        response = self.client.get(url)
        self.assertIn(key, response.context)
