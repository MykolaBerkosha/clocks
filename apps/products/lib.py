
import io, csv

from apps.categories.models import Category
from apps.products.models import Product


def import_products(file):

    io_string = io.StringIO(file.read().decode('utf-8'))

    items = csv.DictReader(io_string)

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

def export_products_csv(response):

    writer = csv.writer(response)

    writer.writerow([
        'Category name',
        'Product name',
        'Price',
        'Tags'
    ])

    for product in Product.objects.all().select_related('category'):

        writer.writerow([
            product.category.name,
            product.name,
            product.price,
            product.tags
        ])
