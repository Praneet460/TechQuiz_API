from django.test import TestCase
from django.contrib.auth import get_user_model
from usersprofile.models import Profile

class ProfileTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        print("DB Testing...")
        db = get_user_model()
        test_user = db.objects.create_user(
                'testuser@gmail.com',
                'testuser',
                'TestUser',
                'testuser'
        )
        cls.profile = Profile.objects.get(user=test_user)
        cls.profile.about = 'I am a TestUser'
        cls.profile.location = "India"
        cls.profile.gender = 0

    def test_profile_model_str(self): 
        self.assertEqual(str(self.profile), "testuser")

    def test_profile_model_about(self):
        self.assertEqual(self.profile.about, 'I am a TestUser')

    def test_profile_model_location(self):
        self.assertEqual(self.profile.location, 'India')

    def test_profile_model_gender(self):
        self.assertEqual(self.profile.gender, 0)

    def test_user_model_email(self):
        self.assertEqual(self.profile.user.email, "testuser@gmail.com")

    def test_user_model_user_name(self):
        self.assertEqual(self.profile.user.user_name, "testuser")

    def test_user_model_first_name(self):
        self.assertEqual(self.profile.user.first_name, "TestUser")