
from django.contrib import admin

from apps.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'category', 'name', 'price', 'slug']
    list_filter = ['category']
