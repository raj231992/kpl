from __future__ import unicode_literals

from django.db import models
from teams.models import Team
from auctions.models import Sold_Player

# Create your models here.

class Match(models.Model):
    toss_choice = (
        ('Bat','Bat'),
        ('Field','Field'),
    )
    match_number = models.CharField(max_length=2)
    date = models.CharField(max_length=50)
    team1 = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='match_team2')
    team2 = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='match_team1')
    toss_won = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='match_toss',blank=True,null=True)
    selected_to = models.CharField(choices=toss_choice,max_length=5,blank=True)
    won = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='match_won',blank=True,null=True)
    man_of_match = models.ForeignKey(Sold_Player,on_delete=models.CASCADE,related_name='match_mom',blank=True,null=True)

    def __str__(self):
        return str(self.match_number)
class Extra(models.Model):
    extra_choices = (
        ('None','None'),
        ('Wide','Wide'),
        ('No Ball','No Ball')
    )
    type = models.CharField(choices=extra_choices,max_length=10)

    def __str__(self):
        return str(self.type)
class Wicket(models.Model):
    wicket_choices = (
        ('None', 'None'),
        ('Run Out','Run Out'),
        ('Caught','Caught'),
        ('Bold','Bold'),
        ('Hit Wicket','Hit Wicket'),
        ('Stumped','Stumped'),
    )
    type = models.CharField(choices=wicket_choices, max_length=15)
    player1 = models.ForeignKey(Sold_Player,on_delete=models.CASCADE,blank=True,related_name='wicket_player1')
    player2 = models.ForeignKey(Sold_Player,on_delete=models.CASCADE,blank=True,related_name='wicket_player2')

class Innings(models.Model):
    innings_choice = (
        ('First','First'),
        ('Second','Second'),
    )
    match = models.ForeignKey(Match,on_delete=models.CASCADE,related_name='inning_match')
    innings = models.CharField(choices=innings_choice,max_length=6)
    batting = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='inning_batting')
    bowling = models.ForeignKey(Team, on_delete=models.CASCADE,related_name='inning_bowling')
    runs = models.CharField(max_length=3,default=0)
    wickets = models.CharField(max_length=1,default=0)
    balls = models.CharField(max_length=2,default=0)
    extras = models.CharField(max_length=2,default=0)

    def __str__(self):
        return str(self.innings)

class Ball(models.Model):
    run = models.CharField(max_length=1,default=0)
    extra = models.ForeignKey(Extra,on_delete=models.CASCADE,related_name='ball_extra')
    wicket = models.ForeignKey(Wicket,on_delete=models.CASCADE,related_name='wicket_extra')

    def __str__(self):
        return str(self.id)

class Over(models.Model):
    over_choice = (
        ('Yes','Yes'),
        ('No','No'),
    )
    innings = models.ForeignKey(Innings, on_delete=models.CASCADE,related_name='over_innings')
    over = models.CharField(max_length=1)
    ball = models.ForeignKey(Ball,on_delete=models.CASCADE,related_name='over_ball')
    super_over = models.CharField(choices=over_choice,max_length=6)
    female_over = models.CharField(choices=over_choice,max_length=6)
    striker = models.ForeignKey(Sold_Player, on_delete=models.CASCADE,related_name='over_striker')
    non_striker = models.ForeignKey(Sold_Player, on_delete=models.CASCADE,related_name='over_non_striker')
    bowler = models.ForeignKey(Sold_Player, on_delete=models.CASCADE,related_name='over_bowler')

    def __str__(self):
        return str(self.over)

class Batting_Scorecard(models.Model):
    retired_choice = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    innings = models.ForeignKey(Innings, on_delete=models.CASCADE,related_name='batting_innings')
    batsman = models.ForeignKey(Sold_Player,on_delete=models.CASCADE,related_name='scorecard_batsman')
    runs = models.CharField(max_length=3,default=0)
    balls = models.CharField(max_length=2,default=0)
    fours = models.CharField(max_length=2,default=0)
    sixes = models.CharField(max_length=2,default=0)
    wicket = models.ForeignKey(Wicket,on_delete=models.CASCADE,blank=True,related_name='wicket_batsman')
    retired = models.CharField(choices=retired_choice,max_length=6)

    def __str__(self):
        return str(self.batsman)

class Bowling_Scorecard(models.Model):
    innings = models.ForeignKey(Innings, on_delete=models.CASCADE,related_name='bowling_innings')
    bowler = models.ForeignKey(Sold_Player, on_delete=models.CASCADE,related_name='scorecard_bowler')
    runs = models.CharField(max_length=3, default=0)
    wickets = models.CharField(max_length=1, default=0)
    overs = models.CharField(max_length=1, default=0)
    extras = models.CharField(max_length=2, default=0)

    def __str__(self):
        return str(self.bowler)

class Tournament_Stats(models.Model):
    sixes = models.CharField(max_length=3, default=0)
    fours = models.CharField(max_length=3, default=0)



