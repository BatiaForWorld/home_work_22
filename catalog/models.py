from django.db import models
from users.models import User
from django.db.models import ForeignKey


# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Введите описание товара",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = [
            "name",
        ]


class Product(models.Model):
    STATUS_CHOICES = (
        (False, 'Черновик'),
        (True, 'Опубликован'),
    )

    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Наименование",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
    )
    image = models.ImageField(
        upload_to='catalog/images',
        blank=True, null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Категория",
    )
    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
    )
    views_counter = models.PositiveIntegerField(
        default=0,
        verbose_name='Счётчик просмотров',
        help_text='Укажите количество просмотров',
    )

    status = models.BooleanField(
        choices=STATUS_CHOICES,
        default=False,
        verbose_name='Статус публикации'
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Владелец'
    )

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
        ]

