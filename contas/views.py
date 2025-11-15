from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import perfil_user
from django.contrib import messages
from axes.handlers.proxy import AxesProxyHandler


def logar(request):
    if request.method == 'POST':
        name = request.POST.get('Usuario') 
        senha = request.POST.get('Senha')

        Nome = name.capitalize()
        
        credentials = {
            'ip_address': request.META.get('REMOTE_ADDR'), 
        }

        if AxesProxyHandler.is_locked(request, credentials): 
            messages.error(request, "Exesso de Tentativas, Tente Novamente daqui a 1 Minuto")
            return redirect('logar')
        
        user = authenticate(request, username=Nome, password=senha)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Usuário ou senha inválidos")
            return redirect('logar')

    return render(request,'logar.html')

def Novo_user(request):
    if request.method == 'POST':
        nome = request.POST.get('Usuario')
        senha = request.POST.get('Senha')
        celular = request.POST.get('celular')

        Nome = nome.capitalize()
        if User.objects.filter(username=Nome).exists():
            messages.error(request, 'Usuario já em Uso')
            return redirect('Novo_user')
        
        elif perfil_user.objects.filter(Celular=celular).exists():
            messages.error(request, 'Número já em Uso')
            return redirect('Novo_user')

        else:
            usuario = User.objects.create_user(
            username=Nome, 
            password=senha
            )
            perfil_user.objects.create(
              user=usuario,
              Celular=celular,
                )
            messages.success(request, 'Usuario Criado com Success')
            return redirect('logar')
    else:
        return render(request , 'novo_user.html')