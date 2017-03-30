from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404

from django.template import Context
from django.template.loader import get_template

from Aplicacio.models import Pelicula, Personatge

# Create your views here.


def foo(request):
    return HttpResponse("Hello World!")


def pelicules(request):
    # Utilitzarem una planteilla prefixada per construir la pagina
    template = get_template("dashboard_movies.html")
    # template = get_template("dashboard2.html")
    # pelicula = Pelicula.objects.get(id=2241)
    pelicules = Pelicula.objects.all()

    longitud = len(pelicules)

    variables = Context({
        "username": "Dani",
        "author": "Luis Barcenas",
        # "pelicula": pelicula
        "pelicules": pelicules,
        "longitud": longitud
    })
    page = template.render(variables)
    return HttpResponse(page)


def personatges(request, id_pelicula):
    template = get_template("dashboard_characters.html")
    print id_pelicula

    personatges = Personatge.objects.filter(id_pelicula=id_pelicula)
    longitud = len(personatges)

    variables = Context({
        "username": "Dani",
        "author": "Luis Barcenas",
        # "pelicula": pelicula
        "personatges": personatges,
        "longitud": longitud
    })

    page = template.render(variables)
    return HttpResponse(page)
