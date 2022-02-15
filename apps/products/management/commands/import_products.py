
import json

from django.core.management.base import BaseCommand

from apps.categories.models import Category
from apps.products.models import Product


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):

        with open(options['file']) as f:

            data = json.load(f)

            categories = {c['id']: c for c in data['categories']}
            stocks = {s['id']: s['stock'] for s in data['stocks']}
            price_types = {t['id']: t['name'] for t in data['types_of_price']}
            prices = {
                '{}/{}'.format(p['product'], p['price_type']): p['price']
                for p in data['prices']
            }

            product_items = self._load_products(
                data['products'],
                categories,
                stocks,
                price_types,
                prices)

            category = Category.objects.first()
            products = []

            for item in product_items:

                products.append(
                    Product(
                        category=category,
                        name=item['description'],
                        price=(
                            item['prices']
                            ['7d527301-6629-11ec-ab69-7085c2afcfa2']
                            ['price']
                        ),
                        tags=item['index']
                    )
                )

            Product.objects.bulk_create(products)

            print('Success')

    def _load_products(
            self,
            data,
            categories,
            stocks,
            price_types,
            prices):

        result = []

        for product in data:

            product_id = product['id']

            try:
                result.append({
                    'index': product['index'],
                    'description': product['description'],
                    'category': categories[product['category']],
                    'stock': stocks.get(product_id) or 0,
                    'prices': {
                        price_type_id: {
                            'price': prices.get(
                                '{}/{}'.format(product_id, price_type_id)
                            ) or 0,
                            'name': price_type_name
                        }
                        for price_type_id, price_type_name in
                        price_types.items()
                    }
                })
            except KeyError:
                pass

        return result
