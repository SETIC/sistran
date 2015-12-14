# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0001_initial'),
        ('localizacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aditivo',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
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
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('contato', models.CharField(max_length=255)),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."contato"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('numero_contrato', models.CharField(max_length=255)),
                ('vigencia_contrato', models.CharField(blank=True, null=True, max_length=255)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField()),
                ('valor_limite', models.FloatField()),
                ('produto', models.CharField(max_length=255)),
                ('saldo_restante', models.FloatField(blank=True, null=True)),
                ('aditivo_vigente', models.CharField(max_length=255)),
                ('organismo', models.ForeignKey(to='administracao.Organismo')),
            ],
            options={
                'db_table': 'contrato',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DadosBancarios',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('banco_agencia', models.CharField(max_length=255)),
                ('banco_conta', models.CharField(max_length=255)),
                ('banco_nome', models.CharField(max_length=255)),
                ('banco_operacao', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."dados_bancarios"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DetemPropriedade',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField(blank=True, null=True)),
                ('unidade_edificada', models.ForeignKey(to='localizacao.UnidadeEdificada')),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."detem_propriedade"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome Completo')),
                ('cpf_cnpj', models.CharField(blank=True, null=True, verbose_name='CPF', max_length=30, unique=True)),
                ('data_de_nascimento', models.DateField(blank=True, null=True)),
                ('escid', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(max_length=255, choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')])),
                ('esc_id_destino', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."pessoa"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Reside',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=255, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, null=True, max_length=300)),
                ('cep', models.CharField(blank=True, null=True, max_length=9, verbose_name='CEP')),
                ('bairro', models.ForeignKey(to='localizacao.Bairro')),
                ('logradouro', models.ForeignKey(to='localizacao.Logradouro')),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."reside"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoContato',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('tipo_contato', models.CharField(unique=True, verbose_name='Tipo do Contato', max_length=255, choices=[('TELEFONE', 'TELEFONE'), ('CELULAR', 'CELULAR'), ('EMAIL', 'EMAIL')])),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."tipo_contato"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, to='pessoal.Pessoa', primary_key=True)),
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
                ('sexo', models.CharField(max_length=255, choices=[('MASCULINO', 'MASCULINO'), ('FEMININO', 'FEMININO')])),
                ('tipo_sanguineo', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."pessoa_fisica"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, to='pessoal.Pessoa', primary_key=True)),
                ('inscricao_estadual', models.CharField(blank=True, null=True, max_length=255)),
                ('razao_social', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."pessoa_juridica"',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='reside',
            name='pessoa',
            field=models.ForeignKey(to='pessoal.Pessoa'),
        ),
        migrations.AddField(
            model_name='dadosbancarios',
            name='pessoa',
            field=models.ForeignKey(to='pessoal.Pessoa'),
        ),
        migrations.AddField(
            model_name='contato',
            name='pessoa',
            field=models.ForeignKey(to='pessoal.Pessoa'),
        ),
        migrations.AddField(
            model_name='contato',
            name='tipo_contato',
            field=models.ForeignKey(to='pessoal.TipoContato'),
        ),
        migrations.AddField(
            model_name='aditivo',
            name='contrato',
            field=models.ForeignKey(to='pessoal.Contrato'),
        ),
        migrations.CreateModel(
            name='Cidadao',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, to='pessoal.PessoaFisica', primary_key=True)),
                ('cm_categoria', models.CharField(blank=True, null=True, max_length=255)),
                ('cm_data_de_emissao', models.DateField(blank=True, null=True)),
                ('cm_numero', models.CharField(blank=True, null=True, max_length=255)),
                ('ct_data_de_emissao', models.DateField(blank=True, null=True)),
                ('ct_numero', models.CharField(blank=True, null=True, max_length=255)),
                ('ct_serie', models.CharField(blank=True, null=True, max_length=255)),
                ('estado_civil', models.CharField(verbose_name='Estado Civil', max_length=255, choices=[('SOLTEIRO(A)', 'SOLTEIRO(A)'), ('CASADO', 'CASADO(A)'), ('SEPARADO', 'SEPARADO(A)'), ('DIVORCIADO', 'DIVORCIADO(A)'), ('VIÚVO', 'VIÚVO(A)')])),
                ('nacionalidade', models.CharField(blank=True, null=True, max_length=255)),
                ('naturalidade', models.CharField(blank=True, null=True, max_length=255)),
                ('profissao', models.CharField(blank=True, null=True, max_length=255)),
                ('rg_data_de_emissao', models.DateField(verbose_name='Data de Emissão do RG')),
                ('rg_numero', models.IntegerField(verbose_name='RG')),
                ('rg_orgao_expeditor', models.CharField(max_length=255, verbose_name='Órgão Expedidor do RG')),
                ('te_numero', models.BigIntegerField(blank=True, null=True, verbose_name='Número Título de Eleitor')),
                ('te_secao', models.IntegerField(blank=True, null=True, verbose_name='Seção Título de Eleitor')),
                ('te_zona', models.IntegerField(blank=True, null=True, verbose_name='Zona Título de Eleitor')),
                ('num_registro_cnh', models.BigIntegerField(blank=True, null=True, verbose_name='Número do Registro da CNH')),
                ('validade_cnh', models.DateField(verbose_name='Validade da CNH')),
                ('categoria_cnh', models.CharField(verbose_name='Categoria da CNH', max_length=255, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('AB', 'AB'), ('AC', 'AC'), ('AD', 'AD'), ('AE', 'AE'), ('ACC', 'ACC')])),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."cidadao"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, to='pessoal.PessoaJuridica', primary_key=True)),
                ('reservado', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'editora',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, to='pessoal.PessoaJuridica', primary_key=True)),
                ('inep_da_escola', models.CharField(max_length=255)),
                ('latitude', models.CharField(blank=True, null=True, max_length=255)),
                ('longitude', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'escola',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, to='pessoal.PessoaJuridica', primary_key=True)),
                ('reservado', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'fornecedor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, to='pessoal.PessoaFisica', primary_key=True)),
                ('prontuario', models.CharField(max_length=255)),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."paciente"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Prefeitura',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, to='pessoal.PessoaJuridica', primary_key=True)),
                ('brasao', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'prefeitura',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, to='pessoal.Cidadao', primary_key=True)),
                ('numero_de_inscricao', models.CharField(blank=True, null=True, max_length=255, unique=True)),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."aluno"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, to='pessoal.Cidadao', primary_key=True)),
                ('carga_horaria', models.CharField(max_length=255)),
                ('data_de_admissao', models.DateField(blank=True, null=True)),
                ('data_de_demissao', models.DateField(blank=True, null=True)),
                ('inss', models.CharField(blank=True, null=True, max_length=255)),
                ('matricula', models.CharField(unique=True, max_length=255)),
                ('ativo', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."funcionario"',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='detempropriedade',
            name='cidadao',
            field=models.ForeignKey(to='pessoal.Cidadao'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fornecedor',
            field=models.ForeignKey(to='pessoal.Fornecedor'),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, to='pessoal.Funcionario', primary_key=True)),
                ('identificacao', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'professor',
                'managed': True,
            },
        ),
    ]
