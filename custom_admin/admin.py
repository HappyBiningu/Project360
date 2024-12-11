from django.contrib.admin import AdminSite
from django.contrib import admin
from core.models import CustomUser, Requirement
from issues.models import Issue
from notifications.models import Notification
from projects.models import UseCase, Project
from tasks.models import Task


class MyAdminSite(AdminSite):
    site_header = "Project360 Admin"
    site_title = "Project360 Admin Portal"
    index_title = "Welcome to Project360 Administration"

# Instantiate the custom admin site
my_admin_site = MyAdminSite(name='myadmin')

# Register models with the custom admin site
@admin.register(CustomUser, site=my_admin_site)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'is_supended')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'email')

@admin.register(Requirement, site=my_admin_site)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'status', 'created_by', 'created_at')
    list_filter = ('priority', 'status')
    search_fields = ('title', 'description')

@admin.register(Project, site=my_admin_site)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('name',)

@admin.register(Task, site=my_admin_site)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'status', 'assignee', 'project')
    list_filter = ('priority', 'status', 'project')
    search_fields = ('title', 'description')

@admin.register(Issue, site=my_admin_site)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'status', 'assignee', 'project')
    list_filter = ('priority', 'status', 'issue_type')
    search_fields = ('title', 'description')

@admin.register(Notification, site=my_admin_site)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'is_read', 'user', 'created_at')
    list_filter = ('is_read',)
    search_fields = ('message',)

@admin.register(UseCase, site=my_admin_site)
class UseCaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'requirement', 'project', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')
