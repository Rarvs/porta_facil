from django.db import models
from api_auth.models import *
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    coordinators = models.ManyToManyField(Coordinator)

class Room(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    departament = models.ForeignKey(Department, on_delete=models.CASCADE)
    admin = models.ManyToManyField(Admin)
    users = models.ManyToManyField(Common)
    
class IOTObject(models.Model):
    mac = models.CharField(max_length=100, unique=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)