# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cidadao',
            table='"cadastro_unico_pessoal"."cidadao"',
        ),
    ]
