from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Player(models.Model):
    cat_opts = (
        ('Batsman', 'Batsman'),
        ('Bowler', 'Bowler'),
        ('All-Rounder', 'All-Rounder'),
    )
    year_opts = (
        ('First', 'First'),
        ('Second', 'Second'),
        ('Third', 'Third'),
    )
    pool_opts = (
        ('A', 'A'),
        ('B', 'B'),
    )
    manager_opts = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    name = models.CharField(max_length=100, unique=True)
    manager = models.CharField(choices=manager_opts,max_length=3)
    year = models.CharField(max_length=10,choices=year_opts)
    pic = models.ImageField(upload_to='player_pics/')
    phone_no = models.CharField(max_length=10)
    category = models.CharField(choices=cat_opts, max_length=100)
    prev_exp = models.TextField(blank=True)
    kpl_exp = models.TextField(blank=True)
    pool = models.CharField(max_length=1,choices=pool_opts,default='B')

    def __str__(self):
        return str(self.name)
