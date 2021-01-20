from rest_framework import serializers
from .models import Profile
from users.serializers import CustomUserSerializer

class SearchProfileSerializer(serializers.ModelSerializer):

    user = CustomUserSerializer(required=True)
    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'about', 'location', 'birth_date', 'gender'
        ]

class ProfileSerializer(serializers.ModelSerializer):

    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Profile
        fields = [
            'id', 'about', 'location', 'birth_date', 'gender'
        ]