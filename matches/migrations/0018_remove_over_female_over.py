# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-01 22:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0017_auto_20170302_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='over',
            name='female_over',
        ),
    ]
