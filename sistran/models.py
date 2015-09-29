 # -*- coding: utf8 -*-
from __future__ import unicode_literals
from django.db import models
from pessoal.models import *

class Anexo(models.Model):
    id = models.AutoField(primary_key=True)
    cidadao = models.ForeignKey('pessoal.Cidadao')
    nome_documento = models.CharField(max_length=255)
    caminho_anexo = models.FileField()# verificar com .FileField

class Proprietario(models.Model):
    id = models.OneToOneField('pessoal.Cidadao', primary_key=True)
    num_cnh = models.IntegerField(max_length=255, null=False, blank=False, verbose_name="Numero da CNH")
    cat_cnh = models.IntegerField(max_length=255, null=False, blank=False, verbose_name="Categoria da CNH")

    def __str__(self):
        return self.id.id.id.nome

class Motorista(models.Model):
    id = models.OneToOneField('pessoal.Cidadao', primary_key=True)
    num_cnh = models.IntegerField(max_length=255, null=False , blank=False, verbose_name="Numero da CNH")
    CATEGORIA_CHOICES = (("A", "A"), ("B","B"), ("C","C"), ("D","D"), ("E","E"), ("AB","AB"), ("AC","AC"),("AD","AD"),("AE","AE"), ("ACC", "ACC"))
    cat_cnh = models.CharField(max_length=255, choices=CATEGORIA_CHOICES, verbose_name="Categoria da CNH")

    def __str__(self):
        return self.id.id.id.nome

class Cobrador(models.Model):
	id = models.OneToOneField('pessoal.Cidadao', primary_key=True)

class Veiculo(models.Model):
    id = models.AutoField(primary_key=True)
    id_proprietario = models.ForeignKey('Proprietario', verbose_name='Proprietário do Veículo')
    data_posse = models.DateField(auto_now=True)
    TIPO_CONCESSAO_CHOICES = (("taxi","Táxi"), ("alternativo","Alternativo"), ("escolar","Escolar"), ("frete","Frete"))
    tipo_concessao = models.CharField(max_length=20, choices=TIPO_CONCESSAO_CHOICES, verbose_name='Tipo do Veículo')
    marca_modelo = models.CharField(max_length=255, null = False, verbose_name='Marca/Modelo do Veículo')
    ano = models.DateField(verbose_name='Ano do Veículo')
    cor = models.CharField(max_length=255, blank=False, verbose_name='Cor do Veículo')
    chassi = models.CharField(max_length=255, blank=False, verbose_name='Chassi do Veículo')
    qnt_passageiros = models.IntegerField(verbose_name='Quant. de Passageiros')
    qnt_portas = models.IntegerField(blank=False, verbose_name='Quant. de Portas')
    placa = models.CharField(max_length=8, blank = False, verbose_name='Placa do Veículo')
    motorista = models.BooleanField(verbose_name='Prorpietário é Motorista desse Veículo?')
    #obs: o proprietário pode ser também o motorista de um veículo
    #O QUE É CATEGORIA????
    CATEGORIA_CHOICES = (("oficial","Oficial"), ("representacao_diplomatica","Representação Diplomática"), ("particular","Particular"), ("aluguel","Aluguel"), ("aprendizagem","Aprendizagem"))
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, verbose_name='Categoria do Veículo')

	#essa classe é importate haja vista que precisaremos manter um históricos de todos os proprietários
	#que um veículo já teve desde o início.
	#Considerando que um veículo so pode ter apenas 1 dono por vez então essa regra de negócio deverá ser
	#feira via código!

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

#também é importante pelo mesmo motivo da classe anterior, precisamos tê-la para manter o histórico de motoritas
# em cada veículo cadastrado no sistema

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

#essa classe armazenará cada item analisado em uma vistória, como farol, parachoque, velocímetro...
#isso evitará problemas caso novos itens surjam após a finalização da ferramenta
class VistoriaItem(models.Model):
	id = models.BigIntegerField(primary_key=True)
	nome_item = models.CharField(max_length=255)

class Vistoria(models.Model):
	id = models.AutoField(primary_key=True)
	veiculo = models.ForeignKey('Veiculo')
	data = models.DateField(blank= False, null = False)
	#estudar se esse campo é realmetne util, haja vista que temos o status (aprovado ou reprovado de cada item em cada vistoria)
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
