import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from src.accounts.managers import UserManager


class User(AbstractUser):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    objects = UserManager()
