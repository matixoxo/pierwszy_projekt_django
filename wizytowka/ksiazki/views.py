from django.shortcuts import render
from django.http import HttpResponse
from .models import Ksiazki, Wydawnictwo, Kategoria
# Create your views here.
def index(request):
    ksiazki = Ksiazki.objects.all()
    dane = {'ksiazki': ksiazki}
    return render(request, 'strona.html', dane)

def wydawnictwo(request, id):
    zapytanie = Wydawnictwo.objects.get(pk=id)
    return HttpResponse(zapytanie.nazwa)

def kategoria(request, id):
    zapytanie = Kategoria.objects.get(pk=id)
    return HttpResponse(zapytanie.nazwa)

def ksiazka(request, id):
    zapytanie = Ksiazki.objects.get(pk=id)
    napis = "<h1>" + str(zapytanie) + "</h1>" + \
            "<p>" + str(zapytanie.autor) + "</p>" + \
            "<p>" + str(zapytanie.wydawnictwo) + "</p>"
    return HttpResponse(napis)