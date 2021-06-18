
from django.db.models import Q
from django.contrib import admin
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from pagination import paginate

from apps.cart.lib import Cart
from apps.categories.models import Category
from apps.products import lib
from apps.products.models import Product
from apps.products.forms import ProductSearchForm, ProductImportForm


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


def import_products(request):

    form = ProductImportForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():

        try:
            lib.import_products(form.cleaned_data['file'])
        except Exception as e:
            form.add_error('file', e)
        else:
            messages.success(request, 'Import successful')

            return redirect(request.get_full_path())

    context = admin.site.each_context(request)
    context['form'] = form

    return render(request, 'products/import.html', context)
