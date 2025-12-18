from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "email",
        "phone",
        "country",
    ]
    list_filter = ("country",
                   "email",)
    search_fields = (
        "email",
        "country",
    )
