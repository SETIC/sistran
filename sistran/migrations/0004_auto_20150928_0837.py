# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistran', '0003_auto_20150927_1749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veiculo',
            old_name='motorista_id',
            new_name='motorista',
        ),
    ]
