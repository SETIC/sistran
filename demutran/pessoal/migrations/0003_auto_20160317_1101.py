# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-17 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal', '0002_auto_20160315_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='celular',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='celular¹'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='celular_alternativo',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='celular²'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='criado em'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='e-mail'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='telefone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='telefone'),
        ),
    ]
