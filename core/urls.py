from django.urls import path
from . import views
from .views import CustomLoginView, signup_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('requirements', views.requirement_list, name='requirement_list'),
    path('<int:pk>/', views.requirement_detail, name='requirement_detail'),
    path('create/', views.requirement_create, name='requirement_create'),
    path('<int:pk>/update/', views.requirement_update, name='requirement_update'),
    path('<int:pk>/delete/', views.requirement_delete, name='requirement_delete'),
    path('<int:requirement_id>/add-attachment/', views.add_attachment, name='add_attachment'),
    path('', CustomLoginView.as_view(), name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
