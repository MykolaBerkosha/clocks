
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView

from apps.reviews.models import Review
from apps.reviews.forms import ReviewForm


def add_review(request):

    form = ReviewForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, _('Review added'))
        return redirect('home')

    return render(request, 'reviews/add.html', {
        'form': form
    })


class ReviewListView(ListView):

    model = Review

