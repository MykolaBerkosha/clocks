
from django import forms

from apps.orders.models import Order


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'first_name',
            'last_name',
            'mobile',
        )
