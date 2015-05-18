# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Marca', models.CharField(max_length=30, verbose_name=b'Marca')),
                ('Modelo', models.CharField(max_length=30, verbose_name=b'Modelo')),
                ('Placa', models.CharField(unique=True, max_length=8, verbose_name=b'Placa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(unique=True, max_length=57, verbose_name=b'Nome')),
                ('Sexo', models.CharField(max_length=1, verbose_name=b'Sexo', choices=[(b'F', b'Feminino'), (b'M', b'Masculino')])),
                ('CPF', models.CharField(unique=True, max_length=14, verbose_name=b'CPF')),
                ('DtNas', models.DateField(null=True, verbose_name=b'Data Nascimento')),
                ('Telefone', models.CharField(max_length=13, null=True, verbose_name=b'Telefone')),
                ('Cidade', models.CharField(max_length=30, null=True, verbose_name=b'Cidade')),
                ('Carro', models.ForeignKey(verbose_name=b'Carro', to='acesso.Carro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Vaga', models.CharField(unique=True, max_length=b'3', verbose_name=b'Vaga')),
                ('Carro', models.ForeignKey(verbose_name=b'Carro', to='acesso.Carro')),
                ('Cliente', models.ForeignKey(verbose_name=b'Cliente', to='acesso.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
