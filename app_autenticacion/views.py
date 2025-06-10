from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

def autenticacion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            usuario = authenticate(request, username=username, password=password)
            
            if usuario is not None:
                login(request, usuario)  
                
                if usuario.rol == "ADMIN_EVENTO":
                    return redirect('panel_administrador')

                elif usuario.rol == "CANDIDATO":
                    return redirect('panel_candidato')
                
            else:
                return HttpResponse("Credenciales inválidas. Por favor, intente de nuevo.")

    return render(request, 'app_autenticacion/autenticacion.html')
