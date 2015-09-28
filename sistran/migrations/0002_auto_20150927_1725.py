# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistran', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cobrador',
            name='id',
            field=models.OneToOneField(primary_key=True, to='pessoal.Cidadao', serialize=False),
        ),
        migrations.AlterField(
            model_name='motorista',
            name='cat_cnh',
            field=models.CharField(verbose_name='Cat. da CNH', max_length=255),
        ),
        migrations.AlterField(
            model_name='motorista',
            name='id',
            field=models.OneToOneField(primary_key=True, to='pessoal.Cidadao', serialize=False),
        ),
        migrations.AlterField(
            model_name='motorista',
            name='num_cnh',
            field=models.CharField(verbose_name='Num. da CNH', max_length=255),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='cat_cnh',
            field=models.CharField(verbose_name='Cat. da CNH', max_length=255),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='id',
            field=models.OneToOneField(primary_key=True, to='pessoal.Cidadao', serialize=False),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='num_cnh',
            field=models.CharField(verbose_name='Num. da CNH', max_length=255),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='categoria',
            field=models.CharField(max_length=50, choices=[('oficial', 'Oficial'), ('representacao_diplomatica', 'Representação Diplomática'), ('particular', 'Particular'), ('aluguel', 'Aluguel'), ('aprendizagem', 'Aprendizagem')]),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='chassi',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='motorista',
            field=models.ForeignKey(to='sistran.Motorista'),
        ),
    ]
