from rest_framework import serializers
from api_auth.serializers import UserSerializer
from .models import Log

class LogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Log
        fields = ['iotObject', 'user', 'command', 'date']