from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from issues.forms import IssueForm 
from notifications.models import Notification


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def issue_create(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            return redirect('issue_list')
    else:
        form = IssueForm()
    return render(request, 'projects/issue_form.html', {'form': form})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')  # Redirect to project list or another relevant page
    else:
        form = ProjectForm()
    
    return render(request, 'projects/project_create.html', {'form': form})



from django.shortcuts import render, get_object_or_404, redirect
from .models import UseCase
from .forms import UseCaseForm

def use_case_list(request):
    """
    View to list all use cases.
    """
    # Calculate the unread notifications count
    unread_notifications_count = Notification.objects.filter(user=request.user, is_read=False).count()

    # Pass it to the context
    context = {
        'unread_notifications_count': unread_notifications_count,
    }

    use_cases = UseCase.objects.all()
    return render(request, 'projects/use_case_list.html', {'use_cases': use_cases})


def use_case_create(request):
    """
    View to create a new use case.
    """
    if request.method == 'POST':
        form = UseCaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('use_case_list')
    else:
        form = UseCaseForm()
    return render(request, 'projects/use_case_form.html', {'form': form})


def use_case_detail(request, pk):
    """
    View to display details of a specific use case.
    """
    use_case = get_object_or_404(UseCase, pk=pk)
    return render(request, 'projects/use_case_detail.html', {'use_case': use_case})


def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')  # Redirect to project list after editing
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_edit.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Project

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.delete()
        return redirect('project_list')  # Redirect to the project list after deletion
    return HttpResponseForbidden("You are not allowed to perform this action.")


from django.shortcuts import render, get_object_or_404
from .models import Project

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})
