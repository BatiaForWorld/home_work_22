from django.db import models


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
    image = models.ImageField(
        upload_to="catalog/images",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Введите название категории",
        null=True,
        blank=True,
        related_name="category",
    )
    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за покупку",
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
        verbose_name='Счётчик просмотров',
        help_text='Укажите количество просмотров',
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "name",
            "category",
        ]
