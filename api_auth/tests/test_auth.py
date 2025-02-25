from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class AuthenticationTests(APITestCase):
    def setUp(self):
        # Create a user for testing
        self.username = "testuser"
        self.password = "testpass123"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
        self.auth_url = reverse(
            "api/auth/login/"
        )  # Replace 'auth' with the actual name of your auth endpoint

    def test_user_authentication_with_valid_credentials(self):
        # Test authentication with valid credentials
        data = {
            "username": self.username,
            "password": self.password,
        }
        response = self.client.post(self.auth_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(
            "token", response.data
        )  # Assuming your auth endpoint returns a token

    def test_user_authentication_with_invalid_credentials(self):
        # Test authentication with invalid credentials
        data = {
            "username": self.username,
            "password": "wrongpassword",
        }
        response = self.client.post(self.auth_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("token", response.data)

    def test_user_authentication_with_missing_credentials(self):
        # Test authentication with missing credentials
        data = {
            "username": self.username,
            # 'password' is missing
        }
        response = self.client.post(self.auth_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("token", response.data)

    def test_user_authentication_with_empty_credentials(self):
        # Test authentication with empty credentials
        data = {
            "username": "",
            "password": "",
        }
        response = self.client.post(self.auth_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("token", response.data)

#python manage.py test