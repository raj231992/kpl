from django.shortcuts import render
from django.views import View
from .models import Team
from auctions.models import Sold_Player
# Create your views here.


class Team_Display(View):
    def get(self,request):
        teams = Team.objects.all()
        context = {
            'teams':teams
        }
        return render(request,'teams.html',context)

class Team_Players(View):
    def get(self,request,pk):
        team = Team.objects.get(pk=pk)
        manager = team.manager
        players = Sold_Player.objects.filter(team=team).order_by('player__name')
        context = {
            'team':team,
            'manager':manager,
            'players':players,
        }
        return render(request,'team_players.html',context)
