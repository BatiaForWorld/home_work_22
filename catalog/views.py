from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Category, Product


def index(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "index.html", context)


def category(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "category.html", context)


def product(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product.html", context)


def product_detail(request, pk):
    info = get_object_or_404(Product, pk=pk)
    context = {"info": info}
    return render(request, "product_detail.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html")


def sign(request):
    return render(request, "sign.html")
