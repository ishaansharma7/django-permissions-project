from django.contrib import admin
from accounts.models import CustomUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'username', 'full_name',)
    list_filter = ('email', 'username', 'full_name', 'is_active', 'is_staff')
    list_display = ('email', 'username',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'full_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Personal', {'fields': ('contact_number',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'full_name', 'contact_number', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

admin.site.register(CustomUser, UserAdminConfig)