# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacio', '0002_auto_20170325_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='durada',
            field=models.TextField(null=True, blank=True),
        ),
    ]
