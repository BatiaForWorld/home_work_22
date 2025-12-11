import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, TemplateView, DeleteView, UpdateView, CreateView, DetailView
from blog.models import Blog
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexListView(TemplateView):
    model = Blog
    template_name = 'blog/index.html'


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(is_published=True).order_by('-created_at')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.object.pk])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


class ContactsView(View):
    template_name = "blog/contacts.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


@csrf_exempt
def tinymce_image_upload(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        upload_dir = os.path.join(settings.MEDIA_ROOT, "tinymce_uploads")

        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(upload_dir, file.name)

        with open(file_path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        file_url = f"{settings.MEDIA_URL}tinymce_uploads/{file.name}"

        return JsonResponse({"location": file_url})

    return JsonResponse({"error": "Invalid request"}, status=400)
