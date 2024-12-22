from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USUARIO_PADRAO = 'usuario'
    COORDENADOR = 'coordenador'
    ADMINISTRADOR = 'administrador'

    TIPOS_USUARIO = [
        (USUARIO_PADRAO, 'Usuário Padrão'),
        (COORDENADOR, 'Coordenador'),
        (ADMINISTRADOR, 'Administrador'),
    ]

    tipo_usuario = models.CharField(
        max_length = 15,
        choices = TIPOS_USUARIO,
        default=USUARIO_PADRAO,
    )