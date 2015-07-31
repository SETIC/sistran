from __future__ import unicode_literals

from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.


class Assessoria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    organismo = models.ForeignKey('Organismo')
    assessoria = models.CharField(max_length=255)
    contato_telefonico = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'assessoria'


class Cargo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    celula = models.ForeignKey('Celula')
    cargo = models.CharField(max_length=255)
    moeda_salario = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargo'


class Celula(models.Model):
    id = models.BigIntegerField(primary_key=True)
    organismo = models.ForeignKey('Organismo')
    celula = models.CharField(max_length=255)
    contato_telefonico = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'celula'


class Lotacao(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cargo = models.ForeignKey(Cargo)
    funcionario = models.ForeignKey('Funcionario')
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True)
    situacao = models.CharField(max_length=255)
    funcao = models.CharField(max_length=255)
    vinculo = models.CharField(max_length=255, blank=True, null=True)
    turno = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lotacao'


class Organismo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    prefeitura = models.ForeignKey('Prefeitura')
    contato_telefonico = models.CharField(max_length=255)
    organismo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'organismo'


class Bairro(models.Model):
    id = models.ForeignKey('DivisaoAdministrativa', db_column='id', primary_key=True)
    bairro = models.CharField(max_length=255)
    municipio = models.ForeignKey('Municipio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bairro'


class Comercial(models.Model):
    id = models.ForeignKey('UnidadeEdificada', db_column='id', primary_key=True)
    reservado = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comercial'


class Logradouro(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tipo_logradouro = models.ForeignKey('TipoLogradouro')
    logradouro = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'logradouro'


class Distrito(models.Model):
    id = models.ForeignKey('DivisaoAdministrativa', db_column='id', primary_key=True)
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
    id = models.ForeignKey('UnidadeEdificada', db_column='id', primary_key=True)
    reservado = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industrial'





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
    estado = models.ForeignKey(Estado)
    municipio = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'municipio'


class Quadra(models.Model):
    id = models.BigIntegerField(primary_key=True)
    setor = models.ForeignKey('Setor')
    quadra = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quadra'


class Residencial(models.Model):
    id = models.ForeignKey('UnidadeEdificada', db_column='id', primary_key=True)
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

    class Meta:
        managed = False
        db_table = 'tipo_logradouro'


class TipoLogradouroLogradouro(models.Model):
    tipo_logradouro_logradouro = models.ForeignKey(TipoLogradouro, blank=True, null=True)
    logradouro = models.ForeignKey(Logradouro, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_logradouro_logradouro'


class UnidadeEdificada(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lote = models.ForeignKey(Lote)
    area_edificada = models.FloatField()
    area_total_construida = models.FloatField()
    identificacao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidade_edificada'

class Aditivo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contrato = models.ForeignKey('Contrato')
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


class Aluno(models.Model):
    id = models.ForeignKey('Cidadao', db_column='id', primary_key=True)
    numero_de_inscricao = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aluno'


class Cidadao(models.Model):
    id = models.ForeignKey('PessoaFisica', db_column='id', primary_key=True)
    cm_categoria = models.CharField(max_length=255, blank=True, null=True)
    cm_data_de_emissao = models.DateField(blank=True, null=True)
    cm_numero = models.CharField(max_length=255, blank=True, null=True)
    ct_data_de_emissao = models.DateField(blank=True, null=True)
    ct_numero = models.CharField(max_length=255, blank=True, null=True)
    ct_serie = models.CharField(max_length=255, blank=True, null=True)
    estado_civil = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=255, blank=True, null=True)
    naturalidade = models.CharField(max_length=255, blank=True, null=True)
    profissao = models.CharField(max_length=255, blank=True, null=True)
    rg_data_de_emissao = models.DateField(blank=True, null=True)
    rg_numero = models.CharField(max_length=255, blank=True, null=True)
    rg_orgao_expeditor = models.CharField(max_length=255, blank=True, null=True)
    te_numero = models.CharField(max_length=255, blank=True, null=True)
    te_secao = models.CharField(max_length=255, blank=True, null=True)
    te_zona = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cidadao'


class Contato(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pessoa = models.ForeignKey('Pessoa')
    tipo_contato = models.ForeignKey('TipoContato')
    contato = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'contato'


class Contrato(models.Model):
    id = models.BigIntegerField(primary_key=True)
    organismo = models.ForeignKey('Organismo')
    fornecedor = models.ForeignKey('Fornecedor')
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


class DetemPropriedade(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cidadao = models.ForeignKey(Cidadao)
    unidade_edificada = models.ForeignKey('UnidadeEdificada')
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detem_propriedade'


class Editora(models.Model):
    id = models.ForeignKey('PessoaJuridica', db_column='id', primary_key=True)
    reservado = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'editora'


class Escola(models.Model):
    id = models.ForeignKey('PessoaJuridica', db_column='id', primary_key=True)
    inep_da_escola = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escola'


class Fornecedor(models.Model):
    id = models.ForeignKey('PessoaJuridica', db_column='id', primary_key=True)
    reservado = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fornecedor'


class Funcionario(models.Model):
    id = models.ForeignKey(Cidadao, db_column='id', primary_key=True)
    carga_horaria = models.CharField(max_length=255)
    data_de_admissao = models.DateField(blank=True, null=True)
    data_de_demissao = models.DateField(blank=True, null=True)
    inss = models.CharField(max_length=255, blank=True, null=True)
    matricula = models.CharField(unique=True, max_length=255)
    ativo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funcionario'


class Motorista(models.Model):
    id = models.ForeignKey(Funcionario, db_column='id', primary_key=True)
    categoria = models.CharField(max_length=255)
    cnh = models.CharField(max_length=255)
    cnh_validade = models.DateField()
    data_de_emissao = models.DateField()

    class Meta:
        managed = False
        db_table = 'motorista'


class Paciente(models.Model):
    id = models.ForeignKey('PessoaFisica', db_column='id', primary_key=True)
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
    id = models.BigIntegerField(primary_key=True)
    data_de_nascimento = models.DateField(blank=True, null=True)
    nome = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(unique=True, max_length=30, blank=True, null=True)
    escid = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255)
    esc_id_destino = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"cadastro_unico_pessoal"."pessoa"'

    def __str__(self):
        return self.nome


class PessoaFisica(models.Model):
    id = models.ForeignKey(Pessoa, db_column='id', primary_key=True)
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
    sexo = models.CharField(max_length=255)
    tipo_sanguineo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"cadastro_unico_pessoal"."pessoa_fisica"'

    def __str__(self):
        return self.id.nome


class PessoaJuridica(models.Model):
    id = models.ForeignKey(Pessoa, db_column='id', primary_key=True)
    inscricao_estadual = models.CharField(max_length=255, blank=True, null=True)
    razao_social = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'pessoa_juridica'


class Prefeitura(models.Model):
    id = models.ForeignKey(PessoaJuridica, db_column='id', primary_key=True)
    brasao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prefeitura'


class Professor(models.Model):
    id = models.ForeignKey(Funcionario, db_column='id', primary_key=True)
    identificacao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professor'


class Reside(models.Model):
    id = models.BigIntegerField(primary_key=True)
    bairro = models.ForeignKey('Bairro')
    logradouro = models.ForeignKey('Logradouro')
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
