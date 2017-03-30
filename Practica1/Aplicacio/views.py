from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404

from django.template import Context
from django.template.loader import get_template

from Aplicacio.models import Pelicula, Personatge, Relacions

from time import sleep

# Create your views here.


def foo(request):
    return HttpResponse("Hello World!")


def pelicules(request):
    # Utilitzarem una planteilla prefixada per construir la pagina
    template = get_template("dashboard_movies.html")
    pelicules = Pelicula.objects.all()

    longitud = len(pelicules)

    variables = Context({
        "username": "Dani",
        "author": "Luis Barcenas",
        "pelicules": pelicules,
        "longitud": longitud
    })
    page = template.render(variables)
    return HttpResponse(page)


def personatges(request, id_pelicula):
    template = get_template("dashboard_characters.html")
    print id_pelicula
    
    relacions = Relacions.objects.filter(id_pelicula=id_pelicula)
    
    personatges = []
    for relacio in relacions:
        id_personatge = relacio.id_personatge
        personatge = Personatge.objects.filter(id=id_personatge)
        personatges += personatge

    # personatges = Personatge.objects.filter(id_pelicula=id_pelicula)
    longitud = len(personatges)
    print longitud
    print personatges
    
    # sleep(60)

    variables = Context({
        "username": "Dani",
        "author": "Luis Barcenas",
        "personatges": personatges,
        "longitud": longitud
    })

    page = template.render(variables)
    return HttpResponse(page)
