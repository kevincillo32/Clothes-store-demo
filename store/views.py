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
    
def mochilas(request):
    return render(request, 'mochilas.html')
    
def camisagris(request):
    return render(request, 'camisa-gris-nike.html')
    
def camisablanca(request):
    return render(request, 'camisa-blanca-nike.html')
    
def camisablanca2(request):
    return render(request, 'camisa-blanca-2-nike.html')
    
def camisanegra(request):
    return render(request, 'camisa-negra-nike.html')
    
def camisaazul(request):
    return render(request, 'camisa-azul-nike.html')
    
def camisaroja(request):
    return render(request, 'camisa-roja-nike.html') 
       
def cuenta(request):
    return render(request, 'cuenta.html')
    


