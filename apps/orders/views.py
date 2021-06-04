
from django.shortcuts import render, redirect

from apps.orders import forms
from apps.cart.lib import Cart


def checkout(request):

    form = forms.CheckoutForm(request.POST or None)

    cart = Cart(request.session)

    if request.method == 'POST' and form.is_valid():
        form.save()
        cart.clear()
        return redirect('home')

    return render(request, 'orders/checkout.html', {
        'form': form
    })
