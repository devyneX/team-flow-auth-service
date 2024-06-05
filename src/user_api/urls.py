from django.urls import path

from src.user_api.views import GetUsersByIDs, UserRetrieveView

app_name = 'user_api'

urlpatterns = [
    path('users/get_by_ids', GetUsersByIDs.as_view(), name='get_users_by_ids'),
    path('users/<uuid:uuid>', UserRetrieveView.as_view(), name='users'),
]
