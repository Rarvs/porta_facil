from django.db import models
from api_room.models import IOTObject
from django.contrib.auth.models import User


# Create your models here.
class Log(models.Model):
    iotObject = models.OneToOneField(IOTObject, on_delete = models.RESTRICT)
    command = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    date = models.DateField()

    def __str__(self):
        return f'{self.iotObject} - {self.command} - {self.user} - {self.date}'