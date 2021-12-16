from django.urls import path
from AppTecno import views

urlpatterns = [

path('inicio', views.inicio),
path('laptops',views.laptops),

]
