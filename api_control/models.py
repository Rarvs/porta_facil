from django.db import models
from api_room.models import IOTObject
from django.contrib.auth.models import User


# Create your models here.
class Log(models.Model):
    iotObject = models.ForeignKey(IOTObject, on_delete = models.RESTRICT, related_name='log')
    command = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.date}: {self.user} - {self.command} - {self.iotObject} - {self.iotObject.room.code}'