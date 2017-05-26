# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacio', '0003_auto_20170421_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='characters',
            field=models.ManyToManyField(to='Aplicacio.Character', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='locations',
            field=models.ManyToManyField(to='Aplicacio.Location', blank=True),
        ),
    ]
