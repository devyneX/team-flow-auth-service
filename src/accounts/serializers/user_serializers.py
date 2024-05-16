from rest_framework import serializers

from src.accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'uuid',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
            'is_superuser',
        )
