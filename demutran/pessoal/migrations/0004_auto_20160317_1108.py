# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-17 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal', '0003_auto_20160317_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='celular',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='celular_alternativo',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='criado_em',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='email',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='telefone',
        ),
    ]
