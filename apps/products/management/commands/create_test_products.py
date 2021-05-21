
from django.core.management.base import BaseCommand

from apps.products.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        for i in range(1, 50):
            Product.objects.create(
                category_id=1,
                price=i * 12,
                name='Product {}'.format(i)
            )