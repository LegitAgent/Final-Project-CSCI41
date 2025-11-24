from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User 

class UserAdmin(BaseUserAdmin):
    list_display = ('name', 'participant_type', 'department', 'birthdate', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('name', 'password')}),
        ('Personal info', {'fields': ('participant_type', 'department', 'birthdate')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'participant_type', 'department', 'birthdate', 'password1', 'password2'),
        }),
    )
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)