from urllib import request
from django.shortcuts import render,redirect
from .models import Cronometro, Pomodoro
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


#def cronometro(request):
    if request.method =="POST":
        form = CronometroForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return render(request,'cronometroactivo.html')
    else:
        form=CronometroForm()
    return render(request,'cronometro.html',{'form':form})

def cronometro(request):
    context = {}
    return render(request, 'cronometro.html', context)


def cronometroactivo(request, pk):
    cronometro=Cronometro.objects.get(pk=12)
    return render(request, 'cronometroactivo.html', {"cronometro":cronometro,})



