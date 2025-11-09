from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts


name_app = CatalogConfig

urlpatterns = [
    path('',home, name='home'),
    path('contacts/', contacts, name='contacts')
]
