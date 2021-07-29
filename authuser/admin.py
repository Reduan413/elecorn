from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdmin(UserAdmin):
    list_display = ('first_name','last_name','username', 'is_staff', 'is_admin', 'is_superuser', 'is_active',)
    list_filter = ('first_name','last_name', 'username', 'is_staff', 'is_admin', 'is_superuser', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_admin', 'is_superuser', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','username', 'email', 'contact_no', 'password', 'is_staff', 'is_admin', 'is_superuser', 'is_active',)}
        ),
    )
    search_fields = ('first_name','last_name','username', 'email', 'contact_no', )
    ordering = ('first_name','last_name','username', 'email', 'contact_no', )


admin.site.register(User, UserAdmin)