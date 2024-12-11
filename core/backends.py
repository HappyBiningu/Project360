from django.contrib.auth.backends import BaseBackend
from django.db.models import Q
from django.conf import settings
from core.models import CustomUser  # Import your custom user model

class EmailBackend(BaseBackend):
    """
    Custom authentication backend to authenticate using email instead of username.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(Q(email=username))  # Use CustomUser instead of User
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
