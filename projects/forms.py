from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'members']
        widgets = {
            'members': forms.CheckboxSelectMultiple(),
        }



from django import forms
from .models import UseCase

class UseCaseForm(forms.ModelForm):
    class Meta:
        model = UseCase
        fields = ['requirement', 'project', 'title', 'description', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
