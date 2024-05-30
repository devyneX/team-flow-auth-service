from rest_framework.test import APITestCase

from src.accounts.models import User


class TestRegisterView(APITestCase):

    def test_post_valid_data(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@test.com',
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        }

        response = self.client.post('/api/register/', data=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

        user = User.objects.get(username='testuser')
        self.assertTrue(user.check_password('testpassword'))

    def test_post_invalid_data(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@test.com',
            'password': 'testpassword',
            'confirm_password': 'testpassword1'
        }

        response = self.client.post('/api/register/', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('password', response.data)
        self.assertEqual(response.data['password'][0], 'Passwords do not match.')

    def test_post_existing_email(self):
        user = User.objects.create_user(username='testuser', email='testuser@test.com', password='testpassword')

        data = {
            'username': 'testuser1',
            'email': user.email,
            'password': user.password,
            'confirm_password': user.password
        }

        response = self.client.post('/api/register/', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('email', response.data)
        self.assertEqual(response.data['email'][0], 'user with this email already exists.')

    def test_post_existing_username(self):
        user = User.objects.create_user(username='testuser', email='testuser@test.com', password='testpassword')

        data = {
            'username': user.username,
            'email': 'testuser1@test.com',
            'password': user.password,
            'confirm_password': user.password
        }

        response = self.client.post('/api/register/', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('username', response.data)
        self.assertEqual(response.data['username'][0], 'A user with that username already exists.')

    def test_authenticated_user(self):
        user = User.objects.create_user(username='testuser', email='testuser@test.com', password='testpassword')

        jwt = self.client.post('/api/token/', data={'username': user.username, 'password': 'testpassword'})

        data = {
            'username': 'testuser1',
            'email': 'testuser1@test.com',
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        }

        response = self.client.post('/api/register/', data=data, HTTP_AUTHORIZATION=f'Bearer {jwt.data["access"]}')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'Already registered.')
