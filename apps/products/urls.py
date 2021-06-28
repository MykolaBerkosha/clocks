
from django.urls import path

from apps.products import views


app_name = 'products'


urlpatterns = [

    path('search/', views.get_search, name='search'),

    path('<str:category_slug>_<int:category_id>/', views.get_products,
         name='list'),

    path('<str:category_slug>_<int:category_id>/<str:slug>_<int:id>/',
         views.get_product, name='detail'),

    path('import/', views.import_products, name='import'),

    path('export/', views.export_products, name='export')

]
