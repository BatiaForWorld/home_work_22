from django.contrib.auth import login
from django.contrib.auth.views import LogoutView, LoginView
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, LoginForm


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Проверьте правильность заполнения формы.")
        return super().form_invalid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались!'
        from_email = EMAIL_HOST_USER
        send_mail(subject, message, from_email, [user_email])


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = LoginForm


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('users/logged_out.html')
