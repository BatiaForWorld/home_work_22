from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView, View
from django.contrib import messages
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Category, Product
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from config.settings import EMAIL_HOST_USER


class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category.html'


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Product.objects.filter(status=True)

        if user.has_perm('catalog.can_unpublish_product'):
            return Product.objects.all()

        return Product.objects.filter(status=True) | Product.objects.filter(owner=user)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        user = self.request.user

        if not obj.status:
            if not user.is_authenticated:
                raise PermissionDenied
            if obj.owner != user and not user.has_perm('catalog.can_unpublish_product'):
                raise PermissionDenied

        obj.views_counter += 1
        obj.save()
        return obj



class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        product = self.get_object()
        user = self.request.user

        if user == product.owner:
            return ProductForm
        elif user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        else:
            raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        user = request.user

        if user == product.owner or user.has_perm('catalog.can_unpublish_product'):
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied



class ContactsView(View):
    template_name = "catalog/contacts.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message_text = request.POST.get("message")

        if not name or not message_text:
            messages.error(request, "Имя и сообщение обязательны")
            return render(request, self.template_name, request.POST)

        subject = f"Сообщение от {name}"
        message = f"Имя: {name}\nТелефон: {phone}\nСообщение:\n{message_text}"
        from_email = EMAIL_HOST_USER
        recipient_list = [EMAIL_HOST_USER]

        try:
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, f"Спасибо, {name}! Ваше сообщение получено.")
        except Exception as e:
            messages.error(request, f"Ошибка при отправке: {e}")

        return redirect(request.path)


class SignTemplateView(TemplateView):
    template_name = "catalog/sign.html"


def permission_denied_view(request, exception=None):
    return render(request, "403.html", status=403)