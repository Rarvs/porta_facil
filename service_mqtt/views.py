from django.http import JsonResponse
from .mqtt_client_handler import get_mqtt_client

mqtt_client = get_mqtt_client()

def teste(objects, command):
    print(objects, command)

# View para abrir a porta
def abrir_porta_view(request):
    try:
        # mqtt.abrir_porta()
        mqtt_client.publish_message("porta/comando", "OPEN")
        return JsonResponse({"status": "Comando 'OPEN' enviado com sucesso"})
    except Exception as e:
        return JsonResponse({"status": "Erro", "error": str(e)})

# View para consultar o status da porta
def status_porta_view(request):
    try:
        status = mqtt_client.get_last_message("porta/status")
        return JsonResponse({"status": status})
    except Exception as e:
        return JsonResponse({"status": "Erro", "error": str(e)})
