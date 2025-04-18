from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente', 'data', 'horario', 'servico']
widgets = {
    'data': forms.DateInput(attrs={'type': 'date'}),
    'horario': forms.TimeInput(attrs={'type': 'time'}),
}