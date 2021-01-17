from django.conf.urls import url
from django.urls import path
from .views import UserProfile

app_name = 'usersprofile'

urlpatterns = [
    # path('', UserProfile.as_view())
    url(r'^(?P<username>\w{0,50})/$', UserProfile.as_view()),
]