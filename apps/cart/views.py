
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404, render
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_POST

from apps.products.models import Product

from apps.cart.lib import Cart


def index(request):
    return render(request, 'cart/index.html', {})


@require_POST
def add_to_cart(request):

    product_id = request.POST.get('product')

    get_object_or_404(Product, id=product_id)

    cart = Cart(request.session)

    cart.add_product(product_id)

    # product = cart.add_product(product_id)

    # print('Cool' + str(product.get_name(123)))

    messages.success(request, _('Product added to cart'))

    return redirect(request.POST.get('next'))


@require_POST
def remove_from_cart(request):

    product_id = request.POST.get('product')

    get_object_or_404(Product, id=product_id)

    cart = Cart(request.session)

    cart.remove_product(product_id)

    return redirect(request.POST.get('next'))


@require_POST
def clear_cart(request):

    cart = Cart(request.session)

    cart.clear()

    messages.warning(request, _('Cart was cleared'))

    return redirect(request.POST.get('next'))
