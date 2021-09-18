
from django import forms

from apps.orders.models import Order

from apps.products.models import Product


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


class QuickCheckoutForm(forms.Form):

    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget=forms.HiddenInput)

    mobile = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your mobile'
        })
    )
