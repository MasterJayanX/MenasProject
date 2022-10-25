from django.template import Context, Template, loader
from django.http import HttpResponse
from django.shortcuts import render
import datetime


"""
la funcion context recibe diccionarios de los cuales se rescatan en html del modo {{llave}}
para poner tildes en el html devemos escribir &xacute; donde en x va el tilde (por ejemplo Día= D&iacute;a)
"""


def menu(request):
    return render(request, "menu.html")          #aqui tambien se le agrega un diccionario

def cronometros(request):
    doc_externo=loader.get_template("cronometros.html")
    documento=doc_externo.render({})
    return HttpResponse(documento)

def cuestionario(request):
    doc_externo=open("C:/mis cosas/ProyectosDjango/proyecto1/proyecto1/plantillas/cuestionario.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

def metodos(request):
    doc_externo=open("C:/mis cosas/ProyectosDjango/proyecto1/proyecto1/plantillas/metodos.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

def planificacion(request):
    doc_externo=open("C:/mis cosas/ProyectosDjango/proyecto1/proyecto1/plantillas/planificacion.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)








"""
def fecha(request):
    fecha=datetime.datetime.now()
    documento="fecha y horas actuales %s" % fecha
    return HttpResponse(documento) 

"""