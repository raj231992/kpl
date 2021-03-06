# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-01 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_team_alias'),
        ('matches', '0008_auto_20170302_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Points_Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played', models.CharField(default=0, max_length=1)),
                ('won', models.CharField(default=0, max_length=1)),
                ('lost', models.CharField(default=0, max_length=1)),
                ('points', models.CharField(default=0, max_length=2)),
                ('nrr', models.CharField(default=0, max_length=10)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pt_team', to='teams.Team')),
            ],
        ),
    ]
