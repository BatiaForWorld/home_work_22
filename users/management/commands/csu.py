from django.core.management import BaseCommand
from users.models import User
from config.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(email='admin@mail.ru')
        user.set_password('admin')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()