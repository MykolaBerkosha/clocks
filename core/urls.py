
from django.contrib import admin
from django.urls import path, include

from apps.site.views import home


urlpatterns = [

    path('admin/', admin.site.urls),

    path('products/', include('apps.products.urls')),

    path('', home, name='home')

]
