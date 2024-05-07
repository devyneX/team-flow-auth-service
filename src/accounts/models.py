import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from src.accounts.manager import UserManager


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # noqa
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    objects = UserManager()
