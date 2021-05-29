
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from pagination import paginate

from apps.cart.lib import Cart
from apps.categories.models import Category
from apps.products.models import Product
from apps.products.forms import ProductSearchForm


def get_search(request):

    form = ProductSearchForm(request.GET)

    if form.is_valid():

        query = form.cleaned_data['query']
        category = form.cleaned_data['category']

        trimmed_query = query.strip()

        products = Product.objects.all()

        if trimmed_query:
            products = products.filter(
                Q(name__icontains=trimmed_query) |
                Q(tags__icontains=trimmed_query)
            )

        if category:
            products = products.filter(category=category)
    else:
        products = []

    return render(request, 'products/search.html', {
        'products': products,
        'form': form
    })


def get_products(request, category_slug, category_id):

    category = get_object_or_404(Category, id=category_id)

    products = category.products.all().order_by('-id')

    return render(request, 'products/list.html', {
        'category': category,
        'page_obj': paginate(request, products)
    })


def get_product(request, category_slug, category_id, slug, id):

    product = get_object_or_404(Product, category_id=category_id, id=id)

    cart = Cart(request.session)

    return render(request, 'products/detail.html', {
        'product': product,
        'is_added_to_cart': cart.has_product(id)
    })
