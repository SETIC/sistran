# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-16 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracao', '0001_initial'),
        ('localizacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aditivo',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
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
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_contato', models.CharField(blank=True, choices=[('TELEFONE', 'TELEFONE'), ('CELULAR', 'CELULAR'), ('EMAIL', 'EMAIL')], max_length=255, verbose_name='Tipo do Contato')),
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
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('numero_contrato', models.CharField(max_length=255)),
                ('vigencia_contrato', models.CharField(blank=True, max_length=255, null=True)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField()),
                ('valor_limite', models.FloatField()),
                ('produto', models.CharField(max_length=255)),
                ('saldo_restante', models.FloatField(blank=True, null=True)),
                ('aditivo_vigente', models.CharField(max_length=255)),
                ('organismo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracao.Organismo')),
            ],
            options={
                'db_table': 'contrato',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DadosBancarios',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('banco_agencia', models.CharField(max_length=255)),
                ('banco_conta', models.CharField(max_length=255)),
                ('banco_nome', models.CharField(max_length=255)),
                ('banco_operacao', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."dados_bancarios"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DetemPropriedade',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField(blank=True, null=True)),
                ('unidade_edificada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localizacao.UnidadeEdificada')),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."detem_propriedade"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NecessidadesEspeciais',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descrição')),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."necessidades_especiais"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome Completo')),
                ('cpf_cnpj', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='CPF')),
                ('data_de_nascimento', models.DateField(blank=True, null=True)),
                ('escid', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], max_length=255)),
                ('esc_id_destino', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."pessoa"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PessoaFisicaNecessidadesEspeciais',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('observacao', models.CharField(blank=True, max_length=255, null=True, verbose_name='Observação')),
                ('necessidades_especiais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoal.NecessidadesEspeciais')),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."pessoa_fisica_necessidades_especiais"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Reside',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=255, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=300, null=True)),
                ('cep', models.CharField(blank=True, max_length=9, null=True, verbose_name='CEP')),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localizacao.Bairro')),
                ('logradouro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localizacao.Logradouro')),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."reside"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoContato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_contato', models.CharField(choices=[('TELEFONE', 'TELEFONE'), ('CELULAR', 'CELULAR'), ('EMAIL', 'EMAIL')], max_length=255, verbose_name='Tipo do Contato')),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."tipo_contato"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pessoal.Pessoa')),
                ('cor', models.CharField(blank=True, max_length=255, null=True)),
                ('foto', models.CharField(blank=True, max_length=255, null=True)),
                ('grau_de_instrucao', models.CharField(blank=True, max_length=255, null=True)),
                ('rc_data_do_registro', models.DateField(blank=True, null=True)),
                ('rc_folha_do_livro', models.CharField(blank=True, max_length=255, null=True)),
                ('rc_nome_do_cartorio', models.CharField(blank=True, max_length=255, null=True)),
                ('rc_nome_do_livro', models.CharField(blank=True, max_length=255, null=True)),
                ('rc_numero', models.CharField(blank=True, max_length=255, null=True)),
                ('religiao', models.CharField(blank=True, max_length=255, null=True)),
                ('sexo', models.CharField(choices=[('MASCULINO', 'MASCULINO'), ('FEMININO', 'FEMININO')], max_length=255)),
                ('tipo_sanguineo', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."pessoa_fisica"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pessoal.Pessoa')),
                ('inscricao_estadual', models.CharField(blank=True, max_length=255, null=True)),
                ('razao_social', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."pessoa_juridica"',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='reside',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoal.Pessoa'),
        ),
        migrations.AddField(
            model_name='dadosbancarios',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoal.Pessoa'),
        ),
        migrations.AddField(
            model_name='contato',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoal.Pessoa'),
        ),
        migrations.AddField(
            model_name='aditivo',
            name='contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoal.Contrato'),
        ),
        migrations.CreateModel(
            name='Cidadao',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pessoal.PessoaFisica')),
                ('cm_categoria', models.CharField(blank=True, max_length=255, null=True)),
                ('cm_data_de_emissao', models.DateField(blank=True, null=True)),
                ('cm_numero', models.CharField(blank=True, max_length=255, null=True)),
                ('ct_data_de_emissao', models.DateField(blank=True, null=True)),
                ('ct_numero', models.CharField(blank=True, max_length=255, null=True)),
                ('ct_serie', models.CharField(blank=True, max_length=255, null=True)),
                ('estado_civil', models.CharField(choices=[('SOLTEIRO(A)', 'SOLTEIRO(A)'), ('CASADO', 'CASADO(A)'), ('SEPARADO', 'SEPARADO(A)'), ('DIVORCIADO', 'DIVORCIADO(A)'), ('VIÚVO', 'VIÚVO(A)')], max_length=255, verbose_name='Estado Civil')),
                ('nacionalidade', models.CharField(blank=True, max_length=255, null=True)),
                ('naturalidade', models.CharField(blank=True, max_length=255, null=True)),
                ('profissao', models.CharField(blank=True, max_length=255, null=True)),
                ('rg_data_de_emissao', models.DateField(verbose_name='Data de Emissão do RG')),
                ('rg_numero', models.IntegerField(verbose_name='RG')),
                ('rg_orgao_expeditor', models.CharField(max_length=255, verbose_name='Órgão Expedidor do RG')),
                ('te_numero', models.BigIntegerField(blank=True, null=True, verbose_name='Número Título de Eleitor')),
                ('te_secao', models.IntegerField(blank=True, null=True, verbose_name='Seção Título de Eleitor')),
                ('te_zona', models.IntegerField(blank=True, null=True, verbose_name='Zona Título de Eleitor')),
                ('num_registro_cnh', models.BigIntegerField(blank=True, null=True, verbose_name='Número do Registro da CNH')),
                ('validade_cnh', models.DateField(verbose_name='Validade da CNH')),
                ('categoria_cnh', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('AB', 'AB'), ('AC', 'AC'), ('AD', 'AD'), ('AE', 'AE'), ('ACC', 'ACC')], max_length=255, verbose_name='Categoria da CNH')),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."cidadao"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pessoal.PessoaJuridica')),
                ('reservado', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'editora',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pessoal.PessoaJuridica')),
                ('inep_da_escola', models.CharField(max_length=255)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'escola',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pessoal.PessoaJuridica')),
                ('reservado', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'fornecedor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pessoal.PessoaFisica')),
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
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pessoal.PessoaJuridica')),
                ('brasao', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'prefeitura',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='pessoafisicanecessidadesespeciais',
            name='pessoa_fisica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoal.PessoaFisica'),
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pessoal.Cidadao')),
                ('numero_de_inscricao', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."aluno"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pessoal.Cidadao')),
                ('carga_horaria', models.CharField(max_length=255)),
                ('data_de_admissao', models.DateField(blank=True, null=True)),
                ('data_de_demissao', models.DateField(blank=True, null=True)),
                ('inss', models.CharField(blank=True, max_length=255, null=True)),
                ('matricula', models.CharField(max_length=255, unique=True)),
                ('ativo', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': '"cadastro_unico_pessoal"."funcionario"',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='detempropriedade',
            name='cidadao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoal.Cidadao'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoal.Fornecedor'),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pessoal.Funcionario')),
                ('identificacao', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'professor',
                'managed': True,
            },
        ),
    ]
