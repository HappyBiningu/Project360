# issues/filters.py
import django_filters
from .models import Issue

class IssueFilter(django_filters.FilterSet):
    class Meta:
        model = Issue
        fields = ['status', 'priority', 'assignee']  # Adjust based on your model fields
