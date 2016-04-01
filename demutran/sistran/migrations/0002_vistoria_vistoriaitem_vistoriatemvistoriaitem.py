# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-23 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistran', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vistoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('aprovado', models.BooleanField()),
                ('observacao', models.TextField(max_length=255)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistran.Veiculo')),
            ],
        ),
        migrations.CreateModel(
            name='VistoriaItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_item', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VistoriaTemVistoriaItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_vistoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistran.Vistoria')),
                ('id_vistoria_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistran.VistoriaItem')),
            ],
        ),
    ]