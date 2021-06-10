
from django.urls import path

from apps.reviews import views


app_name = 'reviews'


urlpatterns = [

    path('add/', views.add_review, name='add'),

    path('list/', views.ReviewListView.as_view(), name='list')

]
