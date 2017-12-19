# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0005_auto_20171219_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sphere',
            name='parent',
            field=models.ForeignKey(to='english.Sphere', null=True),
        ),
    ]
