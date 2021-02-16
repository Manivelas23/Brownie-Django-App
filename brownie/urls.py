from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='index'),
    path("informar",views.informar,name='informar'),
    path("planificar",views.planificar,name='planificar'),
    path("decidir",views.decidir,name='decidir'),
    path("controlar",views.controlar,name='controlar'),
    path("ejecutar",views.ejecutar,name='ejecutar'),
    path("valorar",views.valorar,name='valorar'),
]

