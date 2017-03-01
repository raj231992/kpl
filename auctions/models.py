from __future__ import unicode_literals

from django.db import models
from players.models import Player
from teams.models import Team
# Create your models here.
class Refresh_Data(models.Model):
    refresh = models.CharField(max_length=1,default='0')
class Current_Player(models.Model):
    current_player = models.ForeignKey(Player,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.current_player)

class Sold_Player(models.Model):
    player = models.ForeignKey(Player,on_delete=models.CASCADE)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    runs = models.CharField(max_length=3,default=0)
    wickets = models.CharField(max_length=2,default=0)
    sixes = models.CharField(max_length=2,default=0)
    fours = models.CharField(max_length=2,default=0)
    catches = models.CharField(max_length=2,default=0)

    def __str__(self):
        return str(self.player)

