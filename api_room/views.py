from rest_framework import generics
from django.shortcuts import render

from django.db.models import Q

from .models import Room, Department, IOTObject
from .serializers import RoomSerializer, RoomSimpleSerializerWithAdmin, DepartmentSerializer, IOTObjectSerializer
from api_permission.permissions import *

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# Create your views here.
class ListRoomAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsSecurity]

class ListObjectAPIView(generics.ListAPIView):
    queryset = IOTObject.objects.all()
    serializer_class = IOTObjectSerializer
    permission_classes = [IsAuthenticated]

class RoomRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_url_kwarg = 'id'


class ListRoomWithAccessAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RoomSimpleSerializerWithAdmin

    def get_queryset(self):
        user = self.request.user
        # if Coordinator.objects.filter(user=user):
        #    return Room.objects.filter(department__coordinators__user=user)
        
        return Room.objects.filter(admin__user=user) | Room.objects.filter(users__user=user) | Room.objects.filter(department__coordinators__user=user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().distinct()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ListDepartmentAPIView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]