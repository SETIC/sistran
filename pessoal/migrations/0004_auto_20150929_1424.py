# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal', '0003_auto_20150922_1006'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='aluno',
            table='"cadastro_unico_pessoal"."aluno"',
        ),
        migrations.AlterModelTable(
            name='contato',
            table='"cadastro_unico_pessoal"."contato"',
        ),
        migrations.AlterModelTable(
            name='dadosbancarios',
            table='"cadastro_unico_pessoal"."dados_bancarios"',
        ),
        migrations.AlterModelTable(
            name='detempropriedade',
            table='"cadastro_unico_pessoal"."detem_propriedade"',
        ),
        migrations.AlterModelTable(
            name='paciente',
            table='"cadastro_unico_pessoal"."paciente"',
        ),
        migrations.AlterModelTable(
            name='pessoajuridica',
            table='"cadastro_unico_pessoal"."pessoa_juridica"',
        ),
        migrations.AlterModelTable(
            name='reside',
            table='"cadastro_unico_pessoal"."reside"',
        ),
        migrations.AlterModelTable(
            name='tipocontato',
            table='"cadastro_unico_pessoal"."tipo_contato"',
        ),
    ]
