# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-04 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20170304_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='sold_player',
            name='runout',
            field=models.IntegerField(default=0),
        ),
    ]