from rest_framework import serializers
from .models import Profile
from users.serializers import CustomUserSerializer

class ProfileSerializer(serializers.ModelSerializer):

    user = CustomUserSerializer(required=True)
    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'about', 'location', 'birth_date', 'gender'
        ]