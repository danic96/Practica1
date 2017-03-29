# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacio', '0003_auto_20170328_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='detail_url',
            field=models.TextField(default='http://google.com', max_length=100),
            preserve_default=False,
        ),
    ]
