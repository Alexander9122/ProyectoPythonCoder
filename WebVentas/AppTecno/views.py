from abc import abstractproperty
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):

    return render (request, 'AppTecno/inicio.html')

def laptops(request):

    return render(request, 'AppTecno/laptops.html')

def celulares(request):

    return render(request, 'AppTecno/celulares.html')

def televisores(request):

    return render(request, 'AppTecno/televisores.html')