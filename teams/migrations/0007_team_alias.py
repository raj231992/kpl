# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-01 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20170207_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='alias',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
