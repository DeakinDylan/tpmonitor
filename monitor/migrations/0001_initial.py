# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-25 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=15)),
                ('temperature', models.FloatField()),
                ('alarmTpMin', models.FloatField()),
                ('alarmTpMax', models.FloatField()),
                ('updatetime', models.DateTimeField(verbose_name='status update')),
                ('status', models.BooleanField(default='true')),
            ],
        ),
    ]
