# custom_admin/models.py

from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    # Other fields as required
    
    def __str__(self):
        return self.username
