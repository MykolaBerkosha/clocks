
from django.contrib import admin

from apps.products.models import Product
from watermarks.models import WatermarkImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'category', 'name', 'price', 'availability','slug', 'description', 'new_price',
                    'type_clocks', 'material', 'water_resistance', 'manufacturer',
                    'case_diameter', 'band_width', 'functions', 'coating',]
    list_filter = ['category']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # watermark = WatermarkImage.get('product')
        # watermark.process(obj.logo.path)
