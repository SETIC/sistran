from __future__ import unicode_literals

from django.db import models

from pessoal.models import *


class Anexo(models.Model):
    id = models.AutoField(primary_key=True)
    cidadao = models.ForeignKey('pessoal.Cidadao')
    nome_documento = models.CharField(max_length=255)
    caminho_anexo = models.FileField()# verificar com .FileField
    
class Proprietario(models.Model):
	id = models.ForeignKey('pessoal.Cidadao', primary_key=True)
	num_cnh = models.CharField(max_length=255, null=False, blank=False)
	cat_cnh = models.CharField(max_length=255, null=False, blank=False)
	 

class Motorista(models.Model):
	id = models.ForeignKey('pessoal.Cidadao', primary_key=True)
	num_cnh = models.CharField(max_length=255, null=False , blank=False)
	cat_cnh = models.CharField(max_length=255, null=False, blank=False)



class Cobrador(models.Model):
	id = models.ForeignKey('pessoal.Cidadao', primary_key=True)



class Veiculo(models.Model):
	id = models.AutoField(primary_key=True)
	id_proprietario = models.ForeignKey('Proprietario')
	data_posse = models.DateField(auto_now=True)
	##ESTUDAR LINHA A BAIXO
	TIPO_CONCESSAO_CHOICES = (
		("taxi","Táxi"),
		("alternativo","Alternativo"),
		("escolar","Escolar"),
		("frete","Frete"),
		)
	tipo_concessao = models.CharField(max_length=20, choices=TIPO_CONCESSAO_CHOICES)
	marca_modelo = CharField(max_length=255, null = False)
	ano = models.DateField()
	cor = models.CharField(max_length=255, blank=False)
	chassi = models.IntegerField(blank=False)
	qnt_passageiros = models.IntegerField()
	qnt_portas = models.IntegerField(blank=False)
	placa = models.CharField(max_length=8, blank = False)
	motorista = models.BooleanField()#obs: o proprietário pode ser também o motorista de um veículo
	#O QUE É CATEGORIA????
	categoria = models.CharField(max_length=255,blank=False,null=False)

'''
class ProprietarioTemVeiculo(models.Model):
	id_proprietario = models.ForeignKey('Proprietario')	
	id_veiculo = models.ForeignKey('Veiculo')
	data_posse = models.DateField(auto_now=True)
	#estudar status possíveis para relação de proprietário e um veículo
	STATUS_CHOICE = (
		('Ativo','Ativo'),
		('Repassado','Repassado'),
		('Cancelado','Cancelado'),
		)
	status = models.CharField(max_length=10, choices=STATUS_CHOICE)
	motorista = models.BooleanField()#obs: o proprietário pode ser também o motorista de um veículo
'''
class VeiculoTemMotorista(models.Model):
	id_motorista = models.ForeignKey('Motorista')	
	id_veiculo = models.ForeignKey('Veiculo')
	data_posse = models.DateField(auto_now=True)
	STATUS_CHOICE = (
		('Ativo','Ativo'),
		('Inativo','Inativo'),
		)
	status = models.CharField(max_length=10, choices=STATUS_CHOICE)


class VeiculoTemCobrador(models.Model):
	id_cobrador = models.ForeignKey('Cobrador')	
	id_veiculo = models.ForeignKey('Veiculo')
	data_posse = models.DateField(auto_now=True)
	STATUS_CHOICE = (
		('Ativo','Ativo'),
		('Inativo','Inativo'),
		)
	status = models.CharField(max_length=10, choices=STATUS_CHOICE)



class VistoriaItem(models.Model):
	id = models.BigIntegerField(primary_key=True)
	nome_item = models.CharField(max_length=255)	



class Vistoria(models.Model):
	id = models.AutoField(primary_key=True)
	veiculo = models.ForeignKey('Veiculo')
	data = models.DateField(blank= False, null = False)
	aprovado = models.BooleanField()#verificar se campos bolleans recebem algum argumento
	observacao = models.CharField(max_length=255)


class VistoriaTemVistoriaItem(models.Model):
	id_vistoria_item = models.ForeignKey('VistoriaItem')
	id_vistoria = models.ForeignKey('Vistoria')
	STATUS_VISTORIA_ITEM_CHOICES = (
		("Aprovado","Aprovado"),
		("Reprovado","Reprovado")
		)
	status = models.CharField(max_length=20,choices=STATUS_VISTORIA_ITEM_CHOICES)


class Reclamacao(models.Model):
	id = models.BigIntegerField(primary_key=True)
	veiculo = models.ForeignKey('Veiculo')
	descricao = models.CharField(max_length=255, null = False)	
	data_hora = models.DateTimeField(blank = False, null = False)


