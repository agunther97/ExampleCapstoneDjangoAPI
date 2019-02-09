import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import User
from ..serializers import UserSerializer


# initialize the APIClient app
client = Client()

class GetAllUsersTest(TestCase):
    """ Test module for GET all users API """

    def setUp(self):
        User.objects.create(
            first_name='Casper', phone_number=6186946051, age=21, last_name='Gunther', address='address1')
        User.objects.create(
            first_name='Muffin', phone_number=6186946052, age=21, last_name='Ranciglio', address='address2')
        User.objects.create(
            first_name='Rambo', phone_number=6186946053, age=25, last_name='Sladek', address='address3')
        User.objects.create(
            first_name='Ricky', phone_number=6186946054, age=30, last_name='Crutcher', address='address4')

    def test_get_all_users(self):
        # get API response
        response = client.get(reverse('get_post_users'))
        # get data from db
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleUserTest(TestCase):
    """ Test module for GET single user API """

    def setUp(self):
        self.casper = User.objects.create(
            first_name='Casper', phone_number=6186946051, age=21, last_name='Gunther', address='address1')
        self.muffin = User.objects.create(
            first_name='Muffin', phone_number=6186946052, age=21, last_name='Ranciglio', address='address2')
        self.rambo = User.objects.create(
            first_name='Rambo', phone_number=6186946053, age=25, last_name='Sladek', address='address3')
        self.ricky = User.objects.create(
            first_name='Ricky', phone_number=6186946054, age=30, last_name='Crutcher', address='address4')

    def test_get_valid_single_user(self):
        response = client.get(
            reverse('get_delete_update_user', kwargs={'pk': self.rambo.pk}))
        user = User.objects.get(pk=self.rambo.pk)
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_user(self):
        response = client.get(
            reverse('get_delete_update_user', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewUserTest(TestCase):
    """ Test module for inserting a new user """

    def setUp(self):
        self.valid_payload = {
            'first_name': 'Muffin',
            'last_name' : 'Ranciglio',
            'age': 21,
            'address': 'address2',
            'phone_number': 6186946052
        }
        self.invalid_payload = {
            'first_name': '',
            'last_name' : 'Gunther',
            'age': 21,
            'address': 'address1',
            'phone_number': 12345678
        }

    def test_create_valid_user(self):
        response = client.post(
            reverse('get_post_users'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        response = client.post(
            reverse('get_post_users'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)