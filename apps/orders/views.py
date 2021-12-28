
from django.conf import settings
from django.shortcuts import render, redirect
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.core.mail import mail_managers
from django.contrib import messages
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

from apps.orders import forms
from apps.orders.models import Order
from apps.cart.lib import Cart


def checkout(request):

    form = forms.CheckoutForm(request.POST or None)

    cart = Cart(request.session)

    if request.method == 'POST' and form.is_valid():

        order = form.save()

        for product in cart.get_products():
            order.items.create(product=product, price=product.price)

        cart.clear()

        mail_managers(
            subject='New order #{}'.format(order.id),
            message='',
            fail_silently=not settings.DEBUG,
            html_message=render_to_string('orders/mail.html', {'order': order})
        )

        messages.success(request, 'Order added')

        return redirect('home')

    return render(request, 'orders/checkout.html', {
        'form': form
    })


@require_POST
def quick_checkout(request):

    form = forms.QuickCheckoutForm(request.POST)

    if form.is_valid():

        order = Order.objects.create(
            mobile=form.cleaned_data['mobile']
        )

        product = form.cleaned_data['product']

        order.items.create(product=product, price=product.price)

        mail_managers(
            subject='New order #{}'.format(order.id),
            message='',
            fail_silently=not settings.DEBUG,
            html_message=render_to_string('orders/mail.html', {'order': order}),
        )

        return JsonResponse({
            'message': 'Order added'
        })

    return HttpResponseBadRequest('Something wrong')
