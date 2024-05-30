from django.urls import path

from src.user_api.views import GetUsersByIDs


urlpatterns = [
    path('users/', GetUsersByIDs.as_view(), name='users')
]
