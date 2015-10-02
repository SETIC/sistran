# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistran', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='motorista',
            field=models.BooleanField(verbose_name='Proprietário é Motorista desse Veículo ?'),
        ),
    ]
