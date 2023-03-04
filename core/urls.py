from django.urls import path
from .views import ListUsers, RegisterUser

urlpatterns = [
    path('users/', ListUsers.as_view()),
    path('register_user/', RegisterUser.as_view()),
]