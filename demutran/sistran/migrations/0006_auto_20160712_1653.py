# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-12 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistran', '0005_auto_20160315_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permissao',
            options={'ordering': ('num_permissao',)},
        ),
        migrations.AlterField(
            model_name='vistoria',
            name='ordem_servico',
            field=models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to='sistran.OrdemServico'),
        ),
    ]
