# your_app/admin.py
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone', 'message')
    readonly_fields = ('created_at',)
    
    def has_add_permission(self, request):
        return False  # Disable adding from admin