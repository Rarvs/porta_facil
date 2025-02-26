from django.test import TestCase, RequestFactory
from rest_framework.test import APIClient, force_authenticate
from rest_framework import status
from django.contrib.auth.models import User
from api_permission.models import Coordinator
from api_permission.views import CoordinatorListCreateAPIView
from api_permission.serializers import CoordinatorSerializer

class CoordinatorListCreateAPIViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = RequestFactory()
        self.coordinator_list_create_url = '/coordinator/'  # Updated endpoint based on urls.py

        # Create a regular user
        self.regular_user = User.objects.create_user(username='regularuser', password='testpass')

        # Create a coordinator user
        self.coordinator_user = User.objects.create_user(username='coordinatoruser', password='testpass')
        self.coordinator = Coordinator.objects.create(user=self.coordinator_user)

    def test_list_coordinators_as_coordinator(self):
        # Authenticate as a coordinator user
        self.client.force_authenticate(user=self.coordinator_user)

        # Make a GET request to the CoordinatorListCreateAPIView
        response = self.client.get(self.coordinator_list_create_url)

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one coordinator exists in the database

    def test_list_coordinators_as_regular_user(self):
        # Authenticate as a regular user (non-coordinator)
        self.client.force_authenticate(user=self.regular_user)

        # Make a GET request to the CoordinatorListCreateAPIView
        response = self.client.get(self.coordinator_list_create_url)

        # Assert the response (should be forbidden)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_coordinator_as_coordinator(self):
        # Authenticate as a coordinator user
        self.client.force_authenticate(user=self.coordinator_user)

        # Prepare the data for creating a new coordinator
        new_user = User.objects.create_user(username='newcoordinator', password='testpass')
        data = {
            "user": new_user.id
        }

        # Make a POST request to the CoordinatorListCreateAPIView
        response = self.client.post(self.coordinator_list_create_url, data, format='json')

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Coordinator.objects.count(), 2)  # Two coordinators should exist now

    def test_create_coordinator_as_regular_user(self):
        # Authenticate as a regular user (non-coordinator)
        self.client.force_authenticate(user=self.regular_user)

        # Prepare the data for creating a new coordinator
        new_user = User.objects.create_user(username='newcoordinator', password='testpass')
        data = {
            "user": new_user.id
        }

        # Make a POST request to the CoordinatorListCreateAPIView
        response = self.client.post(self.coordinator_list_create_url, data, format='json')

        # Assert the response (should be forbidden)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Coordinator.objects.count(), 1)  # Only one coordinator should exist