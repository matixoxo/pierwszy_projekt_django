from django.shortcuts import render
from django.http import HttpResponse
from .models import Ksiazki, Wydawnictwo, Kategoria
# Create your views here.
def index(request):
    kategorie = Kategoria.objects.all()
    wydawnictwa = Wydawnictwo.objects.all()
    dane = {'kategorie': kategorie,
            'wydawnictwa': wydawnictwa
            }
    return render(request, 'strona.html', dane)

def wydawnictwo(request, id):
    zapytanie = Wydawnictwo.objects.get(pk=id)
    return HttpResponse(zapytanie.nazwa)

def kategoria(request, id):
    kategoria = Kategoria.objects.get(pk=id)
    ksiazka_kat = Ksiazki.objects.filter(kategoria = kategoria)
    kategorie = Kategoria.objects.all()
    dane = {
        'kategoria': kategoria,
        'ksiazka_kat': ksiazka_kat,
        'kategorie': kategorie
    }
    return render(request, 'kategoria.html', dane)

def ksiazka(request, id):
    ksiazka = Ksiazki.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    wydawnictwa = Wydawnictwo.objects.all()
    dane = {'ksiazka': ksiazka,
            'kategorie': kategorie,
            'wydawnictwa': wydawnictwa
            }
    return render(request, 'ksiazka.html', dane)