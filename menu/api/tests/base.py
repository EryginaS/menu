from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase


class BaseTest(APITestCase):
    """ Base class for Tests """
    client = APIClient()

    def setUp(self):
        self._user = User.objects.create_user('John', password='user1')

    def user_auth(self):
        self.client.login(username=self._user.username, password='user1')
