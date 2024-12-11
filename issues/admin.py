from django.contrib import admin
from .models import Issue
from django.utils.translation import gettext_lazy as _
from .filters import IssueFilter

# Issue Admin
class IssueAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'project', 'assignee', 'issue_type', 'priority', 'status', 'created_at', 'updated_at')
    
    # Filters in the right sidebar for easy filtering
    list_filter = ('status', 'priority', 'assignee', 'project', 'issue_type', 'created_at')
    
    # Fields for searching in the admin panel
    search_fields = ('title', 'description', 'project__name', 'assignee__username')
    
    # Ordering the list based on creation date
    ordering = ('-created_at',)
    
    # Allow filtering by custom IssueFilter
    actions = ['mark_as_completed']
    
    # Custom action to mark issues as completed
    def mark_as_completed(self, request, queryset):
        queryset.update(status='done')
    mark_as_completed.short_description = _('Mark selected issues as Completed')

    # Customize how the fields are displayed on the form view
    fieldsets = (
        (None, {'fields': ('title', 'description', 'project', 'issue_type', 'priority', 'status', 'assignee')}),
        (_('Timestamps'), {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
    
    # Make created_at and updated_at read-only
    readonly_fields = ('created_at', 'updated_at')
    
    # Remove filter_horizontal and filter_vertical, as they are for many-to-many relationships.
    # No need to use filter_horizontal or filter_vertical with ForeignKey fields (project, assignee)

# Registering Issue model with customized admin
admin.site.register(Issue, IssueAdmin)
