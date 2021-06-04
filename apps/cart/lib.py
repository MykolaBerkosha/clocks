
from apps.products.models import Product


class Cart(object):

    def __init__(self, session):

        self._session = session
        self._data = set(session.get('cart') or [])

    def add_product(self, product_id):
        self._data.add(product_id)
        self._commit()

    def remove_product(self, product_id):
        self._data.remove(product_id)
        self._commit()

    def has_product(self, product_id):
        return str(product_id) in self._data

    def _commit(self):
        self._session['cart'] = list(self._data)

    def get_products(self):
        return Product.objects.filter(id__in=self._data)
