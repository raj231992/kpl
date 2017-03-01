from django.contrib import admin
from .models import Match,Extra,Over,Ball,Wicket,Batting_Scorecard,Bowling_Scorecard,Tournament_Stats,Innings
# Register your models here.

class Match_Admin(admin.ModelAdmin):
    list_display = ['match_number','team1','team2']
    class Meta:
        model = Match
        ordering = ('-match_number')

admin.site.register(Match,Match_Admin)
admin.site.register(Innings)
admin.site.register(Over)
admin.site.register(Ball)
admin.site.register(Wicket)
admin.site.register(Extra)
admin.site.register(Batting_Scorecard)
admin.site.register(Bowling_Scorecard)
admin.site.register(Tournament_Stats)
