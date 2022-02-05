from django.test import TestCase
from .models import ShopUser


# Create your tests here.
class ModelTests(TestCase):
    def test_user_is_created_with_activation_key(self):
        user = ShopUser.objects.create(age=13)
        self.assertIsNotNone(user.age)