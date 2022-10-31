from urllib import request
from django.shortcuts import render,redirect
from .models import Cronometro
from .forms import NewRegister, CronometroForm







def menu(request):
    return render(request,'menu.html')


def registerView(request):
    if request.method == "POST":
        form = NewRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = NewRegister()
    
    return render(request,'registration/register.html',{'form':NewRegister})


def cuestionario(request):
    return render(request,'cuestionario.html')


def cronometro(request):
    if request.method =="POST":
        form = CronometroForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return render(request,'cronometroactivo.html')
    else:
        form=CronometroForm()
    return render(request,'cronometro.html',{'form':form})


def cronometroactivo(request):
    ciclos = Cronometro.ciclos
    testudio = Cronometro.estudio
    tdescanso = Cronometro.descanso
    return render(request, 'cronometroactivo.html', {"ciclos":ciclos,"estudio":testudio,"descanso":tdescanso})



