from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Organizer

# class UserAdmin(BaseUserAdmin):
#     """Customizes the admin interface for the custom User model.
#     (i.e. list_filter adds a filter for is_admin to the interface, etc.)"""
    
#     list_display = ('name', 'participant_type', 'department', 'birthdate', 'is_admin')
#     list_filter = ('is_admin',)
    
#     fieldsets = (
#         (None, {'fields': ('name', 'password')}),
#         ('Personal info', {'fields': ('participant_type', 'department', 'birthdate')}),
#         ('Permissions', {'fields': ('is_admin', 'is_active', 'is_staff', 'is_superuser')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('name', 'participant_type', 'department', 'birthdate', 'password1', 'password2'),
#         }),
#     )
#     search_fields = ('name',)
#     ordering = ('name',)
#     filter_horizontal = ()

class OrganizerInline(admin.StackedInline):
    model = Organizer
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [OrganizerInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)