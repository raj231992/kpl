# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-01 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0018_remove_over_female_over'),
    ]

    operations = [
        migrations.AlterField(
            model_name='over',
            name='over',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=1),
        ),
    ]