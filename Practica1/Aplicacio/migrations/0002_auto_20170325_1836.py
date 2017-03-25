# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('nom', models.TextField(max_length=50)),
                ('num_membres', models.PositiveIntegerField(null=True, blank=True)),
                ('descripcio', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Localitzacio',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('nom', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Personatge',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('nom', models.TextField(max_length=50)),
                ('genere', models.TextField(max_length=50)),
                ('descripcio', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Productora',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('nom', models.TextField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='pelicula',
            old_name='web',
            new_name='productors',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='data',
            field=models.TextField(default='default', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pelicula',
            name='durada',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='id',
            field=models.PositiveIntegerField(serialize=False, primary_key=True),
        ),
    ]
