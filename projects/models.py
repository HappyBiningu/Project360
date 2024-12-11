from django.db import models
from core.models import CustomUser

class Project(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('in_progress','In Progress'),
        ('completed','Completed'),
    ]
    name = models.CharField(max_length=100)
    description =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField(CustomUser, related_name='projects')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    

    def __str__(self):
        return self.name 
    
from django.db import models
from core.models import Requirement, CustomUser

class UseCase(models.Model):
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name="use_cases")
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name="use_cases")  # Linking UseCase to a project
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('Draft', 'Draft'),
        ('Under Review', 'Under Review'),
        ('Approved', 'Approved')
    ], default='Draft')

    def __str__(self):
        return self.title
