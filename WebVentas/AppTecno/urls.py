from django.urls import path
from AppTecno import views

urlpatterns = [

path('tecnologia', views.tecnologia, name="Tecnologia"),
path('laptopRegistro',views.laptopRegistro, name="LaptopRegistro"),
path('leerLaptops',views.leerLaptops,name="LeerLaptops"),
path('eliminarLaptop/<numero_para_borrar>/',views.eliminaLaptop,name="EliminarLaptop"),
path('modificarLaptop/<numero_para_editar>/',views.modificarLaptop,name="ModificarLaptop"),
path('buscarLaptop/', views.buscarLaptop),
path('celularesRegistro',views.celularesRegistro, name="CelularesRegistro"),
path('leerCelulares',views.leerCelulares,name="LeerCelulares"),
path('eliminarCelular/<numero_para_borrar>/',views.eliminaCelular,name="EliminarCelular"),
path('buscarCelular/', views.buscarCelular),
path('televisoresRegistro',views.televisoresRegistro, name="TelevisoresRegistro"),
path('leerTelevisores',views.leerTelevisores,name="LeerTelevisores"),
path('eliminarTelevisor/<numero_para_borrar>/',views.eliminaTelevisor,name="EliminarTelevisor"),
path('buscarTelevisor/', views.buscarTelevisor),
]
