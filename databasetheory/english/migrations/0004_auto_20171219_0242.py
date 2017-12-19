# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0003_auto_20171219_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sphere',
            name='parent',
            field=models.ForeignKey(default=1, to='english.Sphere'),
        ),
    ]
