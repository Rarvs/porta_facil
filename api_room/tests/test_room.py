from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api_room.models import Room, Department, IOTObject
from api_room.serializers import (
    RoomSerializer,
    RoomSimpleSerializerWithAdmin,
    DepartmentSerializer,
    IOTObjectSerializer,
)

class RoomTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.admin_user = User.objects.create_user(
            username="adminuser", password="adminpass", is_staff=True
        )
        self.department = Department.objects.create(name="Test Department")
        self.room = Room.objects.create(name="Test Room", department=self.department)
        self.iot_object = IOTObject.objects.create(
            name="Test IOT Object", room=self.room
        )

    def test_list_all_rooms(self):
        self.client.force_authenticate(user=self.user)
        url = "api/room/listAll/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_room_by_id(self):
        self.client.force_authenticate(user=self.user)
        url = f"api/room/{self.room.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.room.name)

    def test_update_room(self):
        self.client.force_authenticate(user=self.user)
        url = f"api/room/{self.room.id}/"
        data = {"name": "Updated Room Name"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.room.refresh_from_db()
        self.assertEqual(self.room.name, "Updated Room Name")

    def test_delete_room(self):
        self.client.force_authenticate(user=self.user)
        url = f"api/room/{self.room.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Room.objects.count(), 0)

    def test_list_rooms_with_access(self):
        self.client.force_authenticate(user=self.user)
        url = "api/room/list/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_all_departments(self):
        self.client.force_authenticate(user=self.user)
        url = "api/department/listAll/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_iot_objects(self):
        self.client.force_authenticate(user=self.user)
        url = "api/objetos/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
