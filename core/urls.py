
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

from apps.site.views import home

from djrunner import setup_urlpatterns


urlpatterns = [

    path('admin/', admin.site.urls),

    path('products/', include('apps.products.urls')),

    path('cart/', include('apps.cart.urls')),

    path('orders/', include('apps.orders.urls')),

    path('reviews/', include('apps.reviews.urls')),

    path('accounts/', include('accounts.urls')),

    path('callback/', include('apps.callback.urls')),

    path('', home, name='home'),
]

setup_urlpatterns(urlpatterns, home_view=home)
