from django.core.mail import send_mail
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView, View
from django.contrib import messages
from catalog.forms import ProductForm
from catalog.models import Category, Product
from django.contrib.auth.mixins import LoginRequiredMixin
from config.settings import EMAIL_HOST_USER


class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category.html'


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


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


def sign(request):
    return render(request, "")
