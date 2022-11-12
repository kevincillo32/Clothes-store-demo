from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth



# Create your views here.
def login(request):
    return render(request, "login.html")

def registrarse(request):
    if request.method == ("POST"):
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        email= request.POST['email']
        password= request.POST['password']
        user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=password)
        user.save();
        print("Usuario Creado")
        redirect('/Home')
        return render(request,'registrarse.html')
    else:
        
        print("Intentalo de nuevo")
        return render(request,'registrarse.html')