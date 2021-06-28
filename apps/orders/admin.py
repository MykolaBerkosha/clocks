
from django.contrib import admin

from apps.orders.models import Order


admin.site.register(
    Order,
    list_display=['id', 'first_name', 'last_name', 'mobile', 'created']
)
