from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(reques):
    return HttpResponse("<h1>Inicio</h1>")