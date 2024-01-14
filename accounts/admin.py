from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Registered models here.

class CustomUserAdmin(UserAdmin):    # making password non editable
    list_display = ('email', 'first_name', 'last_name', 'username', 'role', 'is_active')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, CustomUserAdmin)
