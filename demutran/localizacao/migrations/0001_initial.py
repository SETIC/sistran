# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-16 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
                'db_table': '"cadastro_unico_localizacao"."estado"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoMunicipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('face_da_quadra', models.CharField(blank=True, max_length=255, null=True)),
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
                'db_table': '"cadastro_unico_localizacao"."logradouro"',
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
                ('identificacao', models.CharField(blank=True, max_length=50, null=True)),
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
                'db_table': '"cadastro_unico_localizacao"."municipio"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Quadra',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('quadra', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'quadra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('setor', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'setor',
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
                'db_table': '"cadastro_unico_localizacao"."tipo_logradouro"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoLogradouroLogradouro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': '"cadastro_unico_localizacao"."tipo_logradouro_logradouro"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UnidadeEdificada',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('area_edificada', models.FloatField()),
                ('area_total_construida', models.FloatField()),
                ('identificacao', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'unidade_edificada',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='localizacao.DivisaoAdministrativa')),
                ('bairro', models.CharField(max_length=255)),
            ],
            options={
                'db_table': '"cadastro_unico_localizacao"."bairro"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comercial',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='localizacao.UnidadeEdificada')),
                ('reservado', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'comercial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='localizacao.DivisaoAdministrativa')),
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
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='localizacao.UnidadeEdificada')),
                ('reservado', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'industrial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Residencial',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='localizacao.UnidadeEdificada')),
                ('reservado', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'residencial',
                'managed': False,
            },
        ),
    ]
