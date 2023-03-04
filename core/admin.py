from django.contrib import admin
from .models import SisUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    search_fields = ("email",)
    list_filter = ("is_active", "is_staff", "is_superuser", "user_type")
    list_editable = ("is_active", "is_staff", "is_superuser", "user_type")
    ordering = ("email", "first_name", "last_name")
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "user_type",
    )
    fieldsets = (
        (
            "Details",
            {"fields": ("email", "first_name", "last_name", "user_type", "password")},
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            "Details",
            {
                "classes": ("wide",),
                "fields": ("email", "user_type", "password1", "password2"),
            },
        ),
        (
            "Permissions",
            {"classes": ("wide",), "fields": ("is_superuser", "is_staff", "is_active")},
        ),
    )


admin.site.register(SisUser, UserAdminConfig)
