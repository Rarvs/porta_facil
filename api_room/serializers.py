from rest_framework import serializers
from .models import Department, Room, IOTObject
from api_permission.serializers import *
from api_permission.models import *

class DepartmentSerializer(serializers.ModelSerializer):
    coordinators = CoordinatorSerializer(many=True, read_only=True)
    
    class Meta:
        model = Department
        fields = ['id', 'name', 'code', 'coordinators']

class RoomSerializerSimple(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id', 'code', 'name']

class IOTObjectSerializer(serializers.ModelSerializer):
    room = RoomSerializerSimple(read_only=True)

    class Meta:
        model = IOTObject
        fields = ['id', 'mac', 'room']


class RoomSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    admin = AdminSerializer(many=True, read_only=True)
    users = CommonSerializer(many=True, read_only=True)
    objects = IOTObjectSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'code', 'name', 'department', 'admin', 'users', 'objects']


class RoomSimpleSerializerWithAdmin(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    admin = AdminSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'code', 'name', 'department', 'admin']