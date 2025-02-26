from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Log

from api_room.models import *
from service_mqtt import views as mqtt

# Create your views here.
@permission_classes([IsAuthenticated])
class CommandView(APIView):
    def get(self, request, *args, **kwargs):
        param_department = self.kwargs.get('department')
        param_room = self.kwargs.get('room')
        param_object = self.kwargs.get('object')
        param_command = self.kwargs.get('command')
        user = request.user
    
        try:
            room = Room.objects.get(
                code = param_room,
                department__code = param_department,
                iotobjects__mac = param_object,
            )
        except Room.DoesNotExist:
            return Response({'result':'Sala não existe'}, status=status.HTTP_404_NOT_FOUND)


        if not room.users.filter(id=user.id).exists():
            return Response({'result':'Usuário não possui acesso a esta sala'}, status=status.HTTP_403_FORBIDDEN)
    
        try:
            mqtt.teste(room, param_command)
            iot = IOTObject.objects.get(mac=param_object)
            Log.objects.create(iotObject = iot, command = param_command, user = user)
            return Response({'result':'Comando executado com sucesso'})
        except Exception as e:
            return Response({'result':'Não foi possível executar o commando', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)