from django.urls import path
from . import views
from .views import mark_as_read



urlpatterns = [
    path('notifications/', views.notification_list, name='notification_list'),
    path('notifications/mark-as-read/<int:notification_id>/', mark_as_read, name='mark_as_read'),
]
