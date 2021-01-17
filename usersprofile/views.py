from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.http import JsonResponse

from .models import Profile
from .serializers import ProfileSerializer

class UserProfile(APIView):
    permission_classes = [AllowAny]

    def get(self, request, username):
        profile = Profile.objects.get(user__user_name = username)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
       