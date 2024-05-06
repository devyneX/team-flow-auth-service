import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from src.accounts.manager import UserManager


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    objects = UserManager()
