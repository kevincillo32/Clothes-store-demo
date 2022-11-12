from django.shortcuts import render
from .models import *

# Create your views here.

# Web pages

def index(request):
    return render(request, 'index.html')  
def camisas(request):
    return render(request, 'camisas.html')
def balones(request):
    return render(request,'balones.html')
def gorras(request):
    return render(request, 'gorras.html')
def sudaderas(request):
    return render(request, 'sudaderas.html')
def zapatos(request):
    return render(request, 'zapatos.html')
def mochilas(request):
    return render(request, 'mochilas.html')


