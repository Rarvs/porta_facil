from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Porta, LogAcesso
from django.utils.timezone import now

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_logs(request):
    logs = LogAcesso.objects.all().order_by('-horario')  # Lista em ordem decrescente
    data = [
        {
            "usuario": log.usuario.username,
            "porta": log.porta.nome,
            "horario": log.horario.strftime("%Y-%m-%d %H:%M:%S"),
            "sucesso": log.sucesso
        }
        for log in logs
    ]
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def abrir_porta(request, porta_id):
    porta = get_object_or_404(Porta, id=porta_id)
    usuario = request.user

    # Simulação de autorização (pode melhorar com autenticação real)
    autorizacao = True  # Troque isso pela verificação correta

    # Registra o log
    LogAcesso.objects.create(usuario=usuario, porta=porta, horario=now(), sucesso=autorizacao)

    if autorizacao:
        porta.status = True
        porta.save()
        return Response({"message": f"A porta {porta.nome} foi aberta"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Acesso negado"}, status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def fechar_porta(request, porta_id):
    porta = get_object_or_404(Porta, id=porta_id)
    porta.status = False
    porta.save()
    return Response({"message": f"A porta {porta.nome} foi fechada"}, status=status.HTTP_200_OK)
