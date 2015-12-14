from django.db import models
from demutran.pessoal.models import *

class Organismo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    prefeitura = models.ForeignKey('pessoal.Prefeitura')
    contato_telefonico = models.CharField(max_length=255)
    organismo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'organismo'


class Assessoria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    organismo = models.ForeignKey('Organismo')
    assessoria = models.CharField(max_length=255)
    contato_telefonico = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'assessoria'


class Celula(models.Model):
    id = models.BigIntegerField(primary_key=True)
    organismo = models.ForeignKey('Organismo')
    celula = models.CharField(max_length=255)
    contato_telefonico = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'celula'


class Cargo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    celula = models.ForeignKey('Celula')
    cargo = models.CharField(max_length=255)
    moeda_salario = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargo'



class Lotacao(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cargo = models.ForeignKey('Cargo')
    funcionario = models.ForeignKey('pessoal.Funcionario')
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True)
    situacao = models.CharField(max_length=255)
    funcao = models.CharField(max_length=255)
    vinculo = models.CharField(max_length=255, blank=True, null=True)
    turno = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lotacao'


