import json

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from saludo.application.services.saludar_service import SaludarService
from saludo.domain.persona import Persona

servicio = SaludarService()

@require_POST
def saludar(request):
    try:
        datos = json.loads(request.body)
        name = datos["name"]
    except (json.JSONDecodeError, KeyError):
        return JsonResponse({"error": "Envía un JSON con el campo 'name'"}, status=400)

    mensaje = servicio.saludar(Persona(name=name))
    return JsonResponse({"mensaje": mensaje})
