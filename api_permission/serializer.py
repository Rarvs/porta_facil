from rest_framework import serializers
from .models import Coordinator, Admin, Common

class ActorUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorUser
        fields = ['id', 'user', 'role']


class CoordinatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinator
        fields = ['id', 'user']


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'user']


class CommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Common
        fields = ['id', 'user']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'user']
