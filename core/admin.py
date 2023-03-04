from django.contrib import admin
from .models import SisUser
from django.contrib.auth.admin import UserAdmin

class UserAdminConfig(UserAdmin):
    search_fields = ('email',)
    list_filter = ('email', 'is_active', 'is_staff', 'is_superuser', 'user_type')
    list_editable = ('is_active', 'is_staff', 'is_superuser', 'user_type')
    ordering = ('email',)
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser' ,'user_type')
    fieldsets = (
        (None, {'fields': ('email', 'user_type', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_type', 'password1', 'password2')
        }),
    )

admin.site.register(SisUser, UserAdminConfig)