from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib import messages

Usuario = get_user_model()

def es_admin(user):
    return user.rol == Usuario.Roles.ADMIN_EVENTO or user.is_superuser

@login_required
@user_passes_test(es_admin)
def panel_administrador(request):
    usuario = request.user  # Suponiendo que el usuario está autenticado
    candidatos = Usuario.objects.filter(rol=Usuario.Roles.CANDIDATO)
    return render(request, 'app_administrador/panel_administrador.html', {'candidatos': candidatos, 'usuario': usuario})

@login_required
@user_passes_test(es_admin)
def crear_candidato(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        documento = request.POST.get('documento_identidad')
        institucion = request.POST.get('institucion')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Usuario.objects.filter(username=username).exists():
            messages.error(request, 'Ya existe un usuario con ese nombre de usuario.')
        else:
            usuario = Usuario.objects.create_user(
                username=username,
                password=password,
                email=email,
                nombre=nombre,
                documento_identidad=documento,
                institucion=institucion,
                rol=Usuario.Roles.CANDIDATO
            )
            messages.success(request, 'Candidato creado exitosamente.')
            return redirect('panel_administrador')  # Ajusta esta URL según tu panel

    return render(request, 'app_administrador/crear_usuario.html')