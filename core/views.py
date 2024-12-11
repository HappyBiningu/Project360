from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Requirement, RequirementAttachment
from .forms import RequirementForm, RequirementAttachmentForm

# List view for Requirements
def requirement_list(request):
    requirements = Requirement.objects.all()
    return render(request, 'requirements/requirement_list.html', {'requirements': requirements})

# Detail view for a single Requirement
def requirement_detail(request, pk):
    requirement = get_object_or_404(Requirement, pk=pk)
    return render(request, 'requirements/requirement_detail.html', {'requirement': requirement})

# Create a new Requirement
def requirement_create(request):
    if request.method == 'POST':
        form = RequirementForm(request.POST, request.FILES)
        if form.is_valid():
            requirement = form.save(commit=False)
            requirement.created_by = request.user  # Set the logged-in user
            requirement.save()
            return redirect('requirement_list')
    else:
        form = RequirementForm()
    return render(request, 'requirements/requirement_form.html', {'form': form})

# Update an existing Requirement
def requirement_update(request, pk):
    requirement = get_object_or_404(Requirement, pk=pk)
    if request.method == 'POST':
        form = RequirementForm(request.POST, instance=requirement)
        if form.is_valid():
            form.save()
            return redirect('requirement_detail', pk=requirement.pk)
    else:
        form = RequirementForm(instance=requirement)
    return render(request, 'requirements/requirement_form.html', {'form': form})

# Delete a Requirement
def requirement_delete(request, pk):
    requirement = get_object_or_404(Requirement, pk=pk)
    if request.method == 'POST':
        requirement.delete()
        return redirect('requirement_list')
    return render(request, 'requirements/requirement_confirm_delete.html', {'requirement': requirement})

# Add attachment to a Requirement
def add_attachment(request, requirement_id):
    requirement = get_object_or_404(Requirement, pk=requirement_id)
    if request.method == 'POST':
        form = RequirementAttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            attachment = form.save(commit=False)
            attachment.requirement = requirement
            attachment.save()
            return redirect('requirement_detail', pk=requirement.pk)
    else:
        form = RequirementAttachmentForm()
    return render(request, 'requirements/add_attachment.html', {'form': form, 'requirement': requirement})


# core/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomerUserCreationForm, EmailLoginForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Login the user after signup
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('dashboard')  # Redirect to dashboard or another page
    else:
        form = CustomerUserCreationForm()
    return render(request, 'requirements/signup.html', {'form': form})

# core/views.py
from django.contrib.auth.views import LoginView
from .forms import EmailLoginForm

class CustomLoginView(LoginView):
    authentication_form = EmailLoginForm
    template_name = 'requirements/login.html'

    def form_valid(self, form):
        return super().form_valid(form)

