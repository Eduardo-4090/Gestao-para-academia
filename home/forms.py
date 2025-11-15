from django import forms
from.models import Alunos

class AlunoForms(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = ['nome' ,'sobrenome', 'nascimento','cpf_or_rg'
                  ,'celular','data_vencimento']
        widgets = {
            'nome': forms.TextInput(attrs={'class':'nome'}),
            'sobrenome':forms.TextInput(attrs={'class':'sobrenome'}),
            'nascimento': forms.DateInput(attrs={'class':'nascimento', 'type':'date'},format='%Y-%m-%d'),
            'celular':forms.TextInput(attrs={'class': 'celular'}),
            'cpf_or_rg': forms.TextInput(attrs={'class':'cpf_rg'}),
            'data_vencimento':forms.DateInput(attrs={'class':'vencimento', 'type':'date'}, format='%Y-%m-%d')
            }
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'nascimento':'Data de Nascimento',
            'cpf_or_rg':'CPF ou RG',
            'celular':'Número de Celular',
            'data_vencimento':'Data de Vencimento'
        }