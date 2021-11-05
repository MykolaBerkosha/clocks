
from django.test import TestCase

from apps.categories.models import Category
from apps.products.models import Product
from apps.orders.models import Order


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


    def test_checkout(self):

        session = self.client.session
        session.update({
            'cart': [self.product_1.pk, self.product_2.pk]
        })
        session.save()

        url = '/orders/checkout/'

        response = self.client.post(url, {
            'first_name': 'Микола',
            'last_name': 'Беркоша',
            'mobile': '0674756206'
        })

        self.assertRedirects(response, '/')

        orders = list(Order.objects.all())

        self.assertEqual(len(orders), 1)

        order = orders[0]

        self.assertEqual(order.first_name, 'Микола')
        self.assertEqual(order.last_name, 'Беркоша')
        self.assertEqual(order.mobile, '0674756206')

        items = list(order.items.all())

        self.assertEqual(len(items), 2)

        self.assertEqual(items[0].product_id, self.product_1.pk)
        self.assertEqual(items[0].price, self.product_1.price)

        self.assertEqual(items[1].product_id, self.product_2.pk)
        self.assertEqual(items[1].price, self.product_2.price)
