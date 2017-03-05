from django.shortcuts import render,reverse
from django.views import View
from players.forms import PlayerForm
from players.models import Player
import datetime
from django.http import HttpResponseRedirect
from matches.models import Match,Current_Match,Points_Table,Innings,Batting_Scorecard,Bowling_Scorecard,Ball,Tournament_Stats,Over
from auctions.models import Sold_Player
import traceback
from teams.models import Team
# Create your views here.
class Home(View):
    def get(self,request):
        t = datetime.datetime(2017, 2, 15, 15, 0, 0)
        td = t-datetime.datetime.now()
        time = int(td.total_seconds())
        points_table = Points_Table.objects.all().order_by('-points', '-nrr')
        matches = Match.objects.all().order_by('match_number')
        current_match = Current_Match.objects.all()[0]
        current_inning = current_match.inning
        current_over = current_match.over
        tournament_stats = Tournament_Stats.objects.all()[0]
        orange_cap = Sold_Player.objects.filter(runs__gt=0).order_by('-runs','-sixes','-fours')[0:4]
        purple_cap = Sold_Player.objects.filter(wickets__gt=0).order_by('-wickets')[0:4]
        most_sixes = Sold_Player.objects.filter(sixes__gt=0).order_by('-sixes','-runs')[0:4]
        most_fours = Sold_Player.objects.filter(fours__gt=0).order_by('-fours','-runs')[0:4]
        most_catches = Sold_Player.objects.filter(catches__gt=0).order_by('-catches')[0:4]
        try:
            other_inning = Innings.objects.filter(batting=current_match.inning.bowling,
                                                  bowling=current_match.inning.batting)
            print other_inning
            other_over = ""

            if len(other_inning)!=0:
                other_inning = other_inning[0]
                other_over = str(other_inning.balls / 6) + "." + str(other_inning.balls % 6)

            team1 = Sold_Player.objects.filter(team=current_match.inning.batting).order_by('player__name')
            team2 = Sold_Player.objects.filter(team=current_match.inning.bowling).order_by('player__name')
            striker = Batting_Scorecard.objects.filter(batsman=current_over.striker,innings=current_inning)[0]
            non_striker = Batting_Scorecard.objects.filter(batsman=current_over.non_striker,innings=current_inning)[0]
            bowler = Bowling_Scorecard.objects.filter(bowler=current_over.bowler,innings=current_inning)[0]
            cur_over = str(current_inning.balls/6)+"."+str(current_inning.balls%6)
            balls = Ball.objects.filter(over=current_over)
            bowler_over = str(bowler.balls/6)+"."+str(bowler.balls%6)
            batting_lineup = Batting_Scorecard.objects.filter(innings=current_inning)
            bowling_lineup = Bowling_Scorecard.objects.filter(innings=current_inning)
            other_batting_lineup = Batting_Scorecard.objects.filter(innings=other_inning)
            other_bowling_lineup = Bowling_Scorecard.objects.filter(innings=other_inning)
            tot_fours = 0
            tot_sixes = 0
            for batsman in batting_lineup:
                tot_fours += batsman.fours
                tot_sixes += batsman.sixes

            other_tot_fours = 0
            other_tot_sixes = 0
            for batsman in other_batting_lineup:
                other_tot_fours += batsman.fours
                other_tot_sixes += batsman.sixes
            match_started = 'Yes'
        except Exception:
            print(traceback.format_exc())
            other_inning = None
            cur_over = '0.0'
            striker = "Striker"
            non_striker = "Non Striker"
            bowler = "Bowler"
            balls = None
            bowler_over = ""
            tot_fours = 0
            tot_sixes = 0
            other_tot_fours = 0
            other_tot_sixes = 0
            batting_lineup = None
            bowling_lineup = None
            other_batting_lineup = None
            other_bowling_lineup = None
            other_over = '0.0'
            other_inning = None
            team1 = None
            team2 = None
            match_started = None

        context = {
            'time': time,
            'matches' : matches,
            'match_started' : match_started,
            'points_table' : points_table,
            'current_match' : current_match,
            'current_inning' : current_inning,
            'other_inning': other_inning,
            'current_over' : current_over,
            'other_over' : other_over,
            'team1' : team1,
            'team2' : team2,
            'cur_over' : cur_over,
            'striker' : striker,
            'non_striker' : non_striker,
            'bowler' : bowler,
            'balls' : balls,
            'bowler_over' : bowler_over,
            'batting_lineup' : batting_lineup,
            'bowling_lineup' : bowling_lineup,
            'other_batting_lineup': other_batting_lineup,
            'other_bowling_lineup': other_bowling_lineup,
            'tot_fours' : tot_fours,
            'tot_sixes' : tot_sixes,
            'other_tot_fours': other_tot_fours,
            'other_tot_sixes': other_tot_sixes,
            'tournament_stats': tournament_stats,
            'orange_cap' : orange_cap,
            'purple_cap' : purple_cap,
            'most_sixes' : most_sixes,
            'most_fours' : most_fours,
            'most_catches' : most_catches,

        }
        return render(request,"index.html",context)

class Rules(View):
    def get(self,request):
        return render(request,"rules.html",{})

class Players(View):
    def get(self,request):
        players = Player.objects.all()
        return render(request,"players.html",{'players':players})

class Register(View):
    def get(self,request):
        player_form = PlayerForm()
        return render(request,"register.html",{'player_form':player_form})
    def post(self,request):
        player_form = PlayerForm(request.POST,request.FILES)
        if player_form.is_valid():
            form_obj = player_form.save(commit=False)
            form_obj.save()
            return render(request, "register_success.html", {})
        else:
            player_form = PlayerForm()
            context = {
                'player_form': player_form,
                'error_message':'There was an error in the details you provided. Please provide full name and proper image.',
            }
            return render(request, "register.html", context)

class Organizers(View):
    def get(self,request):
        return render(request,"organizers.html",{})

class Match_Details(View):
    def get(self,request,match):
        t = datetime.datetime(2017, 2, 15, 15, 0, 0)
        td = t-datetime.datetime.now()
        time = int(td.total_seconds())
        matches = Match.objects.all().order_by('match_number')
        current_match = Match.objects.get(id=match)
        current_inning = current_match.first_innings
        current_over = Over.objects.filter(innings=current_inning).last()
        try:
            other_inning = Innings.objects.filter(batting=current_inning.bowling,
                                                  bowling=current_inning.batting)
            other_over = ""

            if len(other_inning)!=0:
                other_inning = other_inning[0]
                other_over = str(other_inning.balls / 6) + "." + str(other_inning.balls % 6)

            team1 = Sold_Player.objects.filter(team=current_inning.batting).order_by('player__name')
            team2 = Sold_Player.objects.filter(team=current_inning.bowling).order_by('player__name')
            striker = Batting_Scorecard.objects.filter(batsman=current_over.striker,innings=current_inning)[0]
            non_striker = Batting_Scorecard.objects.filter(batsman=current_over.non_striker,innings=current_inning)[0]
            bowler = Bowling_Scorecard.objects.filter(bowler=current_over.bowler,innings=current_inning)[0]
            cur_over = str(current_inning.balls/6)+"."+str(current_inning.balls%6)
            balls = Ball.objects.filter(over=current_over)
            bowler_over = str(bowler.balls/6)+"."+str(bowler.balls%6)
            batting_lineup = Batting_Scorecard.objects.filter(innings=current_inning)
            bowling_lineup = Bowling_Scorecard.objects.filter(innings=current_inning)
            other_batting_lineup = Batting_Scorecard.objects.filter(innings=other_inning)
            other_bowling_lineup = Bowling_Scorecard.objects.filter(innings=other_inning)
            tot_fours = 0
            tot_sixes = 0
            for batsman in batting_lineup:
                tot_fours += batsman.fours
                tot_sixes += batsman.sixes

            other_tot_fours = 0
            other_tot_sixes = 0
            for batsman in other_batting_lineup:
                other_tot_fours += batsman.fours
                other_tot_sixes += batsman.sixes
            match_started = 'Yes'
        except Exception:
            print(traceback.format_exc())
            other_inning = None
            cur_over = '0.0'
            striker = "Striker"
            non_striker = "Non Striker"
            bowler = "Bowler"
            balls = None
            bowler_over = ""
            tot_fours = 0
            tot_sixes = 0
            other_tot_fours = 0
            other_tot_sixes = 0
            batting_lineup = None
            bowling_lineup = None
            other_batting_lineup = None
            other_bowling_lineup = None
            other_over = '0.0'
            other_inning = None
            team1 = None
            team2 = None
            match_started = None

        context = {
            'time': time,
            'matches' : matches,
            'match_started' : match_started,
            'current_match' : current_match,
            'current_inning' : current_inning,
            'other_inning': other_inning,
            'current_over' : current_over,
            'other_over' : other_over,
            'team1' : team1,
            'team2' : team2,
            'cur_over' : cur_over,
            'striker' : striker,
            'non_striker' : non_striker,
            'bowler' : bowler,
            'balls' : balls,
            'bowler_over' : bowler_over,
            'batting_lineup' : batting_lineup,
            'bowling_lineup' : bowling_lineup,
            'other_batting_lineup': other_batting_lineup,
            'other_bowling_lineup': other_bowling_lineup,
            'tot_fours' : tot_fours,
            'tot_sixes' : tot_sixes,
            'other_tot_fours': other_tot_fours,
            'other_tot_sixes': other_tot_sixes,

        }
        return render(request,"match_details.html",context)