from django.contrib.auth import get_user_model
from django.test import TestCase


class TestUserModel(TestCase):

    def setUp(self):
        self.model = get_user_model()

    def test_create_user(self):
        user = self.model.objects.create_user(username='username', email='test@test.com', password='password')

        self.assertFalse(user.is_email_verified, 'is_email_verified should be False')

        with self.assertRaises(TypeError):
            self.model.objects.create_user()
        with self.assertRaises(TypeError):
            self.model.objects.create_user(username='')
        with self.assertRaises(TypeError):
            self.model.objects.create_user(email='')
        with self.assertRaises(ValueError):
            self.model.objects.create_user(username='', email='test@test.com', password='password')
        with self.assertRaises(ValueError):
            self.model.objects.create_user(username='username', email='', password='password')

    def test_create_superuser(self):
        self.model.objects.create_superuser(username='username', email='email', password='password')

        with self.assertRaises(ValueError):
            self.model.objects.create_superuser(
                username='username', email='email', password='password', is_superuser=False
            )

        with self.assertRaises(ValueError):
            self.model.objects.create_superuser(
                username='username', email='email', password='password', is_staff=False
            )
