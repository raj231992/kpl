# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-04 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0036_auto_20170303_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='batting_scorecard',
            name='come_back',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=6),
        ),
    ]
