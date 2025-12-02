from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, IndexListView, \
    CategoryListView, SignTemplateView, ProductUpdateView, ProductDeleteView, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path('catalog/product_list/', ProductListView.as_view(), name='product_list'),
    path('catalog/create/', ProductCreateView.as_view(), name='product_create'),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path("catalog/category/", CategoryListView.as_view(), name="category"),
    path("catalog/contacts/", ContactsView.as_view(), name="contacts"),
    path("catalog/sign/", SignTemplateView.as_view(), name="sign"),

]
