from urllib import request
from django.shortcuts import render,redirect
from .models import Resumen, Amenaza
from .forms import NewRegister, ResumenForm, AmenazaForm
from random import randint


def temporizador(request):
    return render(request,'temporizador/index.html')
    
def menu(request):
    numero=randint(0,2)
    lista_amenazas= Amenaza.objects.all()
    return render(request,'menu.html',{'numero':numero,'lista_amenazas': lista_amenazas})


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
    return render(request,'cuestionariol/cuestionario.html')

def pregunta2(request):
    return render(request,'cuestionariol/pregunta2.html')
def pregunta3(request):
    return render(request,'cuestionariol/pregunta3.html')
def pregunta4(request):
    return render(request,'cuestionariol/pregunta4.html')
def pregunta5(request):
    return render(request,'cuestionariol/pregunta5.html')
def pregunta6(request):
    return render(request,'cuestionariol/pregunta6.html')
def pregunta7(request):
    return render(request,'cuestionariol/pregunta7.html')

def pri(request):
    return render(request,'cuestionariol/pri.html')
def se(request):
    return render(request,'cuestionariol/se.html')
def deba(request):
    return render(request,'cuestionariol/deba.html')
def acti(request):
    return render(request,'cuestionariol/acti.html')
def imp(request):
    return render(request,'cuestionariol/imp.html')
def mapa(request):
    return render(request,'cuestionariol/mapa.html')
def resu(request):
    return render(request,'cuestionariol/resu.html')
def hoja(request):
    return render(request,'cuestionariol/hoja.html')
def pomodoro(request):
    return render(request,'cuestionariol/pomodoro.html')
def inv(request):
    return render(request,'cuestionariol/inv.html')
def flas(request):
    return render(request,'cuestionariol/flas.html')



def resumen(request):
    lista_resumenes= Resumen.objects.all()
    return render(request,'resumen.html',{'lista_resumenes': lista_resumenes})

def nuevoresumen(request):
    if request.method=="POST":
        form = ResumenForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.usuario = request.user.username
            instance.save()
            return redirect('resumen')
    else:
        form=ResumenForm()
    return render(request, 'nuevoresumen.html',{
        'form':form
    })

def ver_resumen(request, pk):
    datos = Resumen.objects.get(pk=pk)
    return render(request, 'ver_resumen.html', {
        'datos':datos
    })

def borrar_resumen(request, pk):
    if request.method == "POST":
        datos = Resumen.objects.get(pk=pk)
        datos.delete()
    return redirect('resumen')

def nueva_amenaza(request):
    if request.method=="POST":
        form = AmenazaForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.usuario = request.user.username
            instance.save()
            return redirect('menu')
    else:
        form=AmenazaForm()
    return render(request, 'nueva_amenaza.html',{
        'form':form
    })

def borrar_amenaza(request, pk):
    if request.method == "POST":
        datos = Amenaza.objects.get(pk=pk)
        datos.delete()
    return redirect('menu')
