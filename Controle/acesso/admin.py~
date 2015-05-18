#coding:utf-8
from django.contrib import admin
from models import Cliente
from models import Carro
from models import Vaga

# Register your models here.


class CarroAdmin(admin.ModelAdmin):
   list_display = ['Marca','Modelo','Placa']
   list_filter = ['Marca','Modelo','Placa']
   search_fields = ['Marca','Modelo','Placa']
   save_as = True
 
#class CarroInline(admin.TabularInline):
     #  model = Carro	
      # extra = 1  

class ClienteAdmin(admin.ModelAdmin):
  list_display = ['Nome','Sexo','CPF','Telefone','Cidade','Carro']
  list_filter = ['Nome']
  search_fields =['Nome']
 # inlines = [CarroInline]
  save_as = True

class VagaAdmin(admin.ModelAdmin):
  list_display = ['Vaga','Cliente','Carro']

admin.site.register(Carro,CarroAdmin)
#admin.site.register(CarroInline)
admin.site.register(Cliente,ClienteAdmin)
#class CarroAdmin(admin.ModelAdmin):
admin.site.register(Vaga,VagaAdmin)
  
