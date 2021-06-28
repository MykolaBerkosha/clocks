
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import mail_managers
from django.contrib import messages
from django.template.loader import render_to_string

from apps.orders import forms
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
