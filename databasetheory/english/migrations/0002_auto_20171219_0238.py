# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='added_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 19, 2, 38, 2, 852020)),
        ),
    ]
