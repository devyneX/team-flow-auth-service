import uuid

from model_bakery import baker
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from src.accounts.models import User


# Create your tests here.
class TestGetUserByIDsView(APITestCase):

    def setUp(self):
        self.url = reverse('user_api:users')

        user1 = baker.make(User)
        user2 = baker.make(User)
        user3 = baker.make(User)
        user4 = baker.make(User)
        user5 = baker.make(User)

        self.data = {'uuids': [user1.uuid, user2.uuid, user3.uuid, user4.uuid, user5.uuid]}

    def test_post_valid_data(self):
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)

    def test_non_existing_uuids(self):
        non_existing_uuid = str(uuid.uuid4())

        while uuid in self.data['uuids']:
            non_existing_uuid = str(uuid.uuid4())

        self.data['uuids'].append(non_existing_uuid)

        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 6)
        self.assertEqual(response.data.get(non_existing_uuid), 'User not found')

    def test_invalid_uuids(self):
        self.data['uuids'].append('invalid_uuid')
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 400)
