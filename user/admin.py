from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from user.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'is_admin', 'is_active')
    search_fields = ('email', 'username',)
    readonly_fields = ('id', 'create_at')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_per_page = 10


admin.site.register(User, UserAdmin)