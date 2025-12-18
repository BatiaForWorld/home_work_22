from catalog.models import Product

def header_products(request):
    user = request.user

    if not user.is_authenticated:
        products = Product.objects.filter(status=True)
    elif user.has_perm('catalog.can_unpublish_product'):
        products = Product.objects.all()
    else:
        products = Product.objects.filter(status=True) | Product.objects.filter(owner=user)

    return {'header_products': products.distinct()}
