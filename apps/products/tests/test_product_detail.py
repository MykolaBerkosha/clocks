
from bs4 import BeautifulSoup

from django.test import TestCase

from apps.categories.models import Category
from apps.products.models import Product


class Case(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Category'
        )

        self.product = Product.objects.create(
            category=self.category,
            name='Test',
            price=100
        )


    def test_page_contains_title(self):

        url = '/products/{}_{}/{}_{}/'.format(
            self.category.slug,
            self.category.id,
            self.product.slug,
            self.product.id)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')

        self.assertIn('Test', soup.title.text)

    def test_page_contains_product_name(self):

        url = '/products/{}_{}/{}_{}/'.format(
            self.category.slug,
            self.category.id,
            self.product.slug,
            self.product.id)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')

        tags = soup.find_all("h4")

        self.assertEqual(len(tags), 1)

        self.assertIn('Test', tags[0].text)
