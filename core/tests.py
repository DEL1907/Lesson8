from django.test import TestCase
from django.test import Client
from core import models


class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.recipe = models.Recipes.objects.create(
            title='Торт',
            description='Описание',

        )

    def test_index(self):
        response = self.client.get('/index_class/')
        self.assertEqual(response.status_code, 200)

    def test_detail_recipe(self):
        response = self.client.get(f'/recipe/{self.recipe.id}/')
        self.assertEqual(response.status_code, 200)

    def test_redirect(self):
        response = self.client.get('/redirect/')
        self.assertEqual(response.status_code, 302)
