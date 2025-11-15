from django.db import models
from django.contrib.auth.models import User

class Alunos(models.Model):
    dono = models.ForeignKey(User , on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    nascimento = models.DateField()
    cpf_or_rg = models.CharField(max_length=20 , blank=True , null= True)
    celular =models.CharField(max_length=20, blank=True, null=True)
    data_vencimento = models.DateField()

    def __str__(self):
        return self.nome
