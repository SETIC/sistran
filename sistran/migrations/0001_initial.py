# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aditivo',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('numero_contrato', models.CharField(max_length=255)),
                ('vigencia_contrato', models.CharField(blank=True, null=True, max_length=255)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField()),
                ('valor_limite', models.FloatField()),
                ('produto', models.CharField(max_length=255)),
                ('saldo_restante', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'aditivo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Assessoria',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('assessoria', models.CharField(max_length=255)),
                ('contato_telefonico', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'assessoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('cargo', models.CharField(max_length=255)),
                ('moeda_salario', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cargo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Celula',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('celula', models.CharField(max_length=255)),
                ('contato_telefonico', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'celula',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('contato', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'contato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('numero_contrato', models.CharField(max_length=255)),
                ('vigencia_contrato', models.CharField(blank=True, null=True, max_length=255)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField()),
                ('valor_limite', models.FloatField()),
                ('produto', models.CharField(max_length=255)),
                ('saldo_restante', models.FloatField(blank=True, null=True)),
                ('aditivo_vigente', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'contrato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DadosBancarios',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('banco_agencia', models.CharField(max_length=255)),
                ('banco_conta', models.CharField(max_length=255)),
                ('banco_nome', models.CharField(max_length=255)),
                ('banco_operacao', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'dados_bancarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetemPropriedade',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'detem_propriedade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DivisaoAdministrativa',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'divisao_administrativa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('abreviacao', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'estado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoMunicipio',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
            options={
                'db_table': 'estado_municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FaceDaQuadra',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('face_da_quadra', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'face_da_quadra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FotoLote',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('foto', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'foto_lote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FotoUnidadeEdificada',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('foto', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'foto_unidade_edificada',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Logradouro',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('logradouro', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'logradouro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lotacao',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField(blank=True, null=True)),
                ('situacao', models.CharField(max_length=255)),
                ('funcao', models.CharField(max_length=255)),
                ('vinculo', models.CharField(blank=True, null=True, max_length=255)),
                ('turno', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'lotacao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('area_lote', models.FloatField()),
                ('delimitacao_frontal', models.CharField(max_length=255)),
                ('pedologia', models.CharField(max_length=255)),
                ('situacao', models.CharField(max_length=255)),
                ('topografia', models.CharField(max_length=255)),
                ('valor_venal', models.FloatField()),
                ('zeragem_de_quadrra', models.CharField(max_length=255)),
                ('identificacao', models.CharField(blank=True, null=True, max_length=50)),
            ],
            options={
                'db_table': 'lote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('municipio', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Organismo',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('contato_telefonico', models.CharField(max_length=255)),
                ('organismo', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'organismo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parentesco',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('parentesco', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'parentesco',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('data_de_nascimento', models.DateField(blank=True, null=True)),
                ('nome', models.CharField(max_length=255)),
                ('cpf_cnpj', models.CharField(blank=True, unique=True, null=True, max_length=30)),
                ('escid', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(max_length=255)),
                ('esc_id_destino', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pessoa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Quadra',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('quadra', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'quadra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reside',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('numero', models.CharField(blank=True, null=True, max_length=20)),
                ('complemento', models.CharField(blank=True, null=True, max_length=300)),
                ('cep', models.CharField(blank=True, null=True, max_length=9)),
            ],
            options={
                'db_table': 'reside',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('setor', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'setor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoContato',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tipo_contato', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'db_table': 'tipo_contato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoLogradouro',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tipo_logradouro', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tipo_logradouro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoLogradouroLogradouro',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
            options={
                'db_table': 'tipo_logradouro_logradouro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UnidadeEdificada',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('area_edificada', models.FloatField()),
                ('area_total_construida', models.FloatField()),
                ('identificacao', models.CharField(blank=True, null=True, max_length=50)),
            ],
            options={
                'db_table': 'unidade_edificada',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.DivisaoAdministrativa', serialize=False)),
                ('bairro', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'bairro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comercial',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.UnidadeEdificada', serialize=False)),
                ('reservado', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'comercial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.DivisaoAdministrativa', serialize=False)),
                ('distrito', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'distrito',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Industrial',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.UnidadeEdificada', serialize=False)),
                ('reservado', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'industrial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.Pessoa', serialize=False)),
                ('cor', models.CharField(blank=True, null=True, max_length=255)),
                ('foto', models.CharField(blank=True, null=True, max_length=255)),
                ('grau_de_instrucao', models.CharField(blank=True, null=True, max_length=255)),
                ('necessidades_especiais', models.CharField(blank=True, null=True, max_length=255)),
                ('rc_data_do_registro', models.DateField(blank=True, null=True)),
                ('rc_folha_do_livro', models.CharField(blank=True, null=True, max_length=255)),
                ('rc_nome_do_cartorio', models.CharField(blank=True, null=True, max_length=255)),
                ('rc_nome_do_livro', models.CharField(blank=True, null=True, max_length=255)),
                ('rc_numero', models.CharField(blank=True, null=True, max_length=255)),
                ('religiao', models.CharField(blank=True, null=True, max_length=255)),
                ('sexo', models.CharField(max_length=255)),
                ('tipo_sanguineo', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'pessoa_fisica',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.Pessoa', serialize=False)),
                ('inscricao_estadual', models.CharField(blank=True, null=True, max_length=255)),
                ('razao_social', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'db_table': 'pessoa_juridica',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Residencial',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.UnidadeEdificada', serialize=False)),
                ('reservado', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'residencial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cidadao',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.PessoaFisica', serialize=False)),
                ('cm_categoria', models.CharField(blank=True, null=True, max_length=255)),
                ('cm_data_de_emissao', models.DateField(blank=True, null=True)),
                ('cm_numero', models.CharField(blank=True, null=True, max_length=255)),
                ('ct_data_de_emissao', models.DateField(blank=True, null=True)),
                ('ct_numero', models.CharField(blank=True, null=True, max_length=255)),
                ('ct_serie', models.CharField(blank=True, null=True, max_length=255)),
                ('estado_civil', models.CharField(max_length=255)),
                ('nacionalidade', models.CharField(blank=True, null=True, max_length=255)),
                ('naturalidade', models.CharField(blank=True, null=True, max_length=255)),
                ('profissao', models.CharField(blank=True, null=True, max_length=255)),
                ('rg_data_de_emissao', models.DateField(blank=True, null=True)),
                ('rg_numero', models.CharField(blank=True, null=True, max_length=255)),
                ('rg_orgao_expeditor', models.CharField(blank=True, null=True, max_length=255)),
                ('te_numero', models.CharField(blank=True, null=True, max_length=255)),
                ('te_secao', models.CharField(blank=True, null=True, max_length=255)),
                ('te_zona', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'cidadao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.PessoaJuridica', serialize=False)),
                ('reservado', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'editora',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.PessoaJuridica', serialize=False)),
                ('inep_da_escola', models.CharField(max_length=255)),
                ('latitude', models.CharField(blank=True, null=True, max_length=255)),
                ('longitude', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'escola',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.PessoaJuridica', serialize=False)),
                ('reservado', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'fornecedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.PessoaFisica', serialize=False)),
                ('prontuario', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'paciente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prefeitura',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.PessoaJuridica', serialize=False)),
                ('brasao', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'prefeitura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.Cidadao', serialize=False)),
                ('numero_de_inscricao', models.CharField(blank=True, unique=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'aluno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.Cidadao', serialize=False)),
                ('carga_horaria', models.CharField(max_length=255)),
                ('data_de_admissao', models.DateField(blank=True, null=True)),
                ('data_de_demissao', models.DateField(blank=True, null=True)),
                ('inss', models.CharField(blank=True, null=True, max_length=255)),
                ('matricula', models.CharField(unique=True, max_length=255)),
                ('ativo', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'funcionario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.Funcionario', serialize=False)),
                ('categoria', models.CharField(max_length=255)),
                ('cnh', models.CharField(max_length=255)),
                ('cnh_validade', models.DateField()),
                ('data_de_emissao', models.DateField()),
            ],
            options={
                'db_table': 'motorista',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='sistran.Funcionario', serialize=False)),
                ('identificacao', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'professor',
                'managed': False,
            },
        ),
    ]
