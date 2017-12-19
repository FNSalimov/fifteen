# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sphere',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('parent', models.ForeignKey(to='english.Sphere')),
            ],
        ),
        migrations.CreateModel(
            name='User_Word',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('learned_time', models.DateTimeField()),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('defenition', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('added_time', models.DateTimeField(default=datetime.datetime(2017, 12, 19, 2, 37, 16, 149199))),
                ('added_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('belongs', models.ForeignKey(to='english.Sphere')),
            ],
        ),
        migrations.AddField(
            model_name='user_word',
            name='word_id',
            field=models.ForeignKey(to='english.Word'),
        ),
    ]
