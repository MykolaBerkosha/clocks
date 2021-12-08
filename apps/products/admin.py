
from django.contrib import admin

from apps.products.models import Product
from watermarks.models import WatermarkImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'category', 'name', 'price', 'slug']
    list_filter = ['category', 'availability',]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        watermark = WatermarkImage.get('product')
        watermark.process(obj.logo.path)
