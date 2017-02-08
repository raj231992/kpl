from django.conf.urls import url
from .views import Current_Player_Data,Auction,Unsold_Player_Data,Refresh_Player_Data,Sold_Player_Data,Team_Money,Top_Sold_Player_Data
urlpatterns = [
    url(r'^current_player/$', Current_Player_Data.as_view()),
    url(r'^unsold_players/$', Unsold_Player_Data.as_view()),
    url(r'^refresh_players/$', Refresh_Player_Data.as_view()),
    url(r'^sold_players/$', Sold_Player_Data.as_view()),
    url(r'^top_sold_players/$', Top_Sold_Player_Data.as_view()),
    url(r'^team_money/$', Team_Money.as_view()),
    url(r'^$', Auction.as_view()),
]