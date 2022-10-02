import pytest
from django.test import TestCase
from django.test import Client
from django.urls import reverse, resolve
from http import HTTPStatus
from django.http import HttpRequest

from lettings.models import Letting, Address

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestLettingsUrls(TestCase):
    pytestmark = pytest.mark.django_db

    def test_lettings_index_url(self):
        url = reverse('lettings:lettings_index')
        resolver = resolve(url)
        request = HttpRequest()
        response = resolver.func(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn(b'<title>Lettings</title>', response.content)

    def test_letting_url(self):
        client = Client()
        address = Address.objects.create(number=21,
                                         street="JumpStreet",
                                         city="Los Angeles",
                                         state='60',
                                         zip_code="95110",
                                         country_iso_code="FRA")
        letting = Letting.objects.create(title="Letting 1", address=address)
        url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
        response = client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn(f'<title>' + str(letting.title) + f'</title>', response.content.decode())
