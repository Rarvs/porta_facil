from rest_framework import generics
from django.shortcuts import render

from .models import Room
from .serializers import RoomSerializer, RoomSimpleSerializerWithAdmin
from api_permission.permissions import *

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# Create your views here.
class ListRoomAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSimpleSerializerWithAdmin
    permission_classes = [IsAuthenticated]

    # def get(sefl, request):
    #     user = request.user

    #     rooms = Room.objects.filter()
    #     serializer = RoomSerializer(rooms, many=True)
    #     return Response(serializer.data)
