from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Log

from api_room.models import *
from service_mqtt import views as mqtt

# Create your views here.
class CommandView(APIView):
    def get(self, request, *args, **kwargs):
        param_department = self.kwargs.get('department')
        param_room = self.kwargs.get('room')
        param_object = self.kwargs.get('object')
        param_command = self.kwargs.get('command')
        user = request.user
        
        room = Room.objects.filter(code=param_room) & Room.objects.filter(department__code=param_department) & Room.objects.filter(iotobjects__mac=param_object)
        
        print(room)
        print(user)
        
        if room:
            try:
                mqtt.teste(room, param_command)
                iot = IOTObject.objects.get(mac=param_object)
                Log.objects.create(iotObject = iot, command = param_command, user = user)
                return Response({'result':'Comando executado com sucesso'})
            except Exception as e:
                return Response({'result':'Não foi possível executar o commando', 'error': str(e)})
        else:
            return Response({'result':'sala inexistente'})