# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnexoCidadao',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nome_documento', models.CharField(max_length=255)),
                ('caminho', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='AnexoPermissao',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nome_documento', models.CharField(max_length=255)),
                ('caminho', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Cobrador',
            fields=[
                ('id', models.OneToOneField(serialize=False, primary_key=True, to='pessoal.Cidadao')),
            ],
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.OneToOneField(serialize=False, primary_key=True, to='pessoal.Cidadao')),
            ],
        ),
        migrations.CreateModel(
            name='Permissao',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('numero', models.IntegerField()),
                ('data', models.DateField()),
                ('tipo_concessao', models.CharField(verbose_name='Tipo do Veículo', max_length=20, choices=[('TÁXI', 'TÁXI'), ('ALTERNATIVO', 'ALTERNATIVO'), ('ESCOLAR', 'ESCOLAR'), ('FRETE', 'FRETE')])),
            ],
        ),
        migrations.CreateModel(
            name='PermissaoTemCobrador',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('data_posse', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=10, choices=[('ATIVO', 'ATIVO'), ('INATIVO', 'INATIVO')])),
                ('cobrador', models.ForeignKey(to='sistran.Cobrador')),
            ],
        ),
        migrations.CreateModel(
            name='PermissaoTemMotorista',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('data_posse', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=10, choices=[('ATIVO', 'ATIVO'), ('INATIVO', 'INATIVO')])),
                ('motorista', models.ForeignKey(to='sistran.Motorista')),
            ],
        ),
        migrations.CreateModel(
            name='PermissaoTemProprietario',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('data_posse', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=10, choices=[('ATIVO', 'ATIVO'), ('TRANSFERIDO', 'TRANSFERIDO'), ('INATIVO', 'INATIVO')])),
            ],
        ),
        migrations.CreateModel(
            name='PermissaoTemVeiculo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('data_posse', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=10, choices=[('ATIVO', 'ATIVO'), ('TRANSFERIDO', 'TRANSFERIDO'), ('INATIVO', 'INATIVO')])),
                ('permissao', models.ForeignKey(to='sistran.Permissao')),
            ],
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.OneToOneField(serialize=False, primary_key=True, to='pessoal.Cidadao')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('codigo_renavan', models.BigIntegerField(serialize=False, primary_key=True)),
                ('veiculo_proprio', models.BooleanField(default=True)),
                ('exercicio', models.DateField()),
                ('placa', models.CharField(verbose_name='Placa do Veículo', max_length=8)),
                ('chassi', models.CharField(verbose_name='Chassi do Veículo', max_length=255)),
                ('num_passageiros', models.IntegerField(verbose_name='Número de Passageiros')),
                ('combustivel', models.CharField(verbose_name='Combustível', max_length=255)),
                ('marca_modelo', models.CharField(verbose_name='Marca/Modelo', max_length=255)),
                ('ano_fabricacao', models.CharField(verbose_name='Ano de Fabricação', max_length=255)),
                ('categoria', models.CharField(verbose_name='Categoria', max_length=155, choices=[('OFICIAL', 'OFICIAL'), ('REPRESENTAÇÃO DIPLOMÁTICA', 'REPRESENTAÇÃO DIPLOMÁTICA'), ('PARTICULAR', 'PARTICULAR'), ('ALUGUEL', 'ALUGUEL'), ('APRENDIZAGEM', 'APRENDIZAGEM')])),
                ('cor_predominante', models.CharField(verbose_name='Cor Predominante', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='permissaotemveiculo',
            name='veiculo',
            field=models.ForeignKey(to='sistran.Veiculo'),
        ),
        migrations.AddField(
            model_name='permissaotemproprietario',
            name='permissao_veiculo',
            field=models.ForeignKey(to='sistran.PermissaoTemVeiculo'),
        ),
        migrations.AddField(
            model_name='permissaotemproprietario',
            name='proprietario',
            field=models.ForeignKey(to='sistran.Proprietario'),
        ),
        migrations.AddField(
            model_name='permissaotemmotorista',
            name='permissao_veiculo',
            field=models.ForeignKey(to='sistran.PermissaoTemVeiculo'),
        ),
        migrations.AddField(
            model_name='permissaotemcobrador',
            name='permissao_veiculo',
            field=models.ForeignKey(to='sistran.PermissaoTemVeiculo'),
        ),
        migrations.AddField(
            model_name='anexopermissao',
            name='permissao',
            field=models.ForeignKey(to='sistran.Permissao'),
        ),
        migrations.AddField(
            model_name='anexocidadao',
            name='cidadao',
            field=models.ForeignKey(to='pessoal.Cidadao'),
        ),
    ]
