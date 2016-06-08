from django.db import models

class Bairro(models.Model):
    id = models.OneToOneField('DivisaoAdministrativa', db_column='id', primary_key=True)
    bairro = models.CharField(max_length=255)
    municipio = models.ForeignKey('Municipio', blank=True, null=True, verbose_name='Município')
    
    def __str__(self):
        return self.bairro

    class Meta:
        managed = False
        db_table = '"cadastro_unico_localizacao"."bairro"'

class Comercial(models.Model):
    id = models.OneToOneField('UnidadeEdificada', db_column='id', primary_key=True)
    reservado = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comercial'

class Distrito(models.Model):
    id = models.OneToOneField('DivisaoAdministrativa', db_column='id', primary_key=True)
    distrito = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'distrito'

class DivisaoAdministrativa(models.Model):
    id = models.BigIntegerField(primary_key=True)
    municipio = models.ForeignKey('Municipio')
    nome = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'divisao_administrativa'

class Estado(models.Model):
    id = models.BigIntegerField(primary_key=True)
    abreviacao = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)

    def __str__(self):
        return self.estado
    
    class Meta:
        managed = False
        db_table = '"cadastro_unico_localizacao"."estado"'

class EstadoMunicipio(models.Model):
    estado_municipio = models.ForeignKey(Estado, blank=True, null=True)
    municipio = models.ForeignKey('Municipio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_municipio'

class FaceDaQuadra(models.Model):
    id = models.BigIntegerField(primary_key=True)
    quadra = models.ForeignKey('Quadra')
    face_da_quadra = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'face_da_quadra'

class FotoLote(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lote = models.ForeignKey('Lote')
    foto = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'foto_lote'

class FotoUnidadeEdificada(models.Model):
    id = models.BigIntegerField(primary_key=True)
    unidade_edificada = models.ForeignKey('UnidadeEdificada')
    foto = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'foto_unidade_edificada'

class Industrial(models.Model):
    id = models.OneToOneField('UnidadeEdificada', db_column='id', primary_key=True)
    reservado = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industrial'

class Logradouro(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_logradouro = models.ForeignKey('TipoLogradouro', null=True, blank=True)
    logradouro = models.CharField(max_length=255)

    def __str__(self):
        return self.logradouro
    
    class Meta:
        managed = False
        db_table = '"cadastro_unico_localizacao"."logradouro"'

class Lote(models.Model):
    id = models.BigIntegerField(primary_key=True)
    bairro = models.ForeignKey(Bairro)
    area_lote = models.FloatField()
    delimitacao_frontal = models.CharField(max_length=255)
    pedologia = models.CharField(max_length=255)
    situacao = models.CharField(max_length=255)
    topografia = models.CharField(max_length=255)
    valor_venal = models.FloatField()
    zeragem_de_quadrra = models.CharField(max_length=255)
    identificacao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lote'

class Municipio(models.Model):
    id = models.BigIntegerField(primary_key=True)
    municipio = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado)
    
    def __str__(self):
        return self.municipio
    
    class Meta:
        managed = False
        db_table = '"cadastro_unico_localizacao"."municipio"'

class Quadra(models.Model):
    id = models.BigIntegerField(primary_key=True)
    setor = models.ForeignKey('Setor')
    quadra = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quadra'

class Residencial(models.Model):
    id = models.OneToOneField('UnidadeEdificada', db_column='id', primary_key=True)
    reservado = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'residencial'

class Setor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    distrito = models.ForeignKey(Distrito)
    setor = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setor'

class TipoLogradouro(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tipo_logradouro = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo_logradouro
    
    class Meta:
        managed = False
        db_table = '"cadastro_unico_localizacao"."tipo_logradouro"'

class TipoLogradouroLogradouro(models.Model):
    tipo_logradouro_logradouro = models.ForeignKey(TipoLogradouro, blank=True, null=True)
    logradouro = models.ForeignKey(Logradouro, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"cadastro_unico_localizacao"."tipo_logradouro_logradouro"'

class UnidadeEdificada(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lote = models.ForeignKey(Lote)
    area_edificada = models.FloatField()
    area_total_construida = models.FloatField()
    identificacao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidade_edificada'
