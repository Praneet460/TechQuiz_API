from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name', 'first_name',)
    ordering = ('-register_date',)
    list_display = ('email', 'user_name', 'first_name', 
                        'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'user_name',)}),
        ('Personal', {'fields': ('first_name', 'last_name', 'register_date',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_staff', 'is_active',)
        }),
    )


admin.site.register(CustomUser, UserAdminConfig)