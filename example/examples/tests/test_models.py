from django.test import TestCase
from ..models import User


class UserTest(TestCase):
    """ Test module for USER model """

    def setUp(self):
        User.objects.create(
            first_name='Aaron', last_name='Gunther', age=21, phone_number =6186946053, address='1521 Themis Street Cape Girardeau MO')

    def test_user_get_name(self):
        user_aaron = User.objects.get(first_name='Aaron')
        self.assertEqual(user_aaron.get_name(), "First Name: Aaron Last Name: Gunther")