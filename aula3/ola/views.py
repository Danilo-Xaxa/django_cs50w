from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "ola/index.html")

def cumprimentar(request, nome):
    return render(request, "ola/cumprimentar.html", {"nome": nome.capitalize()})
