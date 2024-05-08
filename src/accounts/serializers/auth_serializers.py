from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from src.accounts.models import User


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirm_password']
        extra_kwargs = {
            'email': {
                'required': True
            },
            'username': {
                'required': True
            },
            'password': {
                'required': True,
                'write_only': True
            },
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return super().create(validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.get_full_name()
        token['username'] = user.username
        token['email'] = user.email
        return token
