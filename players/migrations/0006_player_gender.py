# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-24 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_auto_20170123_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6),
        ),
    ]
