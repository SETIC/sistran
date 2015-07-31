# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Assessoria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    organismo = models.ForeignKey('Organismo')
    assessoria = models.CharField(max_length=-1)
    contato_telefonico = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'assessoria'


class Cargo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    celula = models.ForeignKey('Celula')
    cargo = models.CharField(max_length=-1)
    moeda_salario = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargo'


class Celula(models.Model):
    id = models.BigIntegerField(primary_key=True)
    organismo = models.ForeignKey('Organismo')
    celula = models.CharField(max_length=-1)
    contato_telefonico = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'celula'


class Lotacao(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cargo = models.ForeignKey(Cargo)
    funcionario = models.ForeignKey('Funcionario')
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True)
    situacao = models.CharField(max_length=-1)
    funcao = models.CharField(max_length=255)
    vinculo = models.CharField(max_length=255, blank=True, null=True)
    turno = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lotacao'


class Organismo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    prefeitura = models.ForeignKey('Prefeitura')
    contato_telefonico = models.CharField(max_length=-1)
    organismo = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'organismo'
