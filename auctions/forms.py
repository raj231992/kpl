from django.forms import ModelForm
from .models import Sold_Player,Current_Player

class Player_Auction_Form(ModelForm):
    class Meta:
        exclude = ['player']
        model = Sold_Player