from django.db import models
from projects.models import Project
from core.models import CustomUser

ISSUE_TYPE_CHOICES = (
    ('bug', 'Bug'),
    ('task', 'Task'),
    ('feature', 'Feature'),
)

PRIORITY_CHOICES = (
    ('low', 'Low'),
    ('medium','Medium'),
    ('high','High'),
    ('critical','Critical'),
)

STATUS_CHOICES = (
    ('to_do', 'To Do'),
    ('in_progress', 'In progress'),
    ('done', 'Done'),
)

class Issue(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPE_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to do')
    assignee = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null= True, related_name='assigned_issues')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title   
