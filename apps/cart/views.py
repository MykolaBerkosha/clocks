
from django.shortcuts import redirect, get_object_or_404, render

from apps.products.models import Product

from apps.cart.lib import Cart


def index(request):
    return render(request, 'cart/index.html', {})


def add_to_cart(request):

    product_id = request.POST.get('product')

    get_object_or_404(Product, id=product_id)

    cart = Cart(request.session)

    cart.add_product(product_id)

    return redirect(request.POST.get('next'))


def remove_from_cart(request):

    product_id = request.POST.get('product')

    get_object_or_404(Product, id=product_id)

    cart = Cart(request.session)

    cart.remove_product(product_id)

    return redirect(request.POST.get('next'))
