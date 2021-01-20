from django.conf.urls import url
from django.urls import path
from .views import SearchUserProfile, UserProfile

app_name = 'usersprofile'

urlpatterns = [
    url(r'^search/(?P<username>\w{0,50})/$', SearchUserProfile.as_view()),
    url(r'^profile/(?P<username>\w{0,50})/$', UserProfile.as_view())
]