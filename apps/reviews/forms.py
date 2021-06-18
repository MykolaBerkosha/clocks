
from django import forms

from ckeditor.widgets import CKEditorWidget

from apps.reviews.models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('name', 'text', 'rating', )
        widgets = {
            'text': CKEditorWidget
        }
