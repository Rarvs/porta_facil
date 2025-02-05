from rest_framework import serializers
from django.contrib.auth.models import User
from api_permission.models import Common

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username', 'password']

    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        
        Common.objects.create(user=user)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']