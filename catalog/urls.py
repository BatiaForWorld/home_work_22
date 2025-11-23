from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, product, contacts, category, sign, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("", index, name="index"),
    path("product/", product, name="product"),
    path("catalog/<int:pk>/", product_detail, name="product_detail"),
    path("contacts/", contacts, name="contacts"),
    path("category/", category, name="category"),
    path("sign/", sign, name="sign"),
]
