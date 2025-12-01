from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path('catalog/', include('catalog.urls', namespace='catalog')),
                  path('blog/', include('blog.urls', namespace='blog')),
                  path("tinymce/", include("tinymce.urls")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
