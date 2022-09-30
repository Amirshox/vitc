from django.contrib.auth.models import AbstractUser

from .manager import UserManager


class User(AbstractUser):
    first_name = None
    last_name = None
    email = None

    EMAIL_FIELD = None
    REQUIRED_FIELDS = []

    objects = UserManager()


__all__ = [
    'User',
]
