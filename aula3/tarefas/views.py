from django.shortcuts import render


# Create your views here.
def index(request):
    tasks = ["foo", "bar", "baz"]
    return render(request, 'tarefas/index.html', {'tasks': tasks})

def adicionar(request):
    return render(request, 'tarefas/adicionar.html')
