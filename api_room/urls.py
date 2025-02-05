from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ListRoomAPIView.as_view(), name='listar todas as salas')
]