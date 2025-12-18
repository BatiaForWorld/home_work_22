from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = "Создание группы модераторов продуктов"

    def handle(self, *args, **options):
        content_type = ContentType.objects.get_for_model(Product)

        permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=[
                'can_unpublish_product',
                'delete_product',
            ]
        )

        group, created = Group.objects.get_or_create(
            name='Модератор продуктов'
        )

        group.permissions.set(permissions)
        group.save()

        if created:
            self.stdout.write(
                self.style.SUCCESS('Группа "Модератор продуктов" создана')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Группа "Модератор продуктов" уже существует, права обновлены')
            )
