 # -*- coding: utf8 -*-
from __future__ import unicode_literals
from django.db import models
from pessoal.models import *

class Permissao(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField(null=False, blank=False)
    data = models.DateField(auto_now=False)
    TIPO_CONCESSAO_CHOICES = (("TÁXI","TÁXI"), ("ALTERNATIVO","ALTERNATIVO"), ("ESCOLAR","ESCOLAR"), ("FRETE","FRETE"))
    tipo_concessao = models.CharField(max_length=20, choices=TIPO_CONCESSAO_CHOICES, verbose_name='Tipo do Veículo')
    permissionario = models.ForeignKey('Proprietario')
    veiculo = models.ForeignKey('Veiculo')

class Anexo(models.Model):
    id = models.AutoField(primary_key=True)
    permissao = models.ForeignKey('Permissao')
    nome = models.CharField(max_length=255)
    caminho = models.FileField()
    
class Proprietario(models.Model):
    id = models.OneToOneField('pessoal.Cidadao', primary_key=True)

    def __str__(self):
        return self.id.id.id.nome

class Motorista(models.Model):
    id = models.OneToOneField('pessoal.Cidadao', primary_key=True)

    def __str__(self):
        return self.id.id.id.nome

class Cobrador(models.Model):
    id = models.OneToOneField('pessoal.Cidadao', primary_key=True)
    
    def __str__(self):
        return self.id.id.id.nome

class Veiculo(models.Model):
    codigo_renavan = models.BigIntegerField(primary_key=True)
    veiculo_proprio = models.BooleanField(default=True)
    exercicio = models.DateField(auto_now=False)
    proprietario = models.ForeignKey('Proprietario', verbose_name='Proprietário')
    placa = models.CharField(max_length=8, blank=False, verbose_name='Placa do Veículo')
    chassi = models.CharField(max_length=255, blank=False, verbose_name='Chassi do Veículo')
    num_passageiros = models.IntegerField(verbose_name='Número de Passageiros')
    combustivel = models.CharField(max_length=255, blank=False, verbose_name='Combustível')
    marca_modelo = models.CharField(max_length=255, blank=False, verbose_name='Marca/Modelo')
    ano_fabricacao = models.DateField(auto_now=False)
    CATEGORIA_CHOICES = (("OFICIAL","OFICIAL"), ("REPRESENTAÇÃO DIPLOMÁTICA","REPRESENTAÇÃO DIPLOMÁTICA"), ("PARTICULAR","PARTICULAR"), ("ALUGUEL","ALUGUEL"), ("APRENDIZAGEM","APRENDIZAGEM"))
    categoria = models.CharField(max_length=155, choices=CATEGORIA_CHOICES, verbose_name='Categoria')
    cor_predominante = models.CharField(max_length=255, blank=False, verbose_name='Cor Predominante')

    def __str__(self):
        return self.marca_modelo + " - " + self.placa

class PermissaoTemProprietario(models.Model):
    permissao = models.ForeignKey('Permissao')
    proprietario = models.ForeignKey('Proprietario')
    data_posse = models.DateField(auto_now=True)
    STATUS_CHOICE = (('ATIVO','ATIVO'),	('TRANSFERIDO','TRANSFERIDO'), ('INATIVO','INATIVO'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    
class PermissaoTemVeiculo(models.Model):
    permissao = models.ForeignKey('Permissao')
    veiculo = models.ForeignKey('Veiculo')
    data_posse = models.DateField(auto_now=True)
    STATUS_CHOICE = (('ATIVO','ATIVO'),	('TRANSFERIDO','TRANSFERIDO'), ('INATIVO','INATIVO'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)

class PermissaoTemMotorista(models.Model):
	permissao = models.ForeignKey('Permissao')
	motorista = models.ForeignKey('Motorista')
	data_posse = models.DateField(auto_now=True)
	STATUS_CHOICE = (('ATIVO','ATIVO'),	('INATIVO','INATIVO'))
	status = models.CharField(max_length=10, choices=STATUS_CHOICE)

class PermissaoTemCobrador(models.Model):
	permissao = models.ForeignKey('Permissao')
	cobrador = models.ForeignKey('Cobrador')
	data_posse = models.DateField(auto_now=True)
	STATUS_CHOICE = (('ATIVO','ATIVO'),	('INATIVO','INATIVO'))
	status = models.CharField(max_length=10, choices=STATUS_CHOICE)