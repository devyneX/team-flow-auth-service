from django.urls import path

from src.user_api.views import GetUsersByIDs

app_name = 'user_api'

urlpatterns = [path('users/', GetUsersByIDs.as_view(), name='users')]
