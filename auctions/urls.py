from django.conf.urls import url
from .views import (Current_Player_Data,Auction,Unsold_Player_Data,Refresh_Player_Data,
                    Sold_Player_Data,Team_Money,Top_Sold_Player_Data,Start_Auction,
                    Skip_Player,Sell_Player)
urlpatterns = [
    url(r'^current_player/$', Current_Player_Data.as_view()),
    url(r'^unsold_players/$', Unsold_Player_Data.as_view()),
    url(r'^refresh_players/$', Refresh_Player_Data.as_view()),
    url(r'^sold_players/$', Sold_Player_Data.as_view()),
    url(r'^top_sold_players/$', Top_Sold_Player_Data.as_view()),
    url(r'^team_money/$', Team_Money.as_view()),
    url(r'^start_auction/$', Start_Auction.as_view()),
    url(r'^skip_player/$', Skip_Player.as_view()),
    url(r'^sell_player/$', Sell_Player.as_view()),
    url(r'^$', Auction.as_view()),
]