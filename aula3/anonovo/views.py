from django.shortcuts import render
from datetime import date


# Create your views here.
def index(request):
    d = "date.today().strftime('%d/%m/%Y')"
    return render(request, 'anonovo/index.html', {"resposta": "Sim!" if d.startswith('01/01') else "Não."})
