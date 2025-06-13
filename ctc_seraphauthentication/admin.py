from django.contrib import admin

# Register your models here.
from .models import PasswordResetLog

@admin.register(PasswordResetLog)
class PasswordResetLogAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_dn', 'timestamp', 'status', 'ip_address')
    list_filter = ('status', 'timestamp')
    search_fields = ('email', 'user_dn')