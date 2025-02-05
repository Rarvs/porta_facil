from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ActorUser(models.Model):
    class ActorUserRolesChoices(models.TextChoices):
        USUARIO_PADRAO = 'padrao'
        COORDENADOR = 'coordenador'
        ADMINISTRADOR = 'administrador'
        SERVIDOR = 'servidor'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ActorUserRolesChoices.choices, default=ActorUserRolesChoices.USUARIO_PADRAO)

class Coordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Common(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Service(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
