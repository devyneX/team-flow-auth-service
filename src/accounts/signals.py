import json

from django.db.models.signals import post_save
from django.dispatch import receiver
from src.accounts.models import User
from src.accounts.serializers.user_serializers import UserSerializer
from src.accounts.producer import ProducerUserCreated


@receiver(post_save, sender=User)
def post_user_creation(sender, instance, created, **kwargs):
    if created:
        print('User created: ', instance)
        serializer = UserSerializer(instance)
        ProducerUserCreated().publish('user_created_method', serializer.data)
