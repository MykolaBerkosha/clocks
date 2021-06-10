
from django import forms

from apps.reviews.models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('name', 'text', 'rating', )
