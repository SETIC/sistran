# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal', '0002_auto_20150908_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anexo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_documento', models.CharField(max_length=255)),
                ('caminho_anexo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Cobrador',
            fields=[
                ('id', models.ForeignKey(to='pessoal.Cidadao', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.ForeignKey(to='pessoal.Cidadao', primary_key=True, serialize=False)),
                ('num_cnh', models.CharField(max_length=255)),
                ('cat_cnh', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.ForeignKey(to='pessoal.Cidadao', primary_key=True, serialize=False)),
                ('num_cnh', models.CharField(max_length=255)),
                ('cat_cnh', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProprietarioTemVeiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('data_posse', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=10, choices=[('Ativo', 'Ativo'), ('Repassado', 'Repassado'), ('Cancelado', 'Cancelado')])),
                ('motorista', models.BooleanField()),
                ('id_proprietario', models.ForeignKey(to='sistran.Proprietario')),
            ],
        ),
        migrations.CreateModel(
            name='Reclamacao',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=255)),
                ('data_hora', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_posse', models.DateField(auto_now=True)),
                ('tipo_concessao', models.CharField(max_length=20, choices=[('taxi', 'Táxi'), ('alternativo', 'Alternativo'), ('escolar', 'Escolar'), ('frete', 'Frete')])),
                ('marca_modelo', models.CharField(max_length=255)),
                ('ano', models.DateField()),
                ('cor', models.CharField(max_length=255)),
                ('chassi', models.IntegerField()),
                ('qnt_passageiros', models.IntegerField()),
                ('qnt_portas', models.IntegerField()),
                ('placa', models.CharField(max_length=8)),
                ('motorista', models.BooleanField()),
                ('categoria', models.CharField(max_length=255)),
                ('id_proprietario', models.ForeignKey(to='sistran.Proprietario')),
            ],
        ),
        migrations.CreateModel(
            name='VeiculoTemCobrador',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('data_posse', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=10, choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')])),
                ('id_cobrador', models.ForeignKey(to='sistran.Cobrador')),
                ('id_veiculo', models.ForeignKey(to='sistran.Veiculo')),
            ],
        ),
        migrations.CreateModel(
            name='VeiculoTemMotorista',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('data_posse', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=10, choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')])),
                ('id_motorista', models.ForeignKey(to='sistran.Motorista')),
                ('id_veiculo', models.ForeignKey(to='sistran.Veiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Vistoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('aprovado', models.BooleanField()),
                ('observacao', models.CharField(max_length=255)),
                ('veiculo', models.ForeignKey(to='sistran.Veiculo')),
            ],
        ),
        migrations.CreateModel(
            name='VistoriaItem',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nome_item', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VistoriaTemVistoriaItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
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
