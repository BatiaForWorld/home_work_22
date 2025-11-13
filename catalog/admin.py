from catalog.models import Category, Product

from django.contrib import admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "purchase_price",
        "category",
    ]
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )
