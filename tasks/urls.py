from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('kanban/', views.kanban_board, name='kanban_board'),
    path('gantt/', views.gantt_chart, name='gantt_chart'),
    path('update-status/<int:task_id>/', views.update_task_status, name='update_task_status'),
]
