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
                'db_table': 'divisao_administrativa',
                'managed': False,
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
                'db_table': 'estado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoMunicipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'estado_municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FaceDaQuadra',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
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
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
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
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
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
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('logradouro', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'logradouro',
                'managed': False,
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
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('municipio', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Quadra',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
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
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
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
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('tipo_logradouro', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tipo_logradouro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoLogradouroLogradouro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'tipo_logradouro_logradouro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UnidadeEdificada',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
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
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='localizacao.DivisaoAdministrativa', serialize=False)),
                ('bairro', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'bairro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comercial',
            fields=[
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='localizacao.UnidadeEdificada', serialize=False)),
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
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='localizacao.DivisaoAdministrativa', serialize=False)),
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
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='localizacao.UnidadeEdificada', serialize=False)),
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
                ('id', models.ForeignKey(primary_key=True, db_column='id', to='localizacao.UnidadeEdificada', serialize=False)),
                ('reservado', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'residencial',
                'managed': False,
            },
        ),
    ]
