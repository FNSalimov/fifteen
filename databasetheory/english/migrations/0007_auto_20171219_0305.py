# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0006_auto_20171219_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='added_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
