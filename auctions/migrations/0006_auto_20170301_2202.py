# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-01 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20170207_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='sold_player',
            name='catches',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='sold_player',
            name='fours',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='sold_player',
            name='runs',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='sold_player',
            name='sixes',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='sold_player',
            name='wickets',
            field=models.CharField(default=0, max_length=2),
        ),
    ]
