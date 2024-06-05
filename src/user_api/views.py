from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from src.accounts.models import User
from src.user_api.serializers.user_serializers import UserAPIListSerializer, UserSerializer


class UserRetrieveView(RetrieveAPIView):
    """
    GET /api/users/<uuid:uuid>/
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'uuid'


class GetUsersByIDs(APIView):
    """
    POST /api/users/get_by_ids
    {
        "uuids": [
            "d3f3a4d4-0f3b-4b3e-8c8b-4c3e6b9e0b8b",
            "d3f3a4d4-0f3b-4b3e-8c8b-4c3e6b9e0b8c",
            ...
        ]
    }
    **All values must be UUIDs**
    """

    def post(self, request, *args, **kwargs):
        serializer = UserAPIListSerializer(data=request.data)

        if serializer.is_valid():
            results = serializer.validated_data['uuids']
            return Response(results, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
