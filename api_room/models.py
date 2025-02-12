from django.db import models
from api_permission.models import *
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    coordinators = models.ManyToManyField(Coordinator, related_name='departments', blank=True)

class Room(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='rooms')
    admin = models.ManyToManyField(Admin, related_name='rooms', blank=True)
    users = models.ManyToManyField(Common, related_name='rooms', blank=True)

    def __str__(self):
        return f'{self.code} - {self.name}'
    
class IOTObject(models.Model):
    status = models.CharField(max_length=50, blank=True, default="Esperando")
    mac = models.CharField(max_length=100, unique=True)
    room = models.ForeignKey(Room, on_delete=models.RESTRICT)