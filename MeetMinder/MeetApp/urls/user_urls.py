from django.urls import path
from MeetApp.views.user_views import create_user, signin_user

urlpatterns = [
    path('create/', create_user, name='create_user'),
    path('signin/', signin_user, name='signin_user'),
]