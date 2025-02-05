from django.db import models
from api_room.models import IOTObject
from django.contrib.auth.models import User

# Create your models here.
class Log(models.Model):
    iotObject = models.OneToOneField(IOTObject, on_delete = models.RESTRICT)
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    date = models.DateField()