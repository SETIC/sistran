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
                ('vigencia_contrato', models.CharField(blank=True, max_length=255, null=True)),
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
            name='Contato',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
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
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('numero_contrato', models.CharField(max_length=255)),
                ('vigencia_contrato', models.CharField(blank=True, max_length=255, null=True)),
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
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('banco_agencia', models.CharField(max_length=255)),
                ('banco_conta', models.CharField(max_length=255)),
                ('banco_nome', models.CharField(max_length=255)),
                ('banco_operacao', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'dados_bancarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetemPropriedade',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'detem_propriedade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parentesco',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('parentesco', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'parentesco',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('data_de_nascimento', models.DateField(blank=True, null=True)),
                ('nome', models.CharField(max_length=255)),
                ('cpf_cnpj', models.CharField(blank=True, unique=True, max_length=30, null=True)),
                ('escid', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(max_length=255)),
                ('esc_id_destino', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."pessoa"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reside',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('numero', models.CharField(blank=True, max_length=20, null=True)),
                ('complemento', models.CharField(blank=True, max_length=300, null=True)),
                ('cep', models.CharField(blank=True, max_length=9, null=True)),
            ],
            options={
                'db_table': 'reside',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoContato',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('tipo_contato', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'db_table': 'tipo_contato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='pessoal.Pessoa', serialize=False)),
                ('cor', models.CharField(blank=True, max_length=255, null=True)),
                ('foto', models.CharField(blank=True, max_length=255, null=True)),
                ('grau_de_instrucao', models.CharField(blank=True, max_length=255, null=True)),
                ('necessidades_especiais', models.CharField(blank=True, max_length=255, null=True)),
                ('rc_data_do_registro', models.DateField(blank=True, null=True)),
                ('rc_folha_do_livro', models.CharField(blank=True, max_length=255, null=True)),
                ('rc_nome_do_cartorio', models.CharField(blank=True, max_length=255, null=True)),
                ('rc_nome_do_livro', models.CharField(blank=True, max_length=255, null=True)),
                ('rc_numero', models.CharField(blank=True, max_length=255, null=True)),
                ('religiao', models.CharField(blank=True, max_length=255, null=True)),
                ('sexo', models.CharField(choices=[('MASCULINO', 'Masculino'), ('FEMININO', 'Feminino'), ('OUTRO', 'Outro')], max_length=255)),
                ('tipo_sanguineo', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."pessoa_fisica"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='pessoal.Pessoa', serialize=False)),
                ('inscricao_estadual', models.CharField(blank=True, max_length=255, null=True)),
                ('razao_social', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'db_table': 'pessoa_juridica',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cidadao',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='pessoal.PessoaFisica', serialize=False)),
                ('cm_categoria', models.CharField(blank=True, max_length=255, null=True)),
                ('cm_data_de_emissao', models.DateField(blank=True, null=True)),
                ('cm_numero', models.CharField(blank=True, max_length=255, null=True)),
                ('ct_data_de_emissao', models.DateField(blank=True, null=True)),
                ('ct_numero', models.CharField(blank=True, max_length=255, null=True)),
                ('ct_serie', models.CharField(blank=True, max_length=255, null=True)),
                ('estado_civil', models.CharField(max_length=255)),
                ('nacionalidade', models.CharField(blank=True, max_length=255, null=True)),
                ('naturalidade', models.CharField(blank=True, max_length=255, null=True)),
                ('profissao', models.CharField(blank=True, max_length=255, null=True)),
                ('rg_data_de_emissao', models.DateField(blank=True, null=True)),
                ('rg_numero', models.CharField(blank=True, max_length=255, null=True)),
                ('rg_orgao_expeditor', models.CharField(blank=True, max_length=255, null=True)),
                ('te_numero', models.CharField(blank=True, max_length=255, null=True)),
                ('te_secao', models.CharField(blank=True, max_length=255, null=True)),
                ('te_zona', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'cidadao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='pessoal.PessoaJuridica', serialize=False)),
                ('reservado', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'editora',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='pessoal.PessoaJuridica', serialize=False)),
                ('inep_da_escola', models.CharField(max_length=255)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'escola',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='pessoal.PessoaJuridica', serialize=False)),
                ('reservado', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'fornecedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='pessoal.PessoaFisica', serialize=False)),
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
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='pessoal.PessoaJuridica', serialize=False)),
                ('brasao', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'prefeitura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='pessoal.Cidadao', serialize=False)),
                ('numero_de_inscricao', models.CharField(blank=True, unique=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'aluno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='pessoal.Cidadao', serialize=False)),
                ('carga_horaria', models.CharField(max_length=255)),
                ('data_de_admissao', models.DateField(blank=True, null=True)),
                ('data_de_demissao', models.DateField(blank=True, null=True)),
                ('inss', models.CharField(blank=True, max_length=255, null=True)),
                ('matricula', models.CharField(unique=True, max_length=255)),
                ('ativo', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'funcionario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='pessoal.Funcionario', serialize=False)),
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
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='pessoal.Funcionario', serialize=False)),
                ('identificacao', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'professor',
                'managed': False,
            },
        ),
    ]
