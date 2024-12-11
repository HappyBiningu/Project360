from django.contrib import admin
from .models import Notification
from django.utils.translation import gettext_lazy as _

class NotificationAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('user', 'message', 'is_read', 'created_at')
    
    # Filters in the right sidebar for easy filtering
    list_filter = ('is_read', 'created_at', 'user')
    
    # Fields for searching in the admin panel
    search_fields = ('message', 'user__username', 'user__email')

    # Allow ordering by created date
    ordering = ('-created_at',)

    # Optionally allow bulk marking as read
    actions = ['mark_as_read']

    # Custom action to mark notifications as read
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = _('Mark selected notifications as read')

# Registering the Notification model with customized admin
admin.site.register(Notification, NotificationAdmin)
