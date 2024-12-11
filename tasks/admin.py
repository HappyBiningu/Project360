from django.contrib import admin
from .models import Task
from core.models import CustomUser
from projects.models import Project
from django.utils.translation import gettext_lazy as _

class TaskAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'assignee', 'project', 'start_date', 'end_date', 'status', 'priority')
    
    # Filters for easy filtering
    list_filter = ('status', 'priority', 'assignee', 'project', 'start_date', 'end_date')
    
    # Search fields for easy searching
    search_fields = ('title', 'description', 'assignee__username', 'assignee__email', 'project__name')

    # Ordering of list, sorting by 'start_date' by default
    ordering = ('-start_date',)

    # Making it possible to add dependencies for tasks through a horizontal filter
    filter_horizontal = ('dependencies',)
    
    # Add a custom action to mark tasks as completed
    actions = ['mark_as_done']

    # Custom action to mark tasks as 'done'
    def mark_as_done(self, request, queryset):
        queryset.update(status='done')
    mark_as_done.short_description = _('Mark selected tasks as done')

# Registering the Task model with the customized admin
admin.site.register(Task, TaskAdmin)
