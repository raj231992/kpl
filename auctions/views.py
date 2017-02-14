from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from players.models import Player
from teams.models import Team
from .serializers import Current_Player_Serializer,Unsold_Player_Serializer,Refresh_Data_Serializer,Sold_Player_Serializer,Team_Serializer
from .models import Current_Player,Refresh_Data,Sold_Player
from .forms import Player_Auction_Form
from django.http import HttpResponseRedirect
import random
# Create your views here.

class Auction(View):
    def get(self,request):
        player_form = Player_Auction_Form()
        admin = User.objects.get(username='raj')
        context={
            'player_form':player_form,
            'admin':admin
        }
        return render(request,"auction.html",context)
class Start_Auction(View):
    def get(self,request):
        if request.user.username =='raj':
            players = Player.objects.all()
            for player in players:
                player.auction_status = 'pending'
                player.save()
            teams = Team.objects.all()
            for team in teams:
                team.players_cost = 0
                team.manager_cost = 0
                team.money = 3000
                team.save()
            players = Player.objects.filter(auction_status='pending',pool='A').exclude(gender='Female').exclude(manager='Yes')
            tot = len(players)
            player = players[random.randint(0,tot-1)]
            Sold_Player.objects.all().delete()
            Current_Player.objects.all().delete()
            current_player = Current_Player(current_player=player)
            current_player.save()
            refresh = Refresh_Data.objects.get(id=1)
            if refresh.refresh == '0':
                refresh.refresh = '1'
            else:
                refresh.refresh = '0'
            refresh.save()
        return HttpResponseRedirect('/kpl/auction/')
class Skip_Player(View):
    def get(self, request):
        players = Player.objects.filter(auction_status='pending', pool='A').exclude(gender='Female').exclude(manager='Yes')
        tot = len(players)
        if tot>0:
            player = players[random.randint(0, tot - 1)]
        else:
            players = Player.objects.filter(auction_status='pending', pool='B').exclude(gender='Female').exclude(manager='Yes')
            tot = len(players)
            player = players[random.randint(0, tot - 1)]
        current_player = Current_Player.objects.all()
        current_player[0].delete()
        cur_player = Current_Player(current_player=player)
        cur_player.save()
        refresh = Refresh_Data.objects.get(id=1)
        if refresh.refresh == '0':
            refresh.refresh = '1'
        else:
            refresh.refresh = '0'
        refresh.save()
        return HttpResponseRedirect('/kpl/auction/')
class Sell_Player(View):
    def post(self,request):
        try:
            player = Current_Player.objects.all()[0]
            team = Team.objects.get(id=request.POST['team'])
            price = int(request.POST['price'])
            sold_player = Sold_Player(player=player.current_player,team=team,price=price)
            sold_player.save()
            player.current_player.auction_status = 'sold'
            player.current_player.save()
            team.players_cost+=price
            costliest_player = Sold_Player.objects.filter(team=team).order_by('-price')[0]
            if team.manager_only=='No':
                team.manager_cost = 0.75*costliest_player.price
            team.money = 3000-(team.players_cost+team.manager_cost)
            team.save()
            refresh = Refresh_Data.objects.get(id=1)
            players = Player.objects.filter(auction_status='pending', pool='A').exclude(gender='Female').exclude(manager='Yes')
            tot = len(players)
            if tot > 0:
                player = players[random.randint(0, tot - 1)]
            else:
                players = Player.objects.filter(auction_status='pending', pool='B').exclude(gender='Female').exclude(manager='Yes')
                tot = len(players)
                player = players[random.randint(0, tot - 1)]
            Current_Player.objects.all().delete()
            cur_player = Current_Player(current_player=player)
            cur_player.save()
            if refresh.refresh == '0':
                refresh.refresh = '1'
            else:
                refresh.refresh = '0'
            refresh.save()
        except:
            Current_Player.objects.all().delete()
            refresh = Refresh_Data.objects.get(id=1)
            if refresh.refresh == '0':
                refresh.refresh = '1'
            else:
                refresh.refresh = '0'
            refresh.save()
        return HttpResponseRedirect('/kpl/auction/')
class Current_Player_Data(APIView):
    def get(self,request):
        player = Current_Player.objects.all()[0]
        player_obj = Current_Player_Serializer(player.current_player)
        return Response({'current_player':player_obj.data},status=200)
class Unsold_Player_Data(APIView):
    def get(self,request):
        players = Player.objects.filter(auction_status='pending').exclude(gender='Female').exclude(manager='Yes').order_by('pool','name')
        player_obj = Unsold_Player_Serializer(players,many=True)
        return Response(data=player_obj.data,status=200)
class Sold_Player_Data(APIView):
    def get(self,request):
        sold_players = Sold_Player.objects.all().order_by('-id')
        sold_player_obj = Sold_Player_Serializer(sold_players,many=True)
        return Response(data=sold_player_obj.data,status=200)
class Top_Sold_Player_Data(APIView):
    def get(self,request):
        top_sold_players = Sold_Player.objects.all().order_by('-price')[:8]
        top_sold_player_obj = Sold_Player_Serializer(top_sold_players,many=True)
        return Response(data=top_sold_player_obj.data,status=200)
class Refresh_Player_Data(APIView):
    def get(self,request):
        refresh = Refresh_Data.objects.all()[0]
        refresh_obj = Refresh_Data_Serializer(refresh)
        return Response({'refresh':refresh_obj.data},status=200)

class Team_Money(APIView):
    def get(self,request):
        teams = Team.objects.all().order_by('-money','name')
        team_obj = Team_Serializer(teams,many=True)
        return Response(data=team_obj.data, status=200)




