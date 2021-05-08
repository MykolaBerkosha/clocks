
from django.urls import path

from apps.products import views


app_name = 'products'


urlpatterns = [

    path('<str:category_slug>_<int:category_id>/', views.get_products,
         name='list'),

    path('<str:category_slug>_<int:category_id>/<str:slug>_<int:id>/',
         views.get_product, name='detail'),

]
