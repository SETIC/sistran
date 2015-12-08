 # -*- coding: utf8 -*-
from __future__ import unicode_literals
from django.db import models
from pessoal.models import *
from localizacao.models import *

class Permissao(models.Model):
    id = models.AutoField(primary_key=True)
    num_permissao = models.IntegerField(null=False, blank=False, verbose_name='Número da Permissão')
    data = models.DateField(auto_now=True)
    TIPO_CONCESSAO_CHOICES = (("TÁXI","TÁXI"), ("ALTERNATIVO","ALTERNATIVO"), ("ESCOLAR","ESCOLAR"), ("FRETE","FRETE"))
    tipo_concessao = models.CharField(max_length=20, choices=TIPO_CONCESSAO_CHOICES, verbose_name='Tipo do Veículo')

class AnexoCidadao(models.Model):
    id = models.AutoField(primary_key=True)
    cidadao = models.ForeignKey('pessoal.Cidadao')
    nome_documento = models.CharField(max_length=255)
    caminho = models.FileField()

class AnexoPermissao(models.Model):
    id = models.AutoField(primary_key=True)
    permissao = models.ForeignKey('Permissao')
    nome_documento = models.CharField(max_length=255)
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
    codigo_renavan = models.BigIntegerField(primary_key=True, verbose_name='Código Renavan')
    veiculo_proprio = models.BooleanField(default=True)
    exercicio = models.CharField(max_length=255, null=False, blank=False, verbose_name='Ano de Exercício')
    placa = models.CharField(max_length=8, blank=False, verbose_name='Placa do Veículo')
    chassi = models.CharField(max_length=255, null=False, blank=False, verbose_name='Chassi do Veículo')
    num_passageiros = models.IntegerField(verbose_name='Número de Passageiros')
    combustivel = models.CharField(max_length=255, blank=False, verbose_name='Combustível')
    MARCA_CHOICES = (("AGRALE","AGRALE"), ("ASTON MARTIN","ASTON MARTIN"), ("AUDI","AUDI"), ("BENTLEY","BENTLEY"), ("BMW","BMW"), ("CHANGAN","CHANGAN"), ("CHERY","CHERY"), ("CHEVROLET","CHEVROLET"), ("CHRYSLER","CHRYSLER"), ("CITROËN","CITROËN"), ("DODGE","DODGE"), ("EFFA","EFFA"), ("FERRARI","FERRARI"), ("FIAT","FIAT"), ("FORD","FORD"), ("GEELY","GEELY"), ("HAFEI","HAFEI"), ("HONDA","HONDA"), ("HYUNDAI","HYUNDAI"), ("IVECO","IVECO"), ("JAC MOTORS","JAC MOTORS"), ("JAGUAR","JAGUAR"), ("JEEP","JEEP"), ("JINBEI","JINBEI"), ("KIA","KIA"), ("LAMBORGHINI","LAMBORGHINI"), ("LAND ROVER","LAND ROVER"), ("LEXUS","LEXUS"), ("LIFAN","LIFAN"), ("MAHINDRA","MAHINDRA"), ("MASERATI","MASERATI"), ("MERCEDES-BENZ","MERCEDES-BENZ"), ("MG MOTORS","MG MOTORS"), ("MINI","MINI"), ("MITSUBISHI","MITSUBISHI"), ("NISSAN","NISSAN"), ("PEUGEOT","PEUGEOT"), ("PORSCHE","PORSCHE"), ("RAM","RAM"), ("RENAULT","RENAULT"), ("SMART","SMART"), ("SSANGYONG","SSANGYONG"), ("SUBARU","SUBARU"), ("SUZUKI","SUZUKI"), ("TOYOTA","TOYOTA"), ("TROLLER","TROLLER"), ("VOLKSWAGEN","VOLKSWAGEN"), ("VOLVO","VOLVO"))
    marca = models.CharField(max_length=255, choices=MARCA_CHOICES, null=False, blank=False, verbose_name='Marca')
    modelo = models.CharField(max_length=255, null=False, blank=False, verbose_name='Modelo')
    ano_fabricacao = models.CharField(max_length=255, null=False, blank=False, verbose_name='Ano de Fabricação')
    ano_modelo = models.CharField(max_length=255, null=False, blank=False, verbose_name='Ano do Modelo')
    CATEGORIA_CHOICES = (("OFICIAL","OFICIAL"), ("REPRESENTAÇÃO DIPLOMÁTICA","REPRESENTAÇÃO DIPLOMÁTICA"), ("PARTICULAR","PARTICULAR"), ("ALUGUEL","ALUGUEL"), ("APRENDIZAGEM","APRENDIZAGEM"))
    categoria = models.CharField(max_length=155, choices=CATEGORIA_CHOICES, verbose_name='Categoria')
    COR_CHOICES = (("BRANCA","BRANCA"), ("PRATA","PRATA"), ("PRETA","PRETA"), ("CINZA","CINZA"), ("VERMELHA","VERMELHA"), ("MARROM","MARROM"), ("BEGE","BEGE"), ("AZUL","AZUL"), ("VERDE","VERDE"), ("AMARELA","AMARELA"), ("DOURADA","DOURADA"))
    cor_predominante = models.CharField(max_length=255, blank=False, choices=COR_CHOICES, verbose_name='Cor Predominante')

    def __str__(self):
        return self.marca_modelo + " - " + self.placa

class PermissaoTemProprietario(models.Model):
    permissao_veiculo = models.ForeignKey('PermissaoTemVeiculo')
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
    permissao_veiculo = models.ForeignKey('PermissaoTemVeiculo')
    motorista = models.ForeignKey('Motorista')
    data_posse = models.DateField(auto_now=True)
    STATUS_CHOICE = (('ATIVO','ATIVO'),	('INATIVO','INATIVO'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)

class PermissaoTemCobrador(models.Model):
    permissao_veiculo = models.ForeignKey('PermissaoTemVeiculo')
    cobrador = models.ForeignKey('Cobrador')
    data_posse = models.DateField(auto_now=True)
    STATUS_CHOICE = (('ATIVO','ATIVO'),	('INATIVO','INATIVO'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
