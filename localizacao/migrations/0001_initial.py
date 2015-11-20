# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DivisaoAdministrativa',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'divisao_administrativa',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('abreviacao', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'estado',
            },
        ),
        migrations.CreateModel(
            name='EstadoMunicipio',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
            options={
                'managed': False,
                'db_table': 'estado_municipio',
            },
        ),
        migrations.CreateModel(
            name='FaceDaQuadra',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('face_da_quadra', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'face_da_quadra',
            },
        ),
        migrations.CreateModel(
            name='FotoLote',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('foto', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'foto_lote',
            },
        ),
        migrations.CreateModel(
            name='FotoUnidadeEdificada',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('foto', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'foto_unidade_edificada',
            },
        ),
        migrations.CreateModel(
            name='Logradouro',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('logradouro', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'logradouro',
            },
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('area_lote', models.FloatField()),
                ('delimitacao_frontal', models.CharField(max_length=255)),
                ('pedologia', models.CharField(max_length=255)),
                ('situacao', models.CharField(max_length=255)),
                ('topografia', models.CharField(max_length=255)),
                ('valor_venal', models.FloatField()),
                ('zeragem_de_quadrra', models.CharField(max_length=255)),
                ('identificacao', models.CharField(null=True, max_length=50, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'lote',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('municipio', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'municipio',
            },
        ),
        migrations.CreateModel(
            name='Quadra',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('quadra', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'quadra',
            },
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('setor', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'setor',
            },
        ),
        migrations.CreateModel(
            name='TipoLogradouro',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('tipo_logradouro', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'tipo_logradouro',
            },
        ),
        migrations.CreateModel(
            name='TipoLogradouroLogradouro',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
            options={
                'managed': False,
                'db_table': 'tipo_logradouro_logradouro',
            },
        ),
        migrations.CreateModel(
            name='UnidadeEdificada',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('area_edificada', models.FloatField()),
                ('area_total_construida', models.FloatField()),
                ('identificacao', models.CharField(null=True, max_length=50, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'unidade_edificada',
            },
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, primary_key=True, to='localizacao.DivisaoAdministrativa')),
                ('bairro', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'bairro',
            },
        ),
        migrations.CreateModel(
            name='Comercial',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, primary_key=True, to='localizacao.UnidadeEdificada')),
                ('reservado', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'comercial',
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, primary_key=True, to='localizacao.DivisaoAdministrativa')),
                ('distrito', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'distrito',
            },
        ),
        migrations.CreateModel(
            name='Industrial',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, primary_key=True, to='localizacao.UnidadeEdificada')),
                ('reservado', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'industrial',
            },
        ),
        migrations.CreateModel(
            name='Residencial',
            fields=[
                ('id', models.OneToOneField(db_column='id', serialize=False, primary_key=True, to='localizacao.UnidadeEdificada')),
                ('reservado', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'residencial',
            },
        ),
    ]
