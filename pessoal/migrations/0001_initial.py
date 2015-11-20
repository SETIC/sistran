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
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('numero_contrato', models.CharField(max_length=255)),
                ('vigencia_contrato', models.CharField(null=True, max_length=255, blank=True)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField()),
                ('valor_limite', models.FloatField()),
                ('produto', models.CharField(max_length=255)),
                ('saldo_restante', models.FloatField(null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'aditivo',
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('contato', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': '"cadastro_unico_pessoal"."contato"',
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('numero_contrato', models.CharField(max_length=255)),
                ('vigencia_contrato', models.CharField(null=True, max_length=255, blank=True)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField()),
                ('valor_limite', models.FloatField()),
                ('produto', models.CharField(max_length=255)),
                ('saldo_restante', models.FloatField(null=True, blank=True)),
                ('aditivo_vigente', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'contrato',
            },
        ),
        migrations.CreateModel(
            name='DadosBancarios',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('banco_agencia', models.CharField(max_length=255)),
                ('banco_conta', models.CharField(max_length=255)),
                ('banco_nome', models.CharField(max_length=255)),
                ('banco_operacao', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': '"cadastro_unico_pessoal"."dados_bancarios"',
            },
        ),
        migrations.CreateModel(
            name='DetemPropriedade',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField(null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': '"cadastro_unico_pessoal"."detem_propriedade"',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(verbose_name='Nome Completo', max_length=255)),
                ('data_de_nascimento', models.DateField(null=True, blank=True)),
                ('cpf_cnpj', models.CharField(verbose_name='CPF', null=True, max_length=30, blank=True, unique=True)),
                ('escid', models.IntegerField(null=True, blank=True)),
                ('status', models.CharField(max_length=255, choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')])),
                ('esc_id_destino', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': '"cadastro_unico_pessoal"."pessoa"',
            },
        ),
        migrations.CreateModel(
            name='Reside',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('numero', models.CharField(null=True, max_length=20, blank=True)),
                ('complemento', models.CharField(null=True, max_length=300, blank=True)),
                ('cep', models.CharField(null=True, max_length=9, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': '"cadastro_unico_pessoal"."reside"',
            },
        ),
        migrations.CreateModel(
            name='TipoContato',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('tipo_contato', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'managed': False,
                'db_table': '"cadastro_unico_pessoal"."tipo_contato"',
            },
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, primary_key=True, to='pessoal.Pessoa')),
                ('cor', models.CharField(null=True, max_length=255, blank=True)),
                ('foto', models.CharField(null=True, max_length=255, blank=True)),
                ('grau_de_instrucao', models.CharField(null=True, max_length=255, blank=True)),
                ('necessidades_especiais', models.CharField(null=True, max_length=255, blank=True)),
                ('rc_data_do_registro', models.DateField(null=True, blank=True)),
                ('rc_folha_do_livro', models.CharField(null=True, max_length=255, blank=True)),
                ('rc_nome_do_cartorio', models.CharField(null=True, max_length=255, blank=True)),
                ('rc_nome_do_livro', models.CharField(null=True, max_length=255, blank=True)),
                ('rc_numero', models.CharField(null=True, max_length=255, blank=True)),
                ('religiao', models.CharField(null=True, max_length=255, blank=True)),
                ('sexo', models.CharField(max_length=255, choices=[('MASCULINO', 'Masculino'), ('FEMININO', 'Feminino')])),
                ('tipo_sanguineo', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': '"cadastro_unico_pessoal"."pessoa_fisica"',
            },
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, primary_key=True, to='pessoal.Pessoa')),
                ('inscricao_estadual', models.CharField(null=True, max_length=255, blank=True)),
                ('razao_social', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'managed': False,
                'db_table': '"cadastro_unico_pessoal"."pessoa_juridica"',
            },
        ),
        migrations.CreateModel(
            name='Cidadao',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, primary_key=True, to='pessoal.PessoaFisica')),
                ('cm_categoria', models.CharField(null=True, max_length=255, blank=True)),
                ('cm_data_de_emissao', models.DateField(null=True, blank=True)),
                ('cm_numero', models.CharField(null=True, max_length=255, blank=True)),
                ('ct_data_de_emissao', models.DateField(null=True, blank=True)),
                ('ct_numero', models.CharField(null=True, max_length=255, blank=True)),
                ('ct_serie', models.CharField(null=True, max_length=255, blank=True)),
                ('estado_civil', models.CharField(verbose_name='Estado Civil', max_length=255, choices=[('SOLTEIRO', 'Solteiro(ª)'), ('CASADO', 'Casado(ª)'), ('SEPARADO', 'Separado(ª)'), ('DIVORCIADO', 'Divorciado(ª)'), ('VIÚVO', 'Viúvo(ª)')])),
                ('nacionalidade', models.CharField(null=True, max_length=255, blank=True)),
                ('naturalidade', models.CharField(null=True, max_length=255, blank=True)),
                ('profissao', models.CharField(null=True, max_length=255, blank=True)),
                ('rg_data_de_emissao', models.DateField(verbose_name='Data de Emissão do RG')),
                ('rg_numero', models.IntegerField(verbose_name='Número do RG')),
                ('rg_orgao_expeditor', models.CharField(verbose_name='Órgão Expedidor do RG', max_length=255)),
                ('te_numero', models.BigIntegerField(verbose_name='numero Título de Eleitor', blank=True, null=True)),
                ('te_secao', models.IntegerField(verbose_name='Seção Título de Eleitor', blank=True, null=True)),
                ('te_zona', models.IntegerField(verbose_name='Zona Título de Eleitor', blank=True, null=True)),
                ('num_registro_cnh', models.BigIntegerField(verbose_name='Número do Registro da CNH', blank=True, null=True)),
                ('validade_cnh', models.DateField()),
                ('categoria_cnh', models.CharField(verbose_name='Categoria da CNH', max_length=255, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('AB', 'AB'), ('AC', 'AC'), ('AD', 'AD'), ('AE', 'AE'), ('ACC', 'ACC')])),
            ],
            options={
                'managed': False,
                'db_table': '"cadastro_unico_pessoal"."cidadao"',
            },
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, primary_key=True, to='pessoal.PessoaJuridica')),
                ('reservado', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'editora',
            },
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, primary_key=True, to='pessoal.PessoaJuridica')),
                ('inep_da_escola', models.CharField(max_length=255)),
                ('latitude', models.CharField(null=True, max_length=255, blank=True)),
                ('longitude', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'escola',
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, primary_key=True, to='pessoal.PessoaJuridica')),
                ('reservado', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'fornecedor',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, primary_key=True, to='pessoal.PessoaFisica')),
                ('prontuario', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': '"cadastro_unico_pessoal"."paciente"',
            },
        ),
        migrations.CreateModel(
            name='Prefeitura',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, primary_key=True, to='pessoal.PessoaJuridica')),
                ('brasao', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'prefeitura',
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, primary_key=True, to='pessoal.Cidadao')),
                ('numero_de_inscricao', models.CharField(null=True, max_length=255, blank=True, unique=True)),
            ],
            options={
                'managed': False,
                'db_table': '"cadastro_unico_pessoal"."aluno"',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, primary_key=True, to='pessoal.Cidadao')),
                ('carga_horaria', models.CharField(max_length=255)),
                ('data_de_admissao', models.DateField(null=True, blank=True)),
                ('data_de_demissao', models.DateField(null=True, blank=True)),
                ('inss', models.CharField(null=True, max_length=255, blank=True)),
                ('matricula', models.CharField(max_length=255, unique=True)),
                ('ativo', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': '"cadastro_unico_pessoal"."funcionario"',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, primary_key=True, to='pessoal.Funcionario')),
                ('identificacao', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'professor',
            },
        ),
    ]
