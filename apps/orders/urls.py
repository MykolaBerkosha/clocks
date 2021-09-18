
from django.urls import path

from apps.orders import views


app_name = 'orders'


urlpatterns = [

    path('checkout/', views.checkout, name='checkout'),

    path('quick-checkout/', views.quick_checkout,
         name='quick-checkout'),

]
