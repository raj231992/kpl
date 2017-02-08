# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-06 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0008_auto_20170206_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='auction_status',
            field=models.CharField(choices=[('pending', 'pending'), ('sold', 'sold'), ('unsold', 'unsold')], default='pending', max_length=10),
        ),
    ]