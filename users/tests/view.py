from django.test import TestCase

class URLTests(TestCase):
    def test_user_register(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 404)