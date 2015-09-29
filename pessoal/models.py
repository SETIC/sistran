 # -*- coding: utf8 -*-
from __future__ import unicode_literals
from django.db import models
from administracao.models import *
from localizacao.models import *

class Aluno(models.Model):
    id = models.OneToOneField('Cidadao', db_column='id', primary_key=True)
    numero_de_inscricao = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aluno'

class Contato(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pessoa = models.ForeignKey('Pessoa')
    tipo_contato = models.ForeignKey('TipoContato')
    contato = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'contato'

class DadosBancarios(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pessoa = models.ForeignKey('Pessoa')
    banco_agencia = models.CharField(max_length=255)
    banco_conta = models.CharField(max_length=255)
    banco_nome = models.CharField(max_length=255)
    banco_operacao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dados_bancarios'

class Editora(models.Model):
    id = models.OneToOneField('PessoaJuridica', db_column='id', primary_key=True)
    reservado = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'editora'

class Escola(models.Model):
    id = models.OneToOneField('PessoaJuridica', db_column='id', primary_key=True)
    inep_da_escola = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escola'

class Fornecedor(models.Model):
    id = models.OneToOneField('PessoaJuridica', db_column='id', primary_key=True)
    reservado = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fornecedor'

class Contrato(models.Model):
    id = models.BigIntegerField(primary_key=True)
    organismo = models.ForeignKey(Organismo)
    fornecedor = models.ForeignKey(Fornecedor)
    numero_contrato = models.CharField(max_length=255)
    vigencia_contrato = models.CharField(max_length=255, blank=True, null=True)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    valor_limite = models.FloatField()
    produto = models.CharField(max_length=255)
    saldo_restante = models.FloatField(blank=True, null=True)
    aditivo_vigente = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'contrato'

class Aditivo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contrato = models.ForeignKey(Contrato)
    numero_contrato = models.CharField(max_length=255)
    vigencia_contrato = models.CharField(max_length=255, blank=True, null=True)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    valor_limite = models.FloatField()
    produto = models.CharField(max_length=255)
    saldo_restante = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aditivo'

class Paciente(models.Model):
    id = models.OneToOneField('PessoaFisica', db_column='id', primary_key=True)
    prontuario = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'paciente'

class Parentesco(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pessoa_fisica = models.ForeignKey('PessoaFisica')
    parentesco = models.CharField(max_length=255, blank=True, null=True)
    pessoa = models.ForeignKey('Pessoa')

    class Meta:
        managed = False
        db_table = 'parentesco'

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, verbose_name="Nome Completo")
    data_de_nascimento = models.DateField(blank=True, null=True)
    cpf_cnpj = models.CharField(unique=True, max_length=30, blank=True, null=True, verbose_name = "CPF")
    escid = models.IntegerField(blank=True, null=True)
    STATUS_CHOICES = (('Ativo','Ativo'), ('Inativo','Inativo'))
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    esc_id_destino = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"cadastro_unico_pessoal"."pessoa"'

    def status_color(self):
        if (self.status == 'Ativo'):
            return "<i class='glyphicon glyphicon-ok-circle' style='color:green'></i>"
        else:
            return "<i class='glyphicon glyphicon-remove-circle' style='color:red'></i>"

    status_color.allow_tags = True
    status_color.short_description = "Status"

    def __str__(self):
        return self.nome

class PessoaFisica(models.Model):
    id = models.OneToOneField('Pessoa', db_column='id', primary_key=True)
    cor = models.CharField(max_length=255, blank=True, null=True)
    foto = models.CharField(max_length=255, blank=True, null=True)
    grau_de_instrucao = models.CharField(max_length=255, blank=True, null=True)
    necessidades_especiais = models.CharField(max_length=255, blank=True, null=True)
    rc_data_do_registro = models.DateField(blank=True, null=True)
    rc_folha_do_livro = models.CharField(max_length=255, blank=True, null=True)
    rc_nome_do_cartorio = models.CharField(max_length=255, blank=True, null=True)
    rc_nome_do_livro = models.CharField(max_length=255, blank=True, null=True)
    rc_numero = models.CharField(max_length=255, blank=True, null=True)
    religiao = models.CharField(max_length=255, blank=True, null=True)
    SEXO_CHOICES=(('MASCULINO','Masculino'),('FEMININO','Feminino'), ('OUTRO','Outro'))
    sexo = models.CharField(max_length=255, choices=SEXO_CHOICES)
    tipo_sanguineo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"cadastro_unico_pessoal"."pessoa_fisica"'

    def __str__(self):
        return self.id.nome

class Cidadao(models.Model):
    id = models.OneToOneField('PessoaFisica', db_column='id', primary_key=True)
    cm_categoria = models.CharField(max_length=255, blank=True, null=True)
    cm_data_de_emissao = models.DateField(blank=True, null=True)
    cm_numero = models.CharField(max_length=255, blank=True, null=True)
    ct_data_de_emissao = models.DateField(blank=True, null=True)
    ct_numero = models.CharField(max_length=255, blank=True, null=True)
    ct_serie = models.CharField(max_length=255, blank=True, null=True)
    ESTADO_CIVIL_CHOICES=(('SOLTEIRO','Solteiro'),('CASADO','Casado'), ('VIÚVO','Viúvo'), ('DIVORCIADO','Divorciado'), ('OUTRO','Outro'))
    estado_civil = models.CharField(max_length=255, verbose_name='Estado Civil', choices=ESTADO_CIVIL_CHOICES)
    nacionalidade = models.CharField(max_length=255, blank=True, null=True)
    naturalidade = models.CharField(max_length=255, blank=True, null=True)
    profissao = models.CharField(max_length=255, blank=True, null=True)
    rg_data_de_emissao = models.DateField(blank=True, null=True, verbose_name='Data de Emissão do RG')
    rg_numero = models.CharField(max_length=255, blank=True, null=True, verbose_name='Número do RG')
    rg_orgao_expeditor = models.CharField(max_length=255, blank=True, null=True, verbose_name='Órgão Exp. RG')
    te_numero = models.CharField(max_length=255, blank=True, null=True, verbose_name='Num. Título de Eleitor')
    te_secao = models.CharField(max_length=255, blank=True, null=True, verbose_name='Seção Título de Eleitor')
    te_zona = models.CharField(max_length=255, blank=True, null=True, verbose_name='Zona Título de Eleitor')

    def __str__(self):
        return self.id.id.nome

    class Meta:
        managed = False
        db_table = '"cadastro_unico_pessoal"."cidadao"'

class Funcionario(models.Model):
    id = models.OneToOneField('Cidadao', db_column='id', primary_key=True)
    carga_horaria = models.CharField(max_length=255)
    data_de_admissao = models.DateField(blank=True, null=True)
    data_de_demissao = models.DateField(blank=True, null=True)
    inss = models.CharField(max_length=255, blank=True, null=True)
    matricula = models.CharField(unique=True, max_length=255)
    ativo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.id.id.id.nome

    class Meta:
        managed = False
        db_table = '"cadastro_unico_pessoal"."funcionario"'

#class Motorista(models.Model):
 #   id = models.ForeignKey(Funcionario, db_column='id', primary_key=True)
  #  categoria = models.CharField(max_length=255)
   # cnh = models.CharField(max_length=255)
  #  cnh_validade = models.DateField()
  #  data_de_emissao = models.DateField()

   # class Meta:
   #     managed = False
   #     db_table = '"cadastro_unico_pessoal"."motorista"'

class DetemPropriedade(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cidadao = models.ForeignKey(Cidadao)
    unidade_edificada = models.ForeignKey(UnidadeEdificada)
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detem_propriedade'

class PessoaJuridica(models.Model):
    id = models.OneToOneField(Pessoa, db_column='id', primary_key=True)
    inscricao_estadual = models.CharField(max_length=255, blank=True, null=True)
    razao_social = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'pessoa_juridica'

class Prefeitura(models.Model):
    id = models.OneToOneField(PessoaJuridica, db_column='id', primary_key=True)
    brasao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prefeitura'

class Professor(models.Model):
    id = models.OneToOneField(Funcionario, db_column='id', primary_key=True)
    identificacao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professor'

class Reside(models.Model):
    id = models.BigIntegerField(primary_key=True)
    bairro = models.ForeignKey('localizacao.Bairro')
    logradouro = models.ForeignKey('localizacao.Logradouro')
    pessoa = models.ForeignKey(Pessoa)
    numero = models.CharField(max_length=20, blank=True, null=True)
    complemento = models.CharField(max_length=300, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reside'

class TipoContato(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tipo_contato = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'tipo_contato'
