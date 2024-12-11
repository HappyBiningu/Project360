# custom_admin/urls.py

from django.urls import path
from . import views  # Import views from the same appa




urlpatterns = [
    path('dash/', views.custom_admin_dashboard, name='custom_admin_dashboard'),
    path('another/', views.another_custom_view, name='another_custom_view'),
]
