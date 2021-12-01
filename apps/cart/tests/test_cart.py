
from unittest.mock import Mock, patch

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

    def test_cart(self):

        product = Mock()
        product.get_name = Mock(return_value='Test')

        with patch.object(Cart, 'add_product', return_value=product) as mock_method:
            self.client.post('/cart/add', {
                'product': self.product_1.pk,
                'next': '/'
            })

        mock_method.assert_called_once_with(str(self.product_1.pk))
        product.get_name.assert_called_once_with(123)

    # def test_send_mail(self):
    #     mock_mail_manager = Mock()
    #     with patch.object('mail_managers', return_value=order) as mock_method:
    #         self.client.post('/cart/add', {
    #             'product': self.product_1.pk,
    #             'next': '/'
    #         })
    #
    #     mock_method.assert_called_once_with(str(self.product_1.pk))
    #     product.get_name.assert_called_once_with(123)

    # def test_send_mail(self):
    #
    #     order = Mock()
    #     order.get_name = Mock(return_value='Test')
    #
    #     with patch.object(mail_managers, 'add_product', return_value=order) as mock_method:
    #         self.client.post('/cart/add', {
    #             'product': self.product_1.pk,
    #             'next': '/'
    #         })
    #
    #     mock_method.assert_called_once_with(str(self.product_1.pk))
    #     order.get_name.assert_called_once_with(123)
    # class RegisterTestCase(TestCase):
        # def test_mail_is_sent(self):
        #
        #     with patch('django.core.mail.send_mail') as mocked_send_mail:
        #         from register.models import Subscriber  #This test still fails if I have the import outside the mock context
        #         subscriber = Subscriber.objects.create(
        #             email = 'te...@example.com',
        #         )
        #         self.assertTrue(mocked_send_mail.called)
        #         self.assertFalse(subscriber.active)
        #         self.assertEqual(mocked_send_mail.call_args['recipient_list'], 'te...@example.com')