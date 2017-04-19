# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacio', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RelationCharacterPower',
        ),
        migrations.DeleteModel(
            name='RelationCharacterTeam',
        ),
        migrations.DeleteModel(
            name='RelationMovieCharacter',
        ),
        migrations.DeleteModel(
            name='RelationMovieLocation',
        ),
        migrations.AddField(
            model_name='character',
            name='powers',
            field=models.ManyToManyField(to='Aplicacio.Power'),
        ),
        migrations.AddField(
            model_name='character',
            name='teams',
            field=models.ManyToManyField(to='Aplicacio.Team'),
        ),
        migrations.AddField(
            model_name='movie',
            name='characters',
            field=models.ManyToManyField(to='Aplicacio.Character'),
        ),
        migrations.AddField(
            model_name='movie',
            name='locations',
            field=models.ManyToManyField(to='Aplicacio.Location'),
        ),
    ]
