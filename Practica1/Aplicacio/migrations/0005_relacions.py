# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacio', '0004_pelicula_detail_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relacions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_pelicula', models.PositiveIntegerField()),
                ('id_personatge', models.PositiveIntegerField()),
            ],
        ),
    ]
