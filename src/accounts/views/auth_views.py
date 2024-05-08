from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from src.accounts.serializers.auth_serializers import RegisterSerializer
from src.accounts.utils.jwt_utils import get_token_for_user


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated.'}, status=status.HTTP_400_BAD_REQUEST)

        return super().dispatch(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = get_token_for_user(user)
        return Response(token, status=status.HTTP_201_CREATED)

        # return Response({'detail': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
