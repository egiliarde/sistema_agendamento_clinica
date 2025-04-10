from django.db import models
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome
    
class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    servico = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.cliente} - {self.data} as {self.horario}"
    
    
    
    

# Create your models here.
