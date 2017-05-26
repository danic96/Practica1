# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacio', '0007_auto_20170526_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='powers',
            field=models.ManyToManyField(to='Aplicacio.Power', blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='teams',
            field=models.ManyToManyField(to='Aplicacio.Team', blank=True),
        ),
    ]
