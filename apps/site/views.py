
from django.shortcuts import render

from apps.categories.models import Category


def home(request):
    return render(request, 'home.html', {
        'categories': Category.objects.all()
    })
