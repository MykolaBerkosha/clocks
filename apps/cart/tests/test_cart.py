
from django.test import TestCase

from apps.categories.models import Category
from apps.products.models import Product
from apps.cart.lib import Cart


class Case(TestCase):

    def setUp(self):

        self.category = Category.objects.create(
            name='Category'
        )

        self.product_1 = Product.objects.create(
            category=self.category,
            name='Test 1',
            price=100
        )

        self.product_2 = Product.objects.create(
            category=self.category,
            name='Test 2',
            price=200
        )


    def test_add_to_cart(self):

        url = '/cart/add'
        dst_url = '/'

        session = self.client.session

        self.assertNotIn('cart', session)

        response = self.client.post(url, {
            'product': self.product_1.pk,
            'next': dst_url
        })

        self.assertRedirects(response, dst_url)

        session = self.client.session

        self.assertIn('cart', session)

        product_ids = session['cart']

        self.assertEqual(len(product_ids), 1)

        self.assertEqual(product_ids[0], str(self.product_1.pk))

    def test_remove_to_cart(self):

        session = self.client.session
        session['cart'] = map(str, [self.product_1.pk, self.product_2.pk])

        cart = Cart(session)

        self.assertEqual(cart.count, 2)

        cart.remove_product(str(self.product_1.pk))

        self.assertEqual(cart.count, 1)

        self.assertEqual(cart.get_products()[0].pk, self.product_2.pk)

    def test_clear_to_cart(self):

        session = self.client.session
        session['cart'] = map(str, [self.product_1.pk, self.product_2.pk])

        cart = Cart(session)

        self.assertEqual(cart.count, 2)

        cart.clear()

        self.assertEqual(cart.count, 0)

    def test_cart_total(self):

        session = self.client.session
        session['cart'] = map(str, [self.product_1.pk, self.product_2.pk])

        cart = Cart(session)

        self.assertEqual(cart.count, 2)
        self.assertEqual(cart.total, 300)
