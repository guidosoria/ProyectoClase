from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def crea_curso(req, nombre, camada):
    
    nuevo_curso = Curso(nombre=nombre, camada=camada)
    nuevo_curso.save()
    
    return HttpResponse(f"""
        <p>Curso: {nuevo_curso.nombre} - Camada: {nuevo_curso.camada} creado con éxito!</p>
    """)
    
def lista_cursos(req):

    lista = Curso.objects.all()
    
    return render(req, "lista_cursos.html", {"lista_cursos" : lista})

def inicio(req):
    
    return HttpResponse("Vista de inicio")

def cursos(req):
    
    return HttpResponse("Vista de cursos")

def profesores(req):
    
    return HttpResponse("Vista de profesores")

def estudiantes(req):
    
    return HttpResponse("Vista de estudiantes")

def entregables(req):
    
    return HttpResponse("Vista de inicio")
