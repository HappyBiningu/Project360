from django.urls import path
from . import views



urlpatterns = [
    path('projects/', views.project_list, name='project_list'), 
    path('create/', views.project_create, name='project_create'),
    path('<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('use-cases/', views.use_case_list, name='use_case_list'),
    path('use-cases/create/', views.use_case_create, name='use_case_create'),
    path('use-cases/<int:pk>/', views.use_case_detail, name='use_case_detail'),
    path('projects/create/', views.issue_create, name='issue_create'),
]
