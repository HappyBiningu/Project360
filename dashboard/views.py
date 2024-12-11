from django.shortcuts import render
from django.db.models import Count
from django.utils import timezone
from projects.models import Project
from issues.models import Issue
from tasks.models import Task
from core.models import Requirement
from core.decorators import role_required

def dashboard(request):
    # Projects and Issues
    total_projects = Project.objects.count()
    total_issues = Issue.objects.count()
    issues_by_status = Issue.objects.values('status').annotate(count=Count('id'))

    # Tasks
    total_tasks = Task.objects.count()
    tasks_by_status = Task.objects.values('status').annotate(count=Count('id'))
    tasks_by_priority = Task.objects.values('priority').annotate(count=Count('id'))
    overdue_tasks = Task.objects.filter(end_date__lt=timezone.now(), status__in=['to_do', 'in_progress']).count()

    # Project Dashboard Data
    tasks = Task.objects.all()
    total_project_tasks = tasks.count()
    completed_tasks = tasks.filter(status='Completed').count()
    in_progress_tasks = tasks.filter(status='In Progress').count()

    requirements = Requirement.objects.all()
    total_requirements = requirements.count()

    # Context for template
    context = {
        'total_projects': total_projects,
        'total_issues': total_issues,
        'issues_by_status': issues_by_status,
        'total_tasks': total_tasks,
        'tasks_by_status': tasks_by_status,
        'tasks_by_priority': tasks_by_priority,
        'overdue_tasks': overdue_tasks,
        'total_project_tasks': total_project_tasks,
        'completed_tasks': completed_tasks,
        'in_progress_tasks': in_progress_tasks,
        'total_requirements': total_requirements,
    }

    return render(request, 'dashboard/dashboard.html', context)
