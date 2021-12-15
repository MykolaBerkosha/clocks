
from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView

from apps.reviews.models import Review
from apps.reviews.forms import ReviewForm


def add_review(request):

    form = ReviewForm(request.POST or None)

    status_code = 200

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, _('Review added'))
            return JsonResponse({
                'message': _('Review added')
            })
        else:
            status_code = 403

    return render(request, 'reviews/add.html', {
        'form': form,
        'status_code': status_code
    }, status=status_code)


class ReviewListView(ListView):

    model = Review

