from django.contrib import admin
from .models import Project, UseCase
from core.models import CustomUser
from django.utils.translation import gettext_lazy as _

# Customizing the Project model for admin
class ProjectAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'status', 'created_at', 'updated_at')
    
    # Filters for easy filtering
    list_filter = ('status', 'created_at', 'members')

    # Search fields for easy search
    search_fields = ('name', 'description', 'members__username', 'members__email')

    # Ordering of list
    ordering = ('-created_at',)

    # To allow in-line member selection and editing
    filter_horizontal = ('members',)

    # Optional: Add a custom action to change the status of a project
    actions = ['mark_as_completed']

    # Custom action to mark the project as completed
    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
    mark_as_completed.short_description = _('Mark selected projects as completed')

# Registering the Project model with the customized admin
admin.site.register(Project, ProjectAdmin)


# Customizing the UseCase model for admin
class UseCaseAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'requirement', 'project', 'status')

    # Filters for easy filtering
    list_filter = ('status', 'requirement', 'project')

    # Search fields for easy search
    search_fields = ('title', 'description', 'requirement__title', 'project__name')

    # Ordering of list, using 'title' or 'requirement' as default ordering
    ordering = ('title',)

# Registering the UseCase model with the customized admin
admin.site.register(UseCase, UseCaseAdmin)
