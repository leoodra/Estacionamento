#coding:utf-8
from django import forms
from models import Carro,Cliente,Vaga

class CarroForm(forms.ModelForm):
   class Meta:
       model = Carro
       fields = ['Marca','Modelo','Placa']


class ClienteForm(forms.ModelForm):
   class Meta:
       model = Cliente
       fields = ['Nome','Sexo','CPF','Telefone','Cidade','Carro']


class VagaForm(forms.ModelForm):
   class Meta:
       model = Vaga
       fields = ['Vaga','Cliente','Carro']

