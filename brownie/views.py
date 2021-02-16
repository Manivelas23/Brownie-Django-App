from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'brownie/index.html',{'pagename':'Videos'.capitalize()})

def informar(request):
    return render(request,'brownie/informar.html',{'pagename':'Informar'.capitalize()})

def planificar(request):    
    return render(request,'brownie/planificar.html',{'pagename':'Planificar'.capitalize()})

def decidir(request):
    return render(request,'brownie/decidir.html',{'pagename':'decidir'.capitalize()})

def ejecutar(request):
    return render(request,'brownie/ejecutar.html',{'pagename':'ejecutar'.capitalize()})

def controlar(request):
    return render(request,'brownie/controlar.html',{'pagename':'controlar'.capitalize()})

def valorar(request):
    return render(request,'brownie/valorar.html',{'pagename':'valorar'.capitalize()})

