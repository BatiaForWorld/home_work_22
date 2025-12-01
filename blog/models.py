import os
from PIL import Image
from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    content = models.TextField(
        verbose_name="Содержимое"
    )
    preview = models.ImageField(
        upload_to="blog/blog_previews",
        verbose_name="Превью изображения",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
    )
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров"
    )

    class Meta:
        verbose_name = "Моя статья"
        verbose_name_plural = "Мои статьи"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.preview:
            self.create_responsive_images()

    def create_responsive_images(self):
        img_path = self.preview.path
        filename, ext = os.path.splitext(os.path.basename(img_path))
        mobile_path = f"mobile/{filename}_300.webp"
        desktop_path = f"desktop/{filename}_900.webp"
        img = Image.open(img_path)
        img = img.convert("RGB")
        img_mobile = img.copy()
        img_mobile.thumbnail((300, 300))
        img_mobile.save(os.path.join(os.path.dirname(img_path), mobile_path), "WEBP", quality=85)
        img_desktop = img.copy()
        img_desktop.thumbnail((900, 900))
        img_desktop.save(os.path.join(os.path.dirname(img_path), desktop_path), "WEBP", quality=85)

        self.mobile_image = mobile_path
        self.desktop_image = desktop_path

        super().save()
