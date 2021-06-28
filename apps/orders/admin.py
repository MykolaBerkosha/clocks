
from django.contrib import admin

from apps.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = [
        'id', 'first_name', 'last_name', 'mobile', 'created', 'products_tag'
    ]

    def products_tag(self, obj):
        return ', '.join(map(str, obj.items.all()))
