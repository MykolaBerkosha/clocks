
from django.contrib import admin

from apps.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = [
        'id', 'first_name', 'last_name', 'mobile', 'created', 'products_tag',
        'delivery_method', 'delivery_district_address', 'delivery_region_address',
        'post_office'
    ]

    def products_tag(self, obj):
        return ', '.join(map(str, obj.items.all()))
