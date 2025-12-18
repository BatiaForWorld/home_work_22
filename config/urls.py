from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from catalog.views import permission_denied_view

handler403 = permission_denied_view

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path('', include('catalog.urls', namespace='catalog')),
                  path('blog/', include('blog.urls', namespace='blog')),
                  path('users/', include('users.urls', namespace='users')),
                  path("tinymce/", include("tinymce.urls")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
