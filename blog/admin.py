from blog.models import Blog

from django.contrib import admin


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "created_at",
        "updated_at",
        "is_published",
        "views_count",

    ]
    list_filter = (
        "id",
        "created_at",
        "is_published",
                   )
    search_fields = (
        "id",
        "title",
    )


