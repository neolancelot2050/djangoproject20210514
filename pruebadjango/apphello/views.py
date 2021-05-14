from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"apphello/index.html")

def olivo(request):
    return HttpResponse("Hello, Olivo")

def saludar(request, nombre):
    #return HttpResponse(f"Hello {nombre.capitalize()}")
    return render(request,"apphello/saludar.html",{"nombre":nombre.capitalize() })    