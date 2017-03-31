# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacio', '0006_personatge_id_pelicula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personatge',
            name='id_pelicula',
        ),
    ]
