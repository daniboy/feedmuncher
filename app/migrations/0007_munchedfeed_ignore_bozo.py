# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150406_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='munchedfeed',
            name='ignore_bozo',
            field=models.BooleanField(default=False),
        ),
    ]
