# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.TextField(max_length=50)),
                ('gender', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.TextField(max_length=50)),
                ('deck', models.TextField(max_length=100)),
                ('duration', models.TextField(null=True, blank=True)),
                ('revenue', models.TextField(null=True, blank=True)),
                ('detail_url', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RelationCharacterPower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_character', models.PositiveIntegerField()),
                ('id_power', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RelationCharacterTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_character', models.PositiveIntegerField()),
                ('id_team', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RelationMovieCharacter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_movie', models.PositiveIntegerField()),
                ('id_character', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RelationMovieLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_movie', models.PositiveIntegerField()),
                ('id_location', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.TextField(max_length=50)),
                ('num_members', models.PositiveIntegerField(null=True, blank=True)),
                ('description', models.TextField(max_length=100)),
            ],
        ),
    ]
