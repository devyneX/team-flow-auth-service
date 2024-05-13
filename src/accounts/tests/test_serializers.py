from django.test import TestCase

from src.accounts.models import User
from src.accounts.serializers.auth_serializers import CustomTokenObtainPairSerializer, RegisterSerializer


class TestRegisterSerializer(TestCase):

    def setUp(self):
        self.serializer = RegisterSerializer()

    def test_register_serializer_with_valid_data(self):
        data = {'email': 'test1@test.com', 'username': 'test1', 'password': 'password', 'confirm_password': 'password'}

        serializer = RegisterSerializer(data=data)

        self.assertTrue(serializer.is_valid(), serializer.errors)

        user = serializer.save()

        self.assertIsInstance(user, User)

    def test_register_serializer_with_no_data(self):
        data = {}
        serializer = RegisterSerializer(data=data)

        self.assertFalse(serializer.is_valid())

        self.assertIn('email', serializer.errors)
        self.assertIn('username', serializer.errors)
        self.assertIn('password', serializer.errors)
        self.assertIn('confirm_password', serializer.errors)

    def test_register_serializer_with_invalid_email(self):
        data = {'email': 'test1', 'username': 'test1', 'password': 'password', 'confirm_password': 'password'}
        serializer = RegisterSerializer(data=data)

        self.assertFalse(serializer.is_valid())

        self.assertIn('email', serializer.errors)

    def test_register_serializer_with_unmatched_passwords(self):
        data = {
            'email': 'test1@test.com',
            'username': 'test1',
            'password': 'password',
            'confirm_password': 'password1'
        }
        serializer = RegisterSerializer(data=data)

        self.assertFalse(serializer.is_valid())

        self.assertIn('password', serializer.errors)

        self.assertEqual(serializer.errors['password'][0], 'Passwords do not match.')


class TestCustomTokenObtainPairSerializer(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', email='test@test.com', password='password')

    def test_get_token(self):
        data = {'username': 'test', 'password': 'password'}
        serializer = CustomTokenObtainPairSerializer(data=data)

        self.assertTrue(serializer.is_valid(), serializer.errors)

        token = serializer.get_token(self.user)

        self.assertEqual(token['username'], self.user.username)
        self.assertEqual(token['email'], self.user.email)
