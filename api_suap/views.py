from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import requests

suap_api_URL = 'https://suap.ifsuldeminas.edu.br/api/v2/autenticacao/token/'

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):    
    ra = request.data.get("RA")
    senha = request.data.get("senha")

    if not ra or not senha:
        return Response({"error": "RA e senha são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)
    
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "username": ra,
        "password": senha
    }

    try:
        response = requests.post(suap_api_URL, json=payload, headers=headers)
        response_data = response.json()  # Converte a resposta para JSON

        if response.status_code == 200:
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(response_data, status=response.status_code)

    except requests.exceptions.RequestException as e:
        return Response({"error": f"Erro na conexão com SUAP: {str(e)}"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
