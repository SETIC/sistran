# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal', '0002_auto_20150908_1330'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='funcionario',
            table='"cadastro_unico_pessoal"."funcionario"',
        ),
        migrations.AlterModelTable(
            name='motorista',
            table='"cadastro_unico_pessoal"."motorista"',
        ),
    ]
