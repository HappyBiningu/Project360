from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings 

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin','Admin'),
        ('project_manager','Project Manager'),
        ('developer','Developer'),
        ('system_designer','System Designer'),
        ('system_analyst','System Analyst'),
        ('viewer','Viewer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')
    name = models.CharField(max_length=20, blank=True, null=True)
    surname = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_supended = models.BooleanField(default=False)


    def is_admin(self):
        return self.role == 'admin'
    





from django.db import models
from django.conf import settings

class Requirement(models.Model):
    # Priority choices for consistency
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    # Status choices
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    # Basic fields for the requirement
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    feature = models.CharField(max_length=255)

    # Version control for tracking changes
    version = models.IntegerField(default=1)
    previous_version = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='next_version'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class RequirementAttachment(models.Model):
    requirement = models.ForeignKey(Requirement, related_name='attachments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='requirements/attachments/')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for {self.requirement.title}"
