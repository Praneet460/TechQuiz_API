from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.http import JsonResponse
from django.http import Http404

from .models import Profile
from .serializers import SearchProfileSerializer, ProfileSerializer
from .permissions import CustomUpdatePermission

class SearchUserProfile(APIView):
    permission_classes = [AllowAny]

    def get(self, request, username):
        profile = Profile.objects.get(user__user_name = username)
        serializer = SearchProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
       
class UserProfile(APIView):

    permission_classes = [CustomUpdatePermission]

    def get_object(self, username):
        try:
            return Profile.objects.get(user__user_name = username)
        except Profile.DoesNotExist:
            raise Http404 

    def get(self, request, username, format=None, *args, **kwargs):
        profile = self.get_object(username)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, username, format=None, *args, **kwargs):
        
        profile = self.get_object(username)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, username, format=None, *args, **kwargs):
        
        profile = self.get_object(username)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
