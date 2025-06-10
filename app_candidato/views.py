from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from app_usuarios.models import Evaluacion


Usuario = get_user_model()


def es_candidato(user):
    return user.rol == Usuario.Roles.CANDIDATO or user.is_superuser

# Create your views here.
login_required
@user_passes_test(es_candidato)
def panel_candidato(request):
    usuario = request.user  # Suponiendo que el usuario está autenticado

    return render(request, 'app_candidato/panel_candidato.html', {'usuario': usuario})


@login_required
@user_passes_test(es_candidato)
def realizar_evaluacion(request):
    if request.method == 'POST':
        pass

    return render(request, 'app_candidato/realizar_evaluacion.html')


@login_required
@user_passes_test(es_candidato)
def realizar_evaluacion(request):
    preguntas = Evaluacion.objects.all()
    if request.method == 'POST':
        respuestas_usuario = {}
        puntaje = 0
        for pregunta in preguntas:
            respuesta = request.POST.get(f'pregunta_{pregunta.id}')
            if respuesta and int(respuesta) + 1 == pregunta.respuesta_correcta:
                puntaje += 1
            respuestas_usuario[pregunta.id] = respuesta
        messages.success(request, f'Obtuviste {puntaje} de {preguntas.count()} respuestas correctas.')
        return redirect('panel_candidato')  # o donde esté el template que editamos 
    return render(request, 'app_candidato/realizar_evaluacion.html', {'preguntas': preguntas})