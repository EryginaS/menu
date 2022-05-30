import io
import os, shutil

from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from django.conf import settings
from PIL import Image

from .base import BaseTest
from position.models import Category, Allergen, Position

from unittest import mock


# Create your tests here.


class PositionTest(BaseTest):
    """ Test module for POST Position"""

    def setUp(self):
        super().setUp()

        self.category = Category.objects.create(name="Salat")
        self.allergen = Allergen.objects.create(name="cow's milk")

        self.valid_position = {
            "name": "crab salad",
            "price": 120,
            "proteins": 13,
            "fats": 13,
            "carbohydrates": 2,
            "calories": 400,
            "allergens": [self.allergen.pk],
            "category": self.category.pk,
            "image": self.generate_photo_file()

        }

    def tearDown(self):
        try:
            shutil.rmtree(settings.MEDIA_ROOT)
        except FileNotFoundError:
            pass

    @staticmethod
    def generate_photo_file():
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    # CREATE
    def test_create_valid_position_not_auth(self):
        response = self.client.post(
            reverse('create_position'),
            data=self.valid_position,
            format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_valid_position_auth(self):
        self.user_auth()
        response = self.client.post(
            reverse('create_position'),
            data=self.valid_position,
            format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_position(self):
        self.user_auth()
        response = self.client.post(
            reverse('create_position'),
            data=self.valid_position.pop('name'),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
