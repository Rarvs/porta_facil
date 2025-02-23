from django.db import models
from api_room.models import IOTObject
from django.contrib.auth.models import User
from django.utils.timezone import now

class Porta(models.Model):
    nome = models.CharField(max_length=100, unique=True)  # Ex: "Porta Principal"
    status = models.BooleanField(default=False)  # False = Fechada, True = Aberta

    def __str__(self):
        return self.nome

class LogAcesso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Quem abriu
    porta = models.ForeignKey(Porta, on_delete=models.CASCADE)  # Qual porta
    horario = models.DateTimeField(default=now)  # Quando foi aberto
    sucesso = models.BooleanField(default=True)  # Se a autenticação foi aceita

    def __str__(self):
        return f"{self.usuario.username} abriu {self.porta.nome} em {self.horario}"


# Create your models here.
class Log(models.Model):
    iotObject = models.OneToOneField(IOTObject, on_delete = models.RESTRICT)
    command = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    date = models.DateField()

    def __str__(self):
        return f'{self.iotObject} - {self.command} - {self.user} - {self.date}'