from django.core.cache import cache
from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_by_category(category_id):
    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id, status=True)

    cache_key = f'products_category_{category_id}'
    products = cache.get(cache_key)

    if products is None:
        products = Product.objects.filter(category_id=category_id, status=True)
        cache.set(cache_key, products, 60 * 5)

    return products
