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


class Bairro(models.Model):
    id = models.ForeignKey('DivisaoAdministrativa', db_column='id', primary_key=True)
    bairro = models.CharField(max_length=-1)
    municipio = models.ForeignKey('Municipio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bairro'


class Comercial(models.Model):
    id = models.ForeignKey('UnidadeEdificada', db_column='id', primary_key=True)
    reservado = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comercial'


class Cruzamento(models.Model):
    id = models.BigIntegerField(primary_key=True)
    intersecao_dois = models.ForeignKey('Logradouro')
    intersecao_um = models.ForeignKey('Logradouro')
    identificacao = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'cruzamento'


class Distrito(models.Model):
    id = models.ForeignKey('DivisaoAdministrativa', db_column='id', primary_key=True)
    distrito = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'distrito'


class DivisaoAdministrativa(models.Model):
    id = models.BigIntegerField(primary_key=True)
    municipio = models.ForeignKey('Municipio')
    nome = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'divisao_administrativa'


class Estado(models.Model):
    id = models.BigIntegerField(primary_key=True)
    abreviacao = models.CharField(max_length=-1)
    estado = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'estado'


class EstadoMunicipio(models.Model):
    estado_municipio = models.ForeignKey(Estado, blank=True, null=True)
    municipio = models.ForeignKey('Municipio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_municipio'


class FaceDaQuadra(models.Model):
    id = models.BigIntegerField(primary_key=True)
    quadra = models.ForeignKey('Quadra')
    face_da_quadra = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'face_da_quadra'


class FotoLote(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lote = models.ForeignKey('Lote')
    foto = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'foto_lote'


class FotoUnidadeEdificada(models.Model):
    id = models.BigIntegerField(primary_key=True)
    unidade_edificada = models.ForeignKey('UnidadeEdificada')
    foto = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'foto_unidade_edificada'


class Industrial(models.Model):
    id = models.ForeignKey('UnidadeEdificada', db_column='id', primary_key=True)
    reservado = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industrial'


class Logradouro(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tipo_logradouro = models.ForeignKey('TipoLogradouro')
    logradouro = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'logradouro'


class Lote(models.Model):
    id = models.BigIntegerField(primary_key=True)
    bairro = models.ForeignKey(Bairro)
    area_lote = models.FloatField()
    delimitacao_frontal = models.CharField(max_length=-1)
    pedologia = models.CharField(max_length=-1)
    situacao = models.CharField(max_length=-1)
    topografia = models.CharField(max_length=-1)
    valor_venal = models.FloatField()
    zeragem_de_quadrra = models.CharField(max_length=-1)
    identificacao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lote'


class Municipio(models.Model):
    id = models.BigIntegerField(primary_key=True)
    estado = models.ForeignKey(Estado)
    municipio = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'municipio'


class Quadra(models.Model):
    id = models.BigIntegerField(primary_key=True)
    setor = models.ForeignKey('Setor')
    quadra = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quadra'


class Residencial(models.Model):
    id = models.ForeignKey('UnidadeEdificada', db_column='id', primary_key=True)
    reservado = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'residencial'


class Setor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    distrito = models.ForeignKey(Distrito)
    setor = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setor'


class Testada(models.Model):
    id = models.BigIntegerField(primary_key=True)
    face_de_quadra = models.ForeignKey(FaceDaQuadra)
    lote = models.ForeignKey(Lote)
    trecho_de_logradouro = models.ForeignKey('TrechoDeLogradouro')
    testada = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testada'


class TipoLogradouro(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tipo_logradouro = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'tipo_logradouro'


class TipoLogradouroLogradouro(models.Model):
    tipo_logradouro_logradouro = models.ForeignKey(TipoLogradouro, blank=True, null=True)
    logradouro = models.ForeignKey(Logradouro, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_logradouro_logradouro'


class TrechoDeLogradouro(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cruzamento = models.ForeignKey(Cruzamento)
    logradouro = models.ForeignKey(Logradouro)
    cep = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'trecho_de_logradouro'


class UnidadeEdificada(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lote = models.ForeignKey(Lote)
    area_edificada = models.FloatField()
    area_total_construida = models.FloatField()
    identificacao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidade_edificada'
