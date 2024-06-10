#Importamos el modulo path para los deplazamientos entre secciones
from django.urls import path
from inicio import views

#Generamos el urlpatterns con las vistas que queremos que tome el orden es 
#urlpatterns=['Contexto(Vacio)',views.NombreFuncionGeneradora,name='Nombre referenciador a esa vista']
urlpatterns=[
    path('',views.index_render,name='index')
]

