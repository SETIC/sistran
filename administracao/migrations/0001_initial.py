# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessoria',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('assessoria', models.CharField(max_length=255)),
                ('contato_telefonico', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'assessoria',
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('cargo', models.CharField(max_length=255)),
                ('moeda_salario', models.FloatField(null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'cargo',
            },
        ),
        migrations.CreateModel(
            name='Celula',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('celula', models.CharField(max_length=255)),
                ('contato_telefonico', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'celula',
            },
        ),
        migrations.CreateModel(
            name='Lotacao',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField(null=True, blank=True)),
                ('situacao', models.CharField(max_length=255)),
                ('funcao', models.CharField(max_length=255)),
                ('vinculo', models.CharField(null=True, max_length=255, blank=True)),
                ('turno', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'lotacao',
            },
        ),
        migrations.CreateModel(
            name='Organismo',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('contato_telefonico', models.CharField(max_length=255)),
                ('organismo', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'organismo',
            },
        ),
    ]
