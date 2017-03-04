from __future__ import unicode_literals

from django.db import models
from teams.models import Team
from auctions.models import Sold_Player

# Create your models here.
class Innings(models.Model):
    batting = models.ForeignKey(Team,related_name='inning_batting')
    bowling = models.ForeignKey(Team,related_name='inning_bowling')
    runs = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    balls = models.IntegerField(default=0)
    extras = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

class Match(models.Model):
    toss_choice = (
        ('Bat','Bat'),
        ('Field','Field'),
    )
    match_number = models.IntegerField()
    date = models.CharField(max_length=50)
    team1 = models.ForeignKey(Team,related_name='match_team2')
    team2 = models.ForeignKey(Team,related_name='match_team1')
    toss_won = models.ForeignKey(Team,related_name='match_toss',blank=True,null=True)
    selected_to = models.CharField(choices=toss_choice,max_length=5,blank=True)
    first_innings = models.ForeignKey(Innings,related_name='match_first_inning',blank=True,null=True)
    second_innings = models.ForeignKey(Innings,related_name='match_second_inning',blank=True,null=True)
    won = models.ForeignKey(Team,related_name='match_won',blank=True,null=True)
    man_of_match = models.ForeignKey(Sold_Player,related_name='match_mom',blank=True,null=True)

    def __str__(self):
        return str(self.match_number)



class Extra(models.Model):
    type = models.CharField(max_length=10)
    def __str__(self):
        return str(self.Extra)

    def __str__(self):
        return str(self.type)


class Wicket_Type(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return str(self.type)

class Wicket(models.Model):
    type = models.ForeignKey(Wicket_Type,related_name='wicket_type')
    player1 = models.ForeignKey(Sold_Player,blank=True,related_name='wicket_player1')
    player2 = models.ForeignKey(Sold_Player,blank=True,related_name='wicket_player2',null=True)

class Over(models.Model):
    superover_choice = (
        ('Yes','Yes'),
        ('No','No'),
    )
    over_choice = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('Super', 'Super'),
    )
    innings = models.ForeignKey(Innings,related_name='over_innings')
    over = models.IntegerField(default=0)
    super_over = models.CharField(choices=superover_choice,max_length=3,default='No')
    striker = models.ForeignKey(Sold_Player,related_name='over_striker',blank=True,null=True)
    non_striker = models.ForeignKey(Sold_Player,related_name='over_non_striker',blank=True,null=True)
    bowler = models.ForeignKey(Sold_Player,related_name='over_bowler',blank=True,null=True)

    def __str__(self):
        return str(self.over)

class Ball(models.Model):
    runs_choice = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
    )
    over = models.ForeignKey(Over,related_name='ball_over',blank=True,null=True)
    run = models.CharField(choices=runs_choice,max_length=1,default='0')
    overthrow = models.CharField(choices=runs_choice,max_length=1,default='0')
    extra = models.ForeignKey(Extra,related_name='ball_extra',blank=True,null=True)
    wicket = models.ForeignKey(Wicket_Type,related_name='wicket_extra',blank=True,null=True)
    wicket_details = models.ForeignKey(Wicket,related_name='wicket_extra',blank=True,null=True)

    def __str__(self):
        return str(self.id)



class Batting_Scorecard(models.Model):
    retired_choice = (
        ('No', 'No'),
        ('Yes', 'Yes'),

    )
    innings = models.ForeignKey(Innings,related_name='batting_innings')
    batsman = models.ForeignKey(Sold_Player,related_name='scorecard_batsman')
    runs = models.IntegerField(default=0)
    balls = models.IntegerField(default=0)
    fours = models.IntegerField(default=0)
    sixes = models.IntegerField(default=0)
    wicket = models.ForeignKey(Wicket,related_name='wicket_batsman',blank=True,null=True)
    retired = models.CharField(choices=retired_choice,max_length=6,default='No')
    come_back = models.CharField(choices=retired_choice,max_length=6,default='No')

    def __str__(self):
        return str(self.batsman)

class Bowling_Scorecard(models.Model):
    innings = models.ForeignKey(Innings,related_name='bowling_innings')
    bowler = models.ForeignKey(Sold_Player,related_name='scorecard_bowler')
    runs = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    balls = models.IntegerField(default=0)
    overs = models.CharField(max_length=3,default='0.0')
    extras = models.IntegerField(default=0)

    def __str__(self):
        return str(self.bowler)

class Tournament_Stats(models.Model):
    sixes = models.IntegerField(default=0)
    fours = models.IntegerField(default=0)

class Points_Table(models.Model):
    team = models.ForeignKey(Team,related_name='pt_team')
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    nrr = models.FloatField()

    def __str__(self):
        return str(self.team)

class Current_Match(models.Model):
    match = models.ForeignKey(Match,related_name='cur_match',blank=True,null=True)
    inning = models.ForeignKey(Innings,related_name='cur_inning',blank=True,null=True)
    over = models.ForeignKey(Over,related_name='cur_over',blank=True,null=True)
    def __str__(self):
        return str(self.match)


