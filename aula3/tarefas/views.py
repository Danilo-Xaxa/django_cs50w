from django.shortcuts import render
from django import forms


tarefas = ["foo", "bar", "baz"]

class NovaTarefaForm(forms.Form):
    nome_tarefa = forms.CharField(label='Nome Tarefa', max_length=100)
    descricao = forms.CharField(label='Descrição', max_length=100)
    # prazo = forms.DateField(label='Prazo')
    prioridade = forms.IntegerField(label='Prioridade', min_value = 1, max_value = 10)


# Create your views here.
def index(request):
    return render(request, 'tarefas/index.html', {'tarefas': tarefas})

def adicionar(request):
    if request.method == 'POST':
        form = NovaTarefaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['nome_tarefa'])
            tarefas.append(form.cleaned_data['nome_tarefa'])
            return render(request, 'tarefas/index.html', {'tarefas': tarefas})
        else:
            return render(request, 'tarefas/adicionar.html', {'form': form})

    return render(request, 'tarefas/adicionar.html', {'form': NovaTarefaForm()})
