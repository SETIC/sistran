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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_documento', models.CharField(max_length=255)),
                ('caminho', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='AnexoPermissao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_documento', models.CharField(max_length=255)),
                ('caminho', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Cobrador',
            fields=[
                ('id', models.OneToOneField(to='pessoal.Cidadao', serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.OneToOneField(to='pessoal.Cidadao', serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permissao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField(verbose_name='Número da Permissão')),
                ('data', models.DateField(auto_now=True)),
                ('tipo_concessao', models.CharField(verbose_name='Tipo do Veículo', max_length=20, choices=[('TÁXI', 'TÁXI'), ('ALTERNATIVO', 'ALTERNATIVO'), ('ESCOLAR', 'ESCOLAR'), ('FRETE', 'FRETE')])),
            ],
        ),
        migrations.CreateModel(
            name='PermissaoTemCobrador',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('data_posse', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=10, choices=[('ATIVO', 'ATIVO'), ('INATIVO', 'INATIVO')])),
                ('cobrador', models.ForeignKey(to='sistran.Cobrador')),
            ],
        ),
        migrations.CreateModel(
            name='PermissaoTemMotorista',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('data_posse', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=10, choices=[('ATIVO', 'ATIVO'), ('INATIVO', 'INATIVO')])),
                ('motorista', models.ForeignKey(to='sistran.Motorista')),
            ],
        ),
        migrations.CreateModel(
            name='PermissaoTemProprietario',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('data_posse', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=10, choices=[('ATIVO', 'ATIVO'), ('TRANSFERIDO', 'TRANSFERIDO'), ('INATIVO', 'INATIVO')])),
            ],
        ),
        migrations.CreateModel(
            name='PermissaoTemVeiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('data_posse', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=10, choices=[('ATIVO', 'ATIVO'), ('TRANSFERIDO', 'TRANSFERIDO'), ('INATIVO', 'INATIVO')])),
                ('permissao', models.ForeignKey(to='sistran.Permissao')),
            ],
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.OneToOneField(to='pessoal.Cidadao', serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('codigo_renavan', models.BigIntegerField(serialize=False, primary_key=True, verbose_name='Código Renavan')),
                ('veiculo_proprio', models.BooleanField(default=True)),
                ('exercicio', models.CharField(max_length=255, verbose_name='Ano de Exercício')),
                ('placa', models.CharField(max_length=8, verbose_name='Placa do Veículo')),
                ('chassi', models.CharField(max_length=255, verbose_name='Chassi do Veículo')),
                ('num_passageiros', models.IntegerField(verbose_name='Número de Passageiros')),
                ('combustivel', models.CharField(max_length=255, verbose_name='Combustível')),
                ('marca', models.CharField(verbose_name='Marca', max_length=255, choices=[('AGRALE', 'AGRALE'), ('ASTON MARTIN', 'ASTON MARTIN'), ('AUDI', 'AUDI'), ('BENTLEY', 'BENTLEY'), ('BMW', 'BMW'), ('CHANGAN', 'CHANGAN'), ('CHERY', 'CHERY'), ('GM/CHEVROLET', 'GM/CHEVROLET'), ('CHRYSLER', 'CHRYSLER'), ('CITROËN', 'CITROËN'), ('DODGE', 'DODGE'), ('EFFA', 'EFFA'), ('FERRARI', 'FERRARI'), ('FIAT', 'FIAT'), ('FORD', 'FORD'), ('GEELY', 'GEELY'), ('HAFEI', 'HAFEI'), ('HONDA', 'HONDA'), ('HYUNDAI', 'HYUNDAI'), ('IVECO', 'IVECO'), ('JAC MOTORS', 'JAC MOTORS'), ('JAGUAR', 'JAGUAR'), ('JEEP', 'JEEP'), ('JINBEI', 'JINBEI'), ('KIA', 'KIA'), ('LAMBORGHINI', 'LAMBORGHINI'), ('LAND ROVER', 'LAND ROVER'), ('LEXUS', 'LEXUS'), ('LIFAN', 'LIFAN'), ('MAHINDRA', 'MAHINDRA'), ('MASERATI', 'MASERATI'), ('MERCEDES-BENZ', 'MERCEDES-BENZ'), ('MG MOTORS', 'MG MOTORS'), ('MINI', 'MINI'), ('MITSUBISHI', 'MITSUBISHI'), ('NISSAN', 'NISSAN'), ('PEUGEOT', 'PEUGEOT'), ('PORSCHE', 'PORSCHE'), ('RAM', 'RAM'), ('RENAULT', 'RENAULT'), ('SMART', 'SMART'), ('SSANGYONG', 'SSANGYONG'), ('SUBARU', 'SUBARU'), ('SUZUKI', 'SUZUKI'), ('TOYOTA', 'TOYOTA'), ('TROLLER', 'TROLLER'), ('VOLKSWAGEN', 'VOLKSWAGEN'), ('VOLVO', 'VOLVO')])),
                ('modelo', models.CharField(max_length=255, verbose_name='Modelo')),
                ('ano_fabricacao', models.CharField(max_length=255, verbose_name='Ano de Fabricação')),
                ('categoria', models.CharField(verbose_name='Categoria', max_length=155, choices=[('OFICIAL', 'OFICIAL'), ('REPRESENTAÇÃO DIPLOMÁTICA', 'REPRESENTAÇÃO DIPLOMÁTICA'), ('PARTICULAR', 'PARTICULAR'), ('ALUGUEL', 'ALUGUEL'), ('APRENDIZAGEM', 'APRENDIZAGEM')])),
                ('cor_predominante', models.CharField(verbose_name='Cor Predominante', max_length=255, choices=[('BRANCO', 'BRANCO'), ('PRATA', 'PRATA'), ('PRETO', 'PRETO'), ('CINZA', 'CINZA'), ('VERMELHO', 'VERMELHO'), ('MARROM', 'MARROM'), ('BEGE', 'BEGE'), ('AZUL', 'AZUL'), ('VERDE', 'VERDE'), ('AMARELO', 'AMARELO'), ('DOURADO', 'DOURADO')])),
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
