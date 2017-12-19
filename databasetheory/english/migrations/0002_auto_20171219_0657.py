# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_word',
            name='learned_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
