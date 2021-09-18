
from django import forms

from apps.orders.models import Order


class CheckoutForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = Order
        fields = (
            'first_name',
            'last_name',
            'mobile',
        )
