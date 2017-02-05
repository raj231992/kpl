from __future__ import unicode_literals

from django.db import models
from players.models import Player
# Create your models here.


class Team(models.Model):
    manager_only_opts = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    name = models.CharField(max_length=50)
    manager = models.ForeignKey(Player,on_delete=models.CASCADE)
    captain = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='captain')
    logo = models.ImageField(upload_to='team_logo/')
    manager_only = models.CharField(choices=manager_only_opts,max_length=3,default='No')
    money = models.CharField(max_length=4,default='3000')
    def __str__(self):
        return str(self.name)

class Member(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    player = models.ForeignKey(Player,on_delete=models.CASCADE)
    price = models.CharField(max_length=4,default='0')

    def __str__(self):
        return str(self.player)









