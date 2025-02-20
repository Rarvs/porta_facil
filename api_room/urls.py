from django.urls import path
from .views import *

urlpatterns = [
    path('room/listAll/', ListRoomAPIView.as_view(), name='listar todas as salas'),
    path('room/list/', ListRoomWithAccessAPIView.as_view(), name='listar salas com acesso'),
    path('room/<int:id>/', RoomRetrieveUpdateDestroyAPIView.as_view(), name='lista sala pelo id'),
    path('portas/', ListObjectAPIView.as_view(), name='portas'),
    path('department/listAll/', ListDepartmentAPIView.as_view(), name='listar todos os departamentos')
]