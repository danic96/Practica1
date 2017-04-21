# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacio', '0002_auto_20170419_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='deck',
            field=models.TextField(default='null', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='power',
            name='description',
            field=models.TextField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]
