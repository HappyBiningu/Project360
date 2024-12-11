from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from custom_admin.admin import my_admin_site 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom-admin/', my_admin_site.urls),
    path('custom-admin/', include('custom_admin.urls')),
    path('projects/', include('projects.urls')),
    path('issues/', include('issues.urls')),
    path('dashboard', include('dashboard.urls')),
    path('tasks/', include('tasks.urls')),
    path('', include('core.urls')),
    path('notifications/', include('notifications.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
