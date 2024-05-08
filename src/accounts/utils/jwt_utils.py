from src.accounts.serializers.auth_serializers import CustomTokenObtainPairSerializer


def get_token_for_user(user):
    refresh = CustomTokenObtainPairSerializer.get_token(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
