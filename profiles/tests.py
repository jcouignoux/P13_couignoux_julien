import pytest
from django.test import TestCase
from django.test import Client
from django.urls import reverse, resolve
from http import HTTPStatus
from django.http import HttpRequest

from django.contrib.auth.models import User
from profiles.models import Profile

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestProfilesUrls(TestCase):
    pytestmark = pytest.mark.django_db

    def test_profiles_index_url(self):
        url = reverse('profiles:profiles_index')
        resolver = resolve(url)
        request = HttpRequest()
        response = resolver.func(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn(b'<title>Profiles</title>', response.content)

    def test_letting_url(self):
        client = Client()
        user = User.objects.create(username='username',)
        profile = Profile.objects.create(user=user, favorite_city='Sannois')
        url = reverse('profiles:profile', kwargs={'username': user.username})
        response = client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn(f'<title>' + str(user.username) + f'</title>', response.content.decode())
