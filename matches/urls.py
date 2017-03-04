from django.conf.urls import url
from .views import (Match_Display,New_Match,New_Over,New_Ball,Bold_Wicket,Caught_Wicket,Runout_Wicket,Stumped_Wicket,
                    Hit_Wicket,First_Over,Female_Over,End_First_Innings,Retire_Player,End_Match,Clear_Stats)

urlpatterns = [
    url(r'^schedule/$', Match_Display.as_view(),name='schedule'),
    url(r'^new_match/$', New_Match.as_view(),name='new_match'),
    url(r'^first_over/$', First_Over.as_view(),name='first_over'),
    url(r'^new_over/$', New_Over.as_view(),name='new_over'),
    url(r'^female_over/$', Female_Over.as_view(),name='female_over'),
    url(r'^new_ball/$', New_Ball.as_view(),name='new_ball'),
    url(r'^wicket_bold/$', Bold_Wicket.as_view(),name='bold_wicket'),
    url(r'^wicket_caught/$', Caught_Wicket.as_view(),name='caught_wicket'),
    url(r'^wicket_runout/$', Runout_Wicket.as_view(),name='runout_wicket'),
    url(r'^wicket_stumped/$', Stumped_Wicket.as_view(),name='stumped_wicket'),
    url(r'^wicket_hit/$', Hit_Wicket.as_view(),name='hit_wicket'),
    url(r'^retire_player/$', Retire_Player.as_view(),name='retire_player'),
    url(r'^end_first_inning/$', End_First_Innings.as_view(),name='end_first_inning'),
    url(r'^end_match/$', End_Match.as_view(),name='end_match'),
    url(r'^clear_stats/$', Clear_Stats.as_view(),name='clear_stats'),
]