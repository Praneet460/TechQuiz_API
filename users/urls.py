from django.urls import path
from .views import CustomUserRegister

app_name = 'users'

urlpatterns = [
    path('', CustomUserRegister.as_view(), name='register_user'),
]