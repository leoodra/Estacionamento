#coding:utf-8
from django.db import models

# Create your models here.

SEXO = [
         ('F','Feminino'),
         ('M','Masculino')
]


class Carro(models.Model):
       Marca = models.CharField('Marca',max_length=30)
       Modelo = models.CharField('Modelo',max_length=30)
       Placa = models.CharField('Placa',max_length=8,unique=True)
       
       def __unicode__(self):
               return"%s - %s" % (self.Marca,self.Placa)
 

class Cliente(models.Model):
       Nome = models.CharField('Nome',max_length=57, unique=True)
       Sexo = models.CharField('Sexo',max_length=1,choices=SEXO)
       CPF= models.CharField('CPF',max_length=14,unique=True)
       DtNas = models.DateField('Data Nascimento',null=True)
       Telefone = models.CharField('Telefone',max_length=13,null=True)
       Cidade = models.CharField('Cidade',max_length=30,null=True)
       Carro = models.ForeignKey(Carro,verbose_name="Carro")
        
       def __unicode__(self):
               return "%s - %s" % (self.Nome,self.Carro.Marca)


class Vaga(models.Model):
       Vaga = models.CharField('Vaga',max_length='3', unique=True)
       Cliente = models.ForeignKey(Cliente, verbose_name="Cliente")
       Carro = models.ForeignKey(Carro,verbose_name="Carro")

       def __unicode__(self):
           return "%s - %s - %s" % (self.Vaga,self.Cliente.Nome,self.Carro.Marca)









        
