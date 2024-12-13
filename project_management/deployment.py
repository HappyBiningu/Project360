import os
from .settings import *
from .settings import BASE_DIR

# Security settings for production
SECRET_KEY = os.environ['SECRET']  # Set in Azure portal
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]  # Automatically set by Azure
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']]  # Set to your domain
DEBUG = False  # Set to False for production

# WhiteNoise to serve static files efficiently
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise middleware for serving static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Tailwind CSS app name (if you're using Tailwind)
TAILWIND_APP_NAME = 'mytheme'

# Static files configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # Compress and cache static files
STATIC_URL = '/static/'  # URL path to serve static files
STATIC_ROOT = BASE_DIR / 'staticfiles'  # The directory where static files are collected after running collectstatic

# Directories where static files are stored during development
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Path where static files are stored before collection
]

# Media files (uploads)
MEDIA_URL = '/media/'  # URL path to serve media files
MEDIA_ROOT = BASE_DIR / 'media'  # Directory where uploaded media files are stored

# Database configuration (set this in your Azure App Service's environment variables)
conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': conn_str_params['dbname'],
        'HOST': conn_str_params['host'],
        'USER': conn_str_params['user'],
        'PASSWORD': conn_str_params['password'],
    }
}

# Optional: If you're using Azure Blob Storage for media files
# You can use `django-storages` and `azure-storage-blob` to store media in Azure Blob Storage instead of locally
# To install, use `pip install django-storages azure-storage-blob`
# MEDIA_URL = 'https://<your-storage-account-name>.blob.core.windows.net/<container-name>/'
# DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
