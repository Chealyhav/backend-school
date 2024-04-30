
from django.contrib import admin


from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from urllib.parse import urljoin

from django.core.files.storage import FileSystemStorage

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('collection/', include('collection.urls')),
    path('collection/', include('admin_api.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
