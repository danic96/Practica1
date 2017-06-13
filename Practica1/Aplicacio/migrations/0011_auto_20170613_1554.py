# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Aplicacio', '0010_auto_20170526_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveSmallIntegerField(default=3, verbose_name='Rating (stars)', choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')])),
                ('comment', models.TextField(null=True, blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('movie', models.ForeignKey(to='Aplicacio.Movie')),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='moviereview',
            unique_together=set([('movie', 'user')]),
        ),
    ]
