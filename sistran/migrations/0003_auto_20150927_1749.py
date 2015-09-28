# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistran', '0002_auto_20150927_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veiculo',
            old_name='motorista',
            new_name='motorista_id',
        ),
    ]
