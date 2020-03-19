from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from apps.views import index, brand, design, dev, ui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('brand/', brand),
    path('design/', design),
    path('dev/', dev),
    path('ui/', ui),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
