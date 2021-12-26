from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('''
        <p><a href="/tarefas/">Tarefas</a></p>
        <p><a href="/ola/">Olá</a></p>
        <p><a href="/anonovo/">Ano novo</a></p>
        ''')