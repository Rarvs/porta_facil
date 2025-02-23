from django.urls import path
from .views import listar_logs, abrir_porta, fechar_porta

urlpatterns = [
    path('logs/', listar_logs, name="listar_logs"),
    path('portas/<int:porta_id>/abrir/', abrir_porta, name="abrir_porta"),
    path('portas/<int:porta_id>/fechar/', fechar_porta, name="fechar_porta"),
]
