
from django import forms

from apps.categories.models import Category


class ProductSearchForm(forms.Form):

    query = forms.CharField(required=False)

    category = forms.ModelChoiceField(
        required=False,
        queryset=Category.objects.all())


class ProductImportForm(forms.Form):

    file = forms.FileField()
