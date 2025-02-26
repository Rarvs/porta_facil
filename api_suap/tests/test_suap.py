from django.test import TestCase, RequestFactory
from rest_framework import status
from rest_framework.test import APIClient
from requests_mock import Mocker
from api_suap.tests import login

class LoginViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = RequestFactory()
        self.login_url = 'suap/login'  # Updated endpoint based on urls.py
        self.suap_api_url = 'https://suap.ifsuldeminas.edu.br/api/v2/autenticacao/token/'

    @Mocker()
    def test_login_success(self, mock):
        # Mock the SUAP API response for a successful login
        mock_response = {
            "token": "fake-token",
            "user": {
                "username": "123456",
                "name": "Test User"
            }
        }
        mock.post(self.suap_api_url, json=mock_response, status_code=200)

        # Prepare the request data
        data = {
            "RA": "123456",
            "senha": "password123"
        }

        # Make the request to the login view
        response = self.client.post(self.login_url, data, format='json')

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, mock_response)

    @Mocker()
    def test_login_missing_credentials(self, mock):
        # Make the request to the login view without providing RA or senha
        data = {}
        response = self.client.post(self.login_url, data, format='json')

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"error": "RA e senha são obrigatórios."})

    @Mocker()
    def test_login_invalid_credentials(self, mock):
        # Mock the SUAP API response for invalid credentials
        mock_response = {
            "detail": "Invalid credentials"
        }
        mock.post(self.suap_api_url, json=mock_response, status_code=401)

        # Prepare the request data
        data = {
            "RA": "123456",
            "senha": "wrongpassword"
        }

        # Make the request to the login view
        response = self.client.post(self.login_url, data, format='json')

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, mock_response)

    @Mocker()
    def test_login_suap_api_error(self, mock):
        # Mock a connection error to the SUAP API
        mock.post(self.suap_api_url, exc=requests.exceptions.RequestException)

        # Prepare the request data
        data = {
            "RA": "123456",
            "senha": "password123"
        }

        # Make the request to the login view
        response = self.client.post(self.login_url, data, format='json')

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertIn("error", response.data)