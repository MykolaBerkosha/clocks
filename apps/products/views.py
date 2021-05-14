
from django.shortcuts import render, get_object_or_404

from apps.categories.models import Category
from apps.products.models import Product


def get_search(request):

    query = request.GET.get('query')

    if query:
        products = Product.objects.filter(name__icontains=query.strip())
    else:
        products = []

    return render(request, 'products/search.html', {
        'products': products
    })


def get_products(request, category_slug, category_id):

    category = get_object_or_404(Category, id=category_id)

    products = category.products.all()

    return render(request, 'products/list.html', {
        'category': category,
        'products': products
    })


def get_product(request, category_slug, category_id, slug, id):

    product = get_object_or_404(Product, category_id=category_id, id=id)

    return render(request, 'products/detail.html', {
        'product': product
    })
