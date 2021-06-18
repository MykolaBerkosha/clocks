
import io

from csv import DictReader

from apps.categories.models import Category
from apps.products.models import Product


def import_products(file):

    io_string = io.StringIO(file.read().decode('utf-8'))

    items = DictReader(io_string)

    categories = {c.name: c for c in Category.objects.all()}

    for item in items:

        try:
            category = categories[item['category']]
        except KeyError:
            raise Exception('Unknown category')

        Product.objects.create(
            category=category,
            name=item['title'],
            price=item['price'] or 0
        )
