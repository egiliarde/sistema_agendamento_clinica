from django.shortcuts import render, redirect
from .forms import AgendamentoForm
from .models import Agendamento

def novo_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm()
        
    return render(request, 'agenda/novo.html', {'form': form})

def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all().order_by('data')
    return render(request, 'agenda/lista_agendamentos.html', {'agendamentos': agendamentos})
