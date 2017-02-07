from rest_framework.serializers import ModelSerializer
from players.models import Player
from .models import Sold_Player,Refresh_Data
from teams.serializers import Team_Serializer

class Current_Player_Serializer(ModelSerializer):
    class Meta:
        fields = ['name','category','prev_exp','kpl_exp','pic']
        model = Player

class Unsold_Player_Serializer(ModelSerializer):
    class Meta:
        fields = ['name', 'category']
        model = Player
class Refresh_Data_Serializer(ModelSerializer):
    class Meta:
        fields = ['refresh']
        model = Refresh_Data
class Sold_Player_Serializer(ModelSerializer):
    player_details = Unsold_Player_Serializer(source='player')
    team_details = Team_Serializer(source='team')
    class Meta:
        fields = ['player_details','team_details', 'price']
        model = Sold_Player
