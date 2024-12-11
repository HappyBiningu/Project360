# core/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomerUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=20, required=True)
    surname = forms.CharField(max_length=20, required=True)
    company = forms.CharField(max_length=255, required=True)
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'name', 'surname', 'company', 'role']


class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))


from django import forms
from .models import Requirement, RequirementAttachment


class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement
        fields = [
            'title', 
            'description', 
            'priority', 
            'status', 
            'feature', 
            'previous_version'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'feature': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RequirementAttachmentForm(forms.ModelForm):
    class Meta:
        model = RequirementAttachment
        fields = ['requirement', 'file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
