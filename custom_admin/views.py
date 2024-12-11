# custom_admin/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.admin import AdminSite
from .models import CustomUser  # Example of importing a model
from core.models import CustomUser, Requirement
from issues.models import Issue
from notifications.models import Notification
from projects.models import UseCase, Project
from tasks.models import Task

from django.db.models import Count

def custom_admin_dashboard(request):
    user_count = CustomUser.objects.count()
    project_count = Project.objects.count()
    task_count = Task.objects.filter(status='open').count()
    notification_count = Notification.objects.filter(is_read=False).count()
    context = {
        'user_count': user_count,
        'project_count': project_count,
        'task_count': task_count,
        'notification_count': notification_count,
    }
    return render(request, 'custom_admin/dash.html', context)


def another_custom_view(request):
    return HttpResponse("This is another custom admin page")
