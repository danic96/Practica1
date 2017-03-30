# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacio', '0005_relacions'),
    ]

    operations = [
        migrations.AddField(
            model_name='personatge',
            name='id_pelicula',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
