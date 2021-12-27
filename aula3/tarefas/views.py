from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


class NovaTarefaForm(forms.Form):
    nome_tarefa = forms.CharField(label='Nome Tarefa', max_length=100)
    descricao = forms.CharField(label='Descrição', max_length=100)
    # prazo = forms.DateField(label='Prazo')
    prioridade = forms.IntegerField(label='Prioridade', min_value = 1, max_value = 10)


# Create your views here.
def index(request):
    if "tarefas" not in request.session:
        request.session["tarefas"] = []
    return render(request, 'tarefas/index.html', {'tarefas': request.session["tarefas"]})

def adicionar(request):
    if request.method == 'POST':
        form = NovaTarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.cleaned_data['nome_tarefa']
            request.session["tarefas"] += [tarefa]
            return HttpResponseRedirect(reverse('tarefas:index'))
        else:
            return render(request, 'tarefas/adicionar.html', {'form': form})

    return render(request, 'tarefas/adicionar.html', {'form': NovaTarefaForm()})
