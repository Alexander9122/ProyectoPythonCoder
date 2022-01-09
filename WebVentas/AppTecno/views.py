from django.db.models.fields import NullBooleanField
from django.shortcuts import render
from django.http import HttpResponse
from AppTecno.models import *
from AppTecno.forms import *

# Create your views here.
def tecnologia(request):

    return render (request, 'AppTecno/tecnologia.html')

def laptopRegistro(request):

    if request.method == "POST":

        formularioLaptop = LaptopsFormulario(request.POST)

        if formularioLaptop.is_valid():

            informacion = formularioLaptop.cleaned_data
 
            laptopInsta = Laptops(  marca       = informacion["marca"], 
                                    pulgadas    = informacion["pulgadas"], 
                                    procesador  = informacion["procesador"], 
                                    ram         = informacion["ram"], 
                                    precio      = informacion["precio"])            

            laptopInsta.save() 

            laptops = Laptops.objects.all() 

            contexto = {"laptops":laptops}

            return render(request, "AppTecno/leerLaptops.html", contexto)


    else:

        formularioLaptop = LaptopsFormulario()

    return render(request, 'AppTecno/laptopRegistro.html', {"formularioLaptop":formularioLaptop})

def leerLaptops (request):
    
    laptops = Laptops.objects.all()

    contexto = {"laptops":laptops}

    return render (request, "AppTecno/leerLaptops.html", contexto)

def eliminaLaptop (request, numero_para_borrar):

    laptopBorrar = Laptops.objects.get(id=numero_para_borrar)
    laptopBorrar.delete()

    laptops = Laptops.objects.all() 

    contexto = {"laptops":laptops}

    return render(request, "AppTecno/leerLaptops.html", contexto)

def modificarLaptop(request, numero_para_editar):

    laptop = Laptops.objects.get(id=numero_para_editar)

    if request.method == "POST":

        formularioLaptop = LaptopsFormulario(request.POST)

        if formularioLaptop.is_valid():

            informacion = formularioLaptop.cleaned_data
 
            laptop.marca       = informacion["marca"] 
            laptop.pulgadas    = informacion["pulgadas"] 
            laptop.procesador  = informacion["procesador"] 
            laptop.ram         = informacion["ram"] 
            laptop.precio      = informacion["precio"]            

            laptop.save() 

            laptops = Laptops.objects.all() 

            contexto = {"laptops":laptops}

            return render(request, "AppTecno/leerLaptops.html", contexto)


    else:

        formularioLaptop = LaptopsFormulario(initial={"marca":laptop.marca, "pulgadas":laptop.pulgadas, "procesador":laptop.procesador, "ram":laptop.ram, "precio":laptop.precio})

    return render(request, 'AppTecno/modificarLaptop.html', {"formularioLaptop":formularioLaptop, "numero_para_editar":numero_para_editar})

def buscarLaptop(request):

    if request.GET["marca"]:

        marca = request.GET["marca"]
        
        laptops = Laptops.objects.filter(marca__icontains = marca)

        contexto = {"laptops":laptops}

    else:

        laptops = Laptops.objects.all() 

        contexto = {"laptops":laptops}

    return render(request, "AppTecno/leerLaptops.html", contexto)


def celularesRegistro(request):

    if request.method == "POST":

        formularioCelular = CelularesFormulario(request.POST)

        if formularioCelular.is_valid():

            informacion = formularioCelular.cleaned_data
 
            celularInsta = Celulares(   marca           = informacion["marca"], 
                                        compania        = informacion["compania"], 
                                        conectividad    = informacion["conectividad"], 
                                        memoria         = informacion["memoria"], 
                                        precio          = informacion["precio"])            

            celularInsta.save() 

            celulares = Celulares.objects.all() 

            contexto = {"celulares":celulares}

            return render(request, "AppTecno/leerCelulares.html", contexto)

    else:

        formularioCelular = CelularesFormulario()

    return render(request, 'AppTecno/celularesRegistro.html', {"formularioCelular":formularioCelular})


def leerCelulares (request):
    
    celulares = Celulares.objects.all()

    contexto = {"celulares":celulares}

    return render (request, "AppTecno/leerCelulares.html", contexto)

def eliminaCelular (request, numero_para_borrar):

    celularBorrar = Celulares.objects.get(id=numero_para_borrar)
    celularBorrar.delete()

    celulares = Celulares.objects.all() 

    contexto = {"celulares":celulares}

    return render(request, "AppTecno/leerCelulares.html", contexto)

def buscarCelular(request):

    if request.GET["marca"]:

        marca = request.GET["marca"]
        
        celulares = Celulares.objects.filter(marca__icontains = marca)

        contexto = {"celulares":celulares}

    else:

        celulares = Celulares.objects.all() 

        contexto = {"celulares":celulares}

    return render(request, "AppTecno/leerCelulares.html", contexto)

def televisoresRegistro(request):

    if request.method == "POST":

        formularioTelevisores = TelevisoresFormulario(request.POST)

        if formularioTelevisores.is_valid():

            informacion = formularioTelevisores.cleaned_data
 
            televisorInsta = Televisores(   marca       = informacion["marca"], 
                                            pulgadas    = informacion["pulgadas"], 
                                            resolusion  = informacion["resolusion"], 
                                            precio      = informacion["precio"])            

            televisorInsta.save() 

            televisores = Televisores.objects.all() 

            contexto = {"televisores":televisores}

            return render(request, "AppTecno/leerTelevisores.html", contexto)

    else:

        formularioTelevisores = TelevisoresFormulario()

    return render(request, 'AppTecno/televisoresRegistro.html', {"formularioTelevisores":formularioTelevisores})
    
def leerTelevisores (request):
    
    televisores = Televisores.objects.all()

    contexto = {"televisores":televisores}

    return render (request, "AppTecno/leerTelevisores.html", contexto)

def eliminaTelevisor (request, numero_para_borrar):

    televisorBorrar = Televisores.objects.get(id=numero_para_borrar)
    televisorBorrar.delete()

    televisores = Televisores.objects.all() 

    contexto = {"televisores":televisores}

    return render(request, "AppTecno/leerTelevisores.html", contexto)

def buscarTelevisor(request):

    if request.GET["marca"]:

        marca = request.GET["marca"]
        
        televisores = Televisores.objects.filter(marca__icontains = marca)

        contexto = {"televisores":televisores}

    else:

        televisores = Televisores.objects.all() 

        contexto = {"televisores":televisores}

    return render(request, "AppTecno/leerTelevisores.html", contexto)
