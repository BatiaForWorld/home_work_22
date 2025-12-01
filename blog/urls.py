from django.urls import path
from blog.apps import BlogConfig
from blog.views import IndexListView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView, ContactsView, \
    BlogListView
from catalog.views import SignTemplateView

app_name = BlogConfig.name

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path("blog/contacts/", ContactsView.as_view(), name="contacts"),
    path("blog/sign/", SignTemplateView.as_view(), name="sign"),


]
