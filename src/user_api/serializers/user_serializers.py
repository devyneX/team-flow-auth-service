from rest_framework import serializers

from src.accounts.models import User


class UserAPIListSerializer(serializers.Serializer):
    uuids = serializers.ListField(
        child=serializers.UUIDField(),
        allow_empty=False,
    )

    def validate_uuids(self, value):
        result = {}
        for user_uuid in value:
            user_uuid_str = str(user_uuid)
            user = User.objects.filter(uuid=user_uuid).first()
            if user:
                result[user_uuid_str] = UserSerializer(user).data
            else:
                result[user_uuid_str] = 'User not found'
        return result


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
