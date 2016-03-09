# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-25 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistran', '0002_vistoria_vistoriaitem_vistoriatemvistoriaitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('pago', models.BooleanField()),
                ('permissao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistran.Permissao')),
            ],
        ),
        migrations.CreateModel(
            name='TipoServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=255)),
                ('valor', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='ordemservico',
            name='tipo_servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistran.TipoServico'),
        ),
    ]
