
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from apps.site.views import home


urlpatterns = [

    path('admin/', admin.site.urls),

    path('products/', include('apps.products.urls')),

    path('cart/', include('apps.cart.urls')),

    path('orders/', include('apps.orders.urls')),

    path('reviews/', include('apps.reviews.urls')),

    path('', home, name='home'),

    path('account/', include('accounts.urls'))

] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
