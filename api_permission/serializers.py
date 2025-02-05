from rest_framework import serializers
from .models import Coordinator, Admin, Common, ActorUser, Service

class ActorUserSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ActorUser
        fields = ['id', 'user', 'role']


class CoordinatorSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Coordinator
        fields = ['id', 'user']


class AdminSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Admin
        fields = ['id', 'user']


class CommonSerializer(serializers.ModelSerializer):
    user= serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Common
        fields = ['id', 'user']


class ServiceSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Service
        fields = ['id', 'user']
