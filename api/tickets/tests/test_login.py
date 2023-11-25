from django.test import TestCase
from django.contrib.auth.models import User


class LoginTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            email="test@test.com",
            password="test",
        )

    def test_login(self):
        body = {
            "username": "test",
            "password": "test",
        }
        response = self.client.post("/api-token-auth/", body)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("token" in response.json())


