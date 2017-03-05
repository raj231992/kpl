from django import forms
from matches.models import Match, Current_Match, Ball
from teams.models import Team
from auctions.models import Sold_Player
from django.db.models import Q
import traceback


class New_Match_Form(forms.Form):
    match = forms.ModelChoiceField(queryset=Match.objects.all().order_by('match_number'))
    toss_won = forms.ModelChoiceField(queryset=Team.objects.all())
    toss_choice = (
        ('Bat', 'Bat'),
        ('Field', 'Field'),
    )
    choose = forms.ChoiceField(choices=toss_choice)


class First_Over_Form(forms.Form):
    try:
        superover_choice = (
            ('No', 'No'),
            ('Yes', 'Yes'),

        )
        super_over = forms.ChoiceField(choices=superover_choice)
        cur_match = Current_Match.objects.all()[0]
        batting_team = cur_match.inning.batting
        bowling_team = cur_match.inning.bowling
        striker = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=batting_team).exclude(player__gender='Female').order_by('player'))
        non_striker = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=batting_team).exclude(player__gender='Female').order_by('player'))
        bowler = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=bowling_team).exclude(player__gender='Female').order_by('player'))

        def __init__(self, *args, **kwargs):
            cur_match = Current_Match.objects.all()[0]
            batting_team = cur_match.inning.batting
            bowling_team = cur_match.inning.bowling
            super(First_Over_Form, self).__init__(*args, **kwargs)
            self.fields['striker'].queryset = Sold_Player.objects.filter(team=batting_team).exclude(
                player__gender='Female').order_by('player')
            self.fields['non_striker'].queryset = Sold_Player.objects.filter(team=batting_team).exclude(
                player__gender='Female').order_by('player')
            self.fields['bowler'].queryset = Sold_Player.objects.filter(team=bowling_team).exclude(
                player__gender='Female').order_by('player')
    except:
        traceback.print_exc()


class New_Over_Form(forms.Form):
    try:
        superover_choice = (
            ('No', 'No'),
            ('Yes', 'Yes'),

        )
        super_over = forms.ChoiceField(choices=superover_choice)
        cur_match = Current_Match.objects.all()[0]
        batting_team = cur_match.inning.batting
        bowling_team = cur_match.inning.bowling
        striker = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=batting_team).exclude(player__gender='Female').order_by('player'))
        non_striker = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=batting_team).exclude(player__gender='Female').order_by('player'))
        bowler = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=bowling_team).exclude(player__gender='Female').order_by('player'))

        def __init__(self, *args, **kwargs):
            cur_match = Current_Match.objects.all()[0]
            batting_team = cur_match.inning.batting
            bowling_team = cur_match.inning.bowling
            super(New_Over_Form, self).__init__(*args, **kwargs)
            self.fields['striker'].queryset = Sold_Player.objects.filter(team=batting_team).exclude(
                player__gender='Female').order_by('player')
            self.fields['striker'].initial = cur_match.over.striker
            self.fields['non_striker'].queryset = Sold_Player.objects.filter(team=batting_team).exclude(
                player__gender='Female').order_by('player')
            self.fields['non_striker'].initial = cur_match.over.non_striker
            self.fields['bowler'].queryset = Sold_Player.objects.filter(team=bowling_team).exclude(
                player__gender='Female').order_by('player')
    except:
        pass


class New_Ball_Form(forms.ModelForm):
    class Meta:
        model = Ball
        exclude = ('over', 'wicket_details',)


class Bold_Wicket_Form(forms.Form):
    try:
        cur_match = Current_Match.objects.all()[0]
        batting_team = cur_match.inning.batting
        next_batsman = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=batting_team).exclude(player__gender='Female').order_by('player'))

        def __init__(self, *args, **kwargs):
            cur_match = Current_Match.objects.all()[0]
            batting_team = cur_match.inning.batting
            super(Bold_Wicket_Form, self).__init__(*args, **kwargs)
            self.fields['next_batsman'].queryset = Sold_Player.objects.filter(team=batting_team).exclude(
                player__gender='Female').order_by('player')
    except:
        pass


class Hit_Wicket_Form(forms.Form):
    try:
        cur_match = Current_Match.objects.all()[0]
        batting_team = cur_match.inning.batting
        next_batsman = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=batting_team).exclude(player__gender='Female').order_by('player'))

        def __init__(self, *args, **kwargs):
            cur_match = Current_Match.objects.all()[0]
            batting_team = cur_match.inning.batting
            super(Hit_Wicket_Form, self).__init__(*args, **kwargs)
            self.fields['next_batsman'].queryset = Sold_Player.objects.filter(team=batting_team).exclude(
                player__gender='Female').order_by('player')
    except:
        pass


class Catch_Wicket_Form(forms.Form):
    try:
        striker_choice = (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )
        cur_match = Current_Match.objects.all()[0]
        batting_team = cur_match.inning.batting
        bowling_team = cur_match.inning.bowling
        caught_by = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=bowling_team).exclude(player__gender='Female').order_by('player'))
        next_batsman = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=batting_team).exclude(player__gender='Female').order_by('player'))
        striker = forms.ChoiceField(choices=striker_choice)

        def __init__(self, *args, **kwargs):
            cur_match = Current_Match.objects.all()[0]
            batting_team = cur_match.inning.batting
            bowling_team = cur_match.inning.bowling
            super(Catch_Wicket_Form, self).__init__(*args, **kwargs)
            self.fields['next_batsman'].queryset = Sold_Player.objects.filter(team=batting_team).exclude(
                player__gender='Female').order_by('player')
            self.fields['caught_by'].queryset = Sold_Player.objects.filter(team=bowling_team).exclude(
                player__gender='Female').order_by('player')
    except:
        pass


class Runout_Wicket_Form(forms.Form):
    try:
        striker_choice = (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )
        cur_match = Current_Match.objects.all()[0]
        batting_team = cur_match.inning.batting
        bowling_team = cur_match.inning.bowling
        batsman_out = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=batting_team).exclude(player__gender='Female').order_by('player'))
        runout_by = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=bowling_team).exclude(player__gender='Female').order_by('player'))
        next_batsman = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=batting_team).exclude(player__gender='Female').order_by('player'))
        striker = forms.ChoiceField(choices=striker_choice)

        def __init__(self, *args, **kwargs):
            cur_match = Current_Match.objects.all()[0]
            batting_team = cur_match.inning.batting
            bowling_team = cur_match.inning.bowling
            super(Runout_Wicket_Form, self).__init__(*args, **kwargs)
            self.fields['next_batsman'].queryset = Sold_Player.objects.filter(team=batting_team).exclude(
                player__gender='Female').order_by('player')
            self.fields['batsman_out'].queryset = Sold_Player.objects.filter(team=batting_team).exclude(
                player__gender='Female').order_by('player')
            self.fields['runout_by'].queryset = Sold_Player.objects.filter(team=bowling_team).exclude(
                player__gender='Female').order_by('player')
    except:
        pass


class Stumped_Wicket_Form(forms.Form):
    try:
        cur_match = Current_Match.objects.all()[0]
        batting_team = cur_match.inning.batting
        bowling_team = cur_match.inning.bowling
        wicket_keeper = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=bowling_team).exclude(player__gender='Female').order_by('player'))
        next_batsman = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=batting_team).exclude(player__gender='Female').order_by('player'))

        def __init__(self, *args, **kwargs):
            cur_match = Current_Match.objects.all()[0]
            batting_team = cur_match.inning.batting
            bowling_team = cur_match.inning.bowling
            super(Stumped_Wicket_Form, self).__init__(*args, **kwargs)
            self.fields['next_batsman'].queryset = Sold_Player.objects.filter(team=batting_team).exclude(
                player__gender='Female').order_by('player')
            self.fields['wicket_keeper'].queryset = Sold_Player.objects.filter(team=bowling_team).exclude(
                player__gender='Female').order_by('player')
    except:
        pass


class Female_Over_Form(forms.Form):
    try:
        cur_match = Current_Match.objects.all()[0]
        batting_team = cur_match.inning.batting
        bowling_team = cur_match.inning.bowling
        female_batsman = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=batting_team).exclude(player__gender='Male').order_by('player'))
        non_striker = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=batting_team).exclude(player__gender='Female').order_by('player'))
        female_bowler = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=bowling_team).exclude(player__gender='Male').order_by('player'))

        def __init__(self, *args, **kwargs):
            cur_match = Current_Match.objects.all()[0]
            batting_team = cur_match.inning.batting
            bowling_team = cur_match.inning.bowling
            super(Female_Over_Form, self).__init__(*args, **kwargs)
            self.fields['female_batsman'].queryset = Sold_Player.objects.filter(team=batting_team).exclude(
                player__gender='Male').order_by('player')
            self.fields['non_striker'].queryset = Sold_Player.objects.filter(team=batting_team).exclude(
                player__gender='Female').order_by('player')
            self.fields['female_bowler'].queryset = Sold_Player.objects.filter(team=bowling_team).exclude(
                player__gender='Male').order_by('player')
    except:
        pass

class Retire_Player_Form(forms.Form):
    try:
        cur_match = Current_Match.objects.all()[0]
        batting_team = cur_match.inning.batting
        next_batsman = forms.ModelChoiceField(
            queryset=Sold_Player.objects.filter(team=batting_team).exclude(player__gender='Female').order_by('player'))

        def __init__(self, *args, **kwargs):
            cur_match = Current_Match.objects.all()[0]
            batting_team = cur_match.inning.batting
            super(Retire_Player_Form, self).__init__(*args, **kwargs)
            self.fields['next_batsman'].queryset = Sold_Player.objects.filter(team=batting_team).exclude(
                player__gender='Female').order_by('player')
    except:
        pass

class End_Match_Form(forms.Form):
    try:
        cur_match = Current_Match.objects.all()[0]
        players = []
        team1 = Sold_Player.objects.filter(team=cur_match.inning.batting).order_by('player')
        team2 = Sold_Player.objects.filter(team=cur_match.inning.bowling).order_by('player')
        for player in team1:
            players.append(player.id)
        for player in team2:
            players.append(player.id)
        players = Sold_Player.objects.filter(id__in=players)
        man_of_match = forms.ModelChoiceField(queryset=players)

        def __init__(self, *args, **kwargs):
            cur_match = Current_Match.objects.all()[0]
            players = []
            team1 = Sold_Player.objects.filter(team=cur_match.inning.batting).order_by('player')
            team2 = Sold_Player.objects.filter(team=cur_match.inning.bowling).order_by('player')
            for player in team1:
                players.append(player.id)
            for player in team2:
                players.append(player.id)
            players = Sold_Player.objects.filter(id__in=players)
            super(End_Match_Form, self).__init__(*args, **kwargs)
            self.fields['man_of_match'].queryset=players
    except:
        pass
