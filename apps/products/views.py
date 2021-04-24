
from django.shortcuts import render, get_object_or_404

from apps.categories.models import Category



def get_products(request, category_slug, category_id):

    category = get_object_or_404(Category, id=category_id)

    products = category.products.all()

    return render(request, 'products/list.html', {
        'category': category,
        'products': products
    })
