from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Endpoint Home")

def carreras(request):
    return HttpResponse("Endpoint Carreras")

def docentes(request):
    return HttpResponse("Endpoint Docentes")
