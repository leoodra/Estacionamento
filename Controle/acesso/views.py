#coding:utf-8
from django.shortcuts import render, redirect, render_to_response

#from django.http import HttpResponse

from forms import CarroForm,ClienteForm,VagaForm
from models import Carro,Cliente


# Create your views here.

def home(request):
    return render_to_response('acesso/home.html', {})


def cadcarro(request):
    if request.method == 'POST':
      form = CarroForm(request.POST)
    
      if form.is_valid():
          form.save()
          return redirect('cadcarro')
    else:
       form = CarroForm()
    
    return render(request,'acesso/cadcarro.html',{'form' : form })


def cadcliente(request):
    if request.method == 'POST':
      form = ClienteForm(request.POST)
    
      if form.is_valid():
          form.save()
          return redirect('cadcliente')
    else:
       form = ClienteForm()
    
    return render(request,'acesso/cadcliente.html',{'form' : form })

def cadvaga(request):
    if request.method == 'POST':
      form = VagaForm(request.POST)
    
      if form.is_valid():
          form.save()
          return redirect('cadvaga')
    else:
       form = VagaForm()
    
    return render(request,'acesso/cadvaga.html',{'form' : form })


