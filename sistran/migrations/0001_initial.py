# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal', '0004_auto_20150929_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anexo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nome_documento', models.CharField(max_length=255)),
                ('caminho_anexo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Cobrador',
            fields=[
                ('id', models.OneToOneField(to='pessoal.Cidadao', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.OneToOneField(to='pessoal.Cidadao', primary_key=True, serialize=False)),
                ('num_cnh', models.IntegerField(verbose_name='Numero da CNH')),
                ('cat_cnh', models.CharField(verbose_name='Categoria da CNH', max_length=255, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('AB', 'AB'), ('AC', 'AC'), ('AD', 'AD'), ('AE', 'AE'), ('ACC', 'ACC')])),
            ],
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.OneToOneField(to='pessoal.Cidadao', primary_key=True, serialize=False)),
                ('num_cnh', models.IntegerField(verbose_name='Numero da CNH')),
                ('cat_cnh', models.IntegerField(verbose_name='Categoria da CNH')),
            ],
        ),
        migrations.CreateModel(
            name='ProprietarioTemVeiculo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('data_posse', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=10, choices=[('Ativo', 'Ativo'), ('Repassado', 'Repassado'), ('Cancelado', 'Cancelado')])),
                ('motorista', models.BooleanField()),
                ('id_proprietario', models.ForeignKey(to='sistran.Proprietario')),
            ],
        ),
        migrations.CreateModel(
            name='Reclamacao',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=255)),
                ('data_hora', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('data_posse', models.DateField(auto_now=True)),
                ('tipo_concessao', models.CharField(verbose_name='Tipo do Veículo', max_length=20, choices=[('taxi', 'Táxi'), ('alternativo', 'Alternativo'), ('escolar', 'Escolar'), ('frete', 'Frete')])),
                ('marca_modelo', models.CharField(verbose_name='Marca/Modelo do Veículo', max_length=255)),
                ('ano', models.IntegerField(verbose_name='Ano do Veículo')),
                ('cor', models.CharField(verbose_name='Cor do Veículo', max_length=255)),
                ('chassi', models.CharField(verbose_name='Chassi do Veículo', max_length=255)),
                ('qnt_passageiros', models.IntegerField(verbose_name='Quant. de Passageiros')),
                ('qnt_portas', models.IntegerField(verbose_name='Quant. de Portas')),
                ('placa', models.CharField(verbose_name='Placa do Veículo', max_length=8)),
                ('motorista', models.BooleanField(verbose_name='Proprietário é Motorista desse Veículo?')),
                ('categoria', models.CharField(verbose_name='Categoria do Veículo', max_length=50, choices=[('oficial', 'Oficial'), ('representacao_diplomatica', 'Representação Diplomática'), ('particular', 'Particular'), ('aluguel', 'Aluguel'), ('aprendizagem', 'Aprendizagem')])),
                ('id_proprietario', models.ForeignKey(verbose_name='Proprietário do Veículo', to='sistran.Proprietario')),
            ],
        ),
        migrations.CreateModel(
            name='VeiculoTemCobrador',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('data_posse', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=10, choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')])),
                ('id_cobrador', models.ForeignKey(to='sistran.Cobrador')),
                ('id_veiculo', models.ForeignKey(to='sistran.Veiculo')),
            ],
        ),
        migrations.CreateModel(
            name='VeiculoTemMotorista',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('data_posse', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=10, choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')])),
                ('id_motorista', models.ForeignKey(to='sistran.Motorista')),
                ('id_veiculo', models.ForeignKey(to='sistran.Veiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Vistoria',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('data', models.DateField()),
                ('aprovado', models.BooleanField()),
                ('observacao', models.CharField(max_length=255)),
                ('veiculo', models.ForeignKey(to='sistran.Veiculo')),
            ],
        ),
        migrations.CreateModel(
            name='VistoriaItem',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('nome_item', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VistoriaTemVistoriaItem',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('status', models.CharField(max_length=20, choices=[('Aprovado', 'Aprovado'), ('Reprovado', 'Reprovado')])),
                ('id_vistoria', models.ForeignKey(to='sistran.Vistoria')),
                ('id_vistoria_item', models.ForeignKey(to='sistran.VistoriaItem')),
            ],
        ),
        migrations.AddField(
            model_name='reclamacao',
            name='veiculo',
            field=models.ForeignKey(to='sistran.Veiculo'),
        ),
        migrations.AddField(
            model_name='proprietariotemveiculo',
            name='id_veiculo',
            field=models.ForeignKey(to='sistran.Veiculo'),
        ),
        migrations.AddField(
            model_name='anexo',
            name='cidadao',
            field=models.ForeignKey(to='pessoal.Cidadao'),
        ),
    ]
