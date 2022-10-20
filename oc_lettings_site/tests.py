import pytest
from django.test import TestCase
from django.urls import reverse, resolve
from http import HTTPStatus
from django.http import HttpRequest


pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestWebSiteUrls(TestCase):
    pytestmark = pytest.mark.django_db

    def test_index_url(self):
        url = reverse('oc-lettings-site:index')
        resolver = resolve(url)
        request = HttpRequest()
        response = resolver.func(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn(b'<title>Holiday Homes</title>', response.content)

    def test_dummy(self):
        assert 1
