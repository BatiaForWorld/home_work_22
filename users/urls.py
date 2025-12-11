from django.urls import path
from django.views.generic import TemplateView
from users.apps import UsersConfig
from users.views import RegisterView, CustomLogoutView, UserLoginView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", RegisterView.as_view(), name='register'),
    path("login/", UserLoginView.as_view(template_name='users/login.html'), name='login'),
    path("logout/", CustomLogoutView.as_view(next_page='users:logged_out'), name='logout'),
    path("logged_out/", TemplateView.as_view(template_name='users/logged_out.html'), name='logged_out'),

]
