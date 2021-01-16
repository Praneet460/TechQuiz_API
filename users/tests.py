from django.test import TestCase
from django.contrib.auth import get_user_model

class UserAccountTests(TestCase):
    
    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'testsuperuser@gmail.com', 'testsuperuser', 'SuperUser', 'superuser'
        )
        self.assertEqual(super_user.email, 'testsuperuser@gmail.com')
        self.assertEqual(super_user.user_name, 'testsuperuser')
        self.assertEqual(super_user.first_name, 'SuperUser')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "testsuperuser")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testsuperuser@gmail.com',
                user_name = 'testsuperuser',
                first_name = 'SuperUser',
                password = 'superuser',
                is_superuser = False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testsuperuser@gmail.com',
                user_name = 'testsuperuser',
                first_name = 'SuperUser',
                password = 'superuser',
                is_staff = False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='',
                user_name='testsuperuser',
                first_name='SuperUser',
                password='superuser',
                is_superuser=True
            )

        def test_custom_user(self):
            db = get_user_model()
            user = db.objects.create_user(
                'testuser@gmail.com', 'testuser', 'TestUser', 'testuser'
            )

            self.assertEqual(user.email, 'testuser@gmail.com')
            self.assertEqual(user.username, 'testuser')
            self.assertEqual(user.first_name, 'TestUser')
            self.assertTrue(user.is_staff)
            self.assertTrue(user.is_active)
            self.assertFalse(user.is_superuser)

            with self.assertRaises(ValueError):
                db.objects.create_user(
                    email='',
                    user_name='testuser',
                    first_name='TestUser',
                    password='testuser',
                    is_superuser=True
                )
