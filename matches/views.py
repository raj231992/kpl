from django.shortcuts import render, reverse
from .models import Match, Current_Match, Innings, Over, Batting_Scorecard, Bowling_Scorecard, Wicket, Wicket_Type,Points_Table,Tournament_Stats
from django.views import View
from .forms import (New_Match_Form, First_Over_Form, New_Over_Form, Female_Over_Form, New_Ball_Form, Bold_Wicket_Form,
                    Catch_Wicket_Form, Runout_Wicket_Form, Stumped_Wicket_Form, Hit_Wicket_Form,Retire_Player_Form,
                    End_Match_Form)
from teams.models import Team
from django.http import HttpResponseRedirect
from auctions.models import Sold_Player


# Create your views here.

class Match_Display(View):
    def get(self, request):
        matches = Match.objects.all().order_by('match_number')
        return render(request, 'schedule.html', {'matches': matches})


class New_Match(View):
    def get(self, request):
        new_match_form = New_Match_Form()
        return render(request, 'new_match.html', {'new_match_form': new_match_form})

    def post(self, request):
        new_match_form = New_Match_Form(request.POST)
        if new_match_form.is_valid():
            match_number = int(str(new_match_form.cleaned_data['match']))
            toss_won = new_match_form.cleaned_data['toss_won']
            choose = new_match_form.cleaned_data['choose']
            print match_number
            match = Match.objects.get(match_number=match_number)
            team = Team.objects.get(name=toss_won)
            match.toss_won = team
            print choose
            match.selected_to = choose
            if team == match.team1:
                if choose == 'Bat':
                    batting = match.team1
                    bowling = match.team2
                else:
                    batting = match.team2
                    bowling = match.team1
            else:
                if choose == 'Bat':
                    batting = match.team2
                    bowling = match.team1
                else:
                    batting = match.team1
                    bowling = match.team2

            innings = Innings(batting=batting, bowling=bowling)
            innings.save()
            match.first_innings = innings
            match.save()
            cur_match = Current_Match.objects.all()[0]
            cur_match.match = match
            cur_match.inning = innings
            over = Over(innings=innings)
            over.save()
            cur_match.over = over
            cur_match.save()
            print "helpline"
            return HttpResponseRedirect(reverse('match:first_over'))


class First_Over(View):
    def get(self, request):
        cur_match = Current_Match.objects.all()[0]
        first_over_form = First_Over_Form()
        return render(request, 'first_over.html', {'first_over_form': first_over_form})

    def post(self, request):
        first_over_form = First_Over_Form(request.POST)
        if first_over_form.is_valid():
            cur_match = Current_Match.objects.all()[0]
            cur_inning = cur_match.inning
            super_over = first_over_form.cleaned_data['super_over']
            striker = first_over_form.cleaned_data['striker']
            non_striker = first_over_form.cleaned_data['non_striker']
            bowler = first_over_form.cleaned_data['bowler']
            over_cnt = int(cur_inning.balls / 6)
            over = Over(innings=cur_inning, super_over=super_over, striker=striker, non_striker=non_striker,
                        bowler=bowler, over=over_cnt + 1)
            over.save()
            cur_match.over = over
            cur_match.save()
            batting_scorecard = Batting_Scorecard.objects.filter(innings=cur_inning, batsman=striker)
            if len(batting_scorecard) == 0:
                batting_scorecard = Batting_Scorecard(innings=cur_inning, batsman=striker)
                batting_scorecard.save()
            batting_scorecard = Batting_Scorecard.objects.filter(innings=cur_inning, batsman=non_striker)
            if len(batting_scorecard) == 0:
                batting_scorecard = Batting_Scorecard(innings=cur_inning, batsman=non_striker)
                batting_scorecard.save()
            bowling_scorecard = Bowling_Scorecard.objects.filter(innings=cur_inning, bowler=bowler)
            if len(bowling_scorecard) == 0:
                bowling_scorecard = Bowling_Scorecard(innings=cur_inning, bowler=bowler)
                bowling_scorecard.save()
            return HttpResponseRedirect(reverse('match:new_ball'))


class New_Over(View):
    def get(self, request):
        cur_match = Current_Match.objects.all()[0]
        new_over_form = New_Over_Form()
        return render(request, 'new_over.html', {'new_over_form': new_over_form})

    def post(self, request):
        new_over_form = New_Over_Form(request.POST)
        if new_over_form.is_valid():
            cur_match = Current_Match.objects.all()[0]
            cur_inning = cur_match.inning
            cur_over = cur_match.over
            super_over = new_over_form.cleaned_data['super_over']
            striker = new_over_form.cleaned_data['striker']
            non_striker = new_over_form.cleaned_data['non_striker']
            bowler = new_over_form.cleaned_data['bowler']
            over_cnt = int(cur_inning.balls / 6)
            over = Over(innings=cur_inning, super_over=super_over, striker=striker,
                        non_striker=non_striker, bowler=bowler, over=over_cnt + 1)
            over.save()
            cur_match.over = over
            cur_match.save()

            batting_scorecard = Batting_Scorecard.objects.filter(innings=cur_inning, batsman=striker)
            if len(batting_scorecard) == 0:
                batting_scorecard = Batting_Scorecard(innings=cur_inning, batsman=striker)
                batting_scorecard.save()
            batting_scorecard = Batting_Scorecard.objects.filter(innings=cur_inning, batsman=non_striker)
            if len(batting_scorecard) == 0:
                batting_scorecard = Batting_Scorecard(innings=cur_inning, batsman=non_striker)
                batting_scorecard.save()
            bowling_scorecard = Bowling_Scorecard.objects.filter(innings=cur_inning, bowler=bowler)
            if len(bowling_scorecard) == 0:
                bowling_scorecard = Bowling_Scorecard(innings=cur_inning, bowler=bowler)
                bowling_scorecard.save()
            return HttpResponseRedirect(reverse('match:new_ball'))


class Female_Over(View):
    def get(self, request):
        cur_match = Current_Match.objects.all()[0]
        female_over_form = Female_Over_Form()
        return render(request, 'female_over.html', {'female_over_form': female_over_form})

    def post(self, request):
        female_over_form = Female_Over_Form(request.POST)
        if female_over_form.is_valid():
            cur_match = Current_Match.objects.all()[0]
            cur_inning = cur_match.inning
            cur_over = cur_match.over
            batsman = female_over_form.cleaned_data['female_batsman']
            non_striker = female_over_form.cleaned_data['non_striker']
            bowler = female_over_form.cleaned_data['female_bowler']
            over_cnt = int(cur_inning.balls / 6)
            over = Over(innings=cur_inning, super_over='No', striker=batsman, non_striker=non_striker, bowler=bowler,
                        over=over_cnt + 1)
            over.save()
            cur_match.over = over
            cur_match.save()
            striker = batsman
            batting_scorecard = Batting_Scorecard.objects.filter(innings=cur_inning, batsman=striker)
            if len(batting_scorecard) == 0:
                batting_scorecard = Batting_Scorecard(innings=cur_inning, batsman=striker)
                batting_scorecard.save()
            batting_scorecard = Batting_Scorecard.objects.filter(innings=cur_inning, batsman=non_striker)
            if len(batting_scorecard) == 0:
                batting_scorecard = Batting_Scorecard(innings=cur_inning, batsman=non_striker)
                batting_scorecard.save()
            bowling_scorecard = Bowling_Scorecard.objects.filter(innings=cur_inning, bowler=bowler)
            if len(bowling_scorecard) == 0:
                bowling_scorecard = Bowling_Scorecard(innings=cur_inning, bowler=bowler)
                bowling_scorecard.save()
            return HttpResponseRedirect(reverse('match:new_ball'))


class New_Ball(View):
    def get(self, request):
        cur_match = Current_Match.objects.all()[0]
        balls = cur_match.inning.balls
        if balls==30:
            female_player = Batting_Scorecard.objects.get(innings=cur_match.inning, batsman__player__gender='Female')
            female_player.retired = 'Yes'
            female_player.save()
        if cur_match.inning == cur_match.match.first_innings:
            if balls == 48 or cur_match.inning.wickets == 6:
                return HttpResponseRedirect(reverse('match:end_first_inning'))
        if cur_match.inning == cur_match.match.second_innings:
            if balls == 48 or cur_match.inning.wickets == 6 or cur_match.match.second_innings.runs>cur_match.match.first_innings.runs:
                winner = None
                if balls == 48 or cur_match.inning.wickets == 6:
                    winner = cur_match.inning.bowling
                else:
                    winner = cur_match.inning.batting
                cur_match.match.won = winner
                cur_match.match.save()
                winning_team = Points_Table.objects.get(team=winner)
                winning_team.won += 1
                winning_team.played += 1
                winning_team.points += 3
                losing_team = None
                nrr = 0
                if cur_match.match.first_innings.batting.id == winning_team.id:
                    losing_team = cur_match.match.first_innings.bowling
                    nrr = (cur_match.match.first_innings.runs/float(cur_match.match.first_innings.balls))-(cur_match.match.second_innings.runs / float(cur_match.match.second_innings.balls))
                else:
                    losing_team = cur_match.match.first_innings.batting
                    nrr = -(cur_match.match.first_innings.runs / float(cur_match.match.first_innings.balls)) + (
                    cur_match.match.second_innings.runs / float(cur_match.match.second_innings.balls))
                print losing_team,winning_team,cur_match.match.first_innings.batting
                losing_team = Points_Table.objects.get(team=losing_team)
                losing_team.played += 1
                losing_team.lost += 1
                losing_team.nrr += round(-nrr,2)
                winning_team.nrr += round(nrr,2)
                winning_team.save()
                losing_team.save()
                return HttpResponseRedirect(reverse('match:end_match'))
        if cur_match.over.super_over=='No':
            striker = Batting_Scorecard.objects.get(innings=cur_match.inning,batsman=cur_match.over.striker)
            non_striker = Batting_Scorecard.objects.get(innings=cur_match.inning,batsman=cur_match.over.non_striker)
            if striker.runs>30 :
                if striker.retired == 'Yes' and striker.come_back == 'Yes':
                    striker.retired='No'
                    striker.save()
                if striker.come_back=='No':
                    return HttpResponseRedirect(reverse('match:retire_player'))
            if non_striker.runs > 30:
                if non_striker.retired == 'Yes' and non_striker.come_back == 'Yes':
                    non_striker.retired = 'No'
                    non_striker.save()
                if non_striker.come_back == 'No':
                    return HttpResponseRedirect(reverse('match:retire_player'))
        if balls==24 and cur_match.over.striker.player.gender=='Male':
            return HttpResponseRedirect(reverse('match:female_over'))
        if balls % 6 == 0 and cur_match.over.over != int(balls / 6) + 1:
            cur_match = Current_Match.objects.all()[0]
            cur_match.over.striker, cur_match.over.non_striker = cur_match.over.non_striker, cur_match.over.striker
            cur_match.over.save()
            return HttpResponseRedirect(reverse('match:new_over'))

        new_ball_form = New_Ball_Form()
        return render(request, 'new_ball.html', {'new_ball_form': new_ball_form})

    def post(self, request):
        cur_match = Current_Match.objects.all()[0]
        cur_over = cur_match.over
        cur_innings = cur_match.inning
        new_ball_form = New_Ball_Form(request.POST)
        new_ball_form_obj = new_ball_form.save(commit=False)
        new_ball_form_obj.over = cur_over
        new_ball_form_obj.save()
        extra = new_ball_form_obj.extra
        runs = int(new_ball_form_obj.run)
        bye = int(new_ball_form_obj.bye)
        overthrows = int(new_ball_form_obj.overthrow)
        wicket = new_ball_form_obj.wicket
        batsman = Batting_Scorecard.objects.get(innings=cur_innings, batsman=cur_over.striker)
        bowler = Bowling_Scorecard.objects.get(innings=cur_innings, bowler=cur_over.bowler)
        tot_runs = runs + overthrows
        tournament = Tournament_Stats.objects.all()[0]
        if bye !=0:
            cur_innings.runs += bye
            cur_innings.extras += bye
        if tot_runs != 0:
            cur_innings.runs += tot_runs
            try:
                if extra.type =='Wide':
                    pass
                else:
                    batsman.runs += tot_runs
                    batsman.batsman.runs += tot_runs
            except:
                batsman.runs += tot_runs
                batsman.batsman.runs += tot_runs
            bowler.runs += tot_runs
        if cur_over.super_over == 'Yes':
            cur_innings.runs += (tot_runs+bye)

        if extra != None:
            cur_innings.extras += 2
            cur_innings.runs += 2
            bowler.extras += 2
        else:
            cur_innings.balls += 1
            batsman.balls += 1
            batsman.batsman.balls += 1
            bowler.balls += 1
            bowler.overs = str(int(bowler.balls / 6)) + "." + str(int(bowler.balls % 6))
        if tot_runs % 2 != 0:
            cur_over.striker, cur_over.non_striker = cur_over.non_striker, cur_over.striker
        if runs == 4 or overthrows == 4:
            batsman.fours += 1
            batsman.batsman.fours += 1
            tournament.fours +=1
            tournament.save()
        if runs == 6 or overthrows == 6:
            batsman.sixes += 1
            batsman.batsman.sixes += 1
            tournament.sixes += 1
            tournament.save()
        cur_match.save()
        batsman.save()
        batsman.batsman.save()
        bowler.save()
        cur_innings.save()
        cur_over.save()
        if cur_match.over.over == 5:
            if tot_runs != 0:
                try:
                    if extra.type == 'Wide':
                        pass

                except:
                    batsman.runs += tot_runs
                    batsman.batsman.runs += tot_runs
                    batsman.save()
                    batsman.batsman.save()
                bowler.runs += tot_runs
                cur_innings.runs += (tot_runs+bye)
                cur_innings.save()
            if tot_runs % 2 != 0:
                cur_over.striker, cur_over.non_striker = cur_over.non_striker, cur_over.striker
                cur_over.save()
            if wicket:
                cur_innings.runs -= 2
                batsman.runs -= 2
                batsman.batsman.runs -= 2
                batsman.save()
                batsman.batsman.save()
                if wicket.type != 'Run Out':
                    bowler.wickets += 1
                    bowler.bowler.wickets += 1
                bowler.runs -= 2
                bowler.save()
                bowler.bowler.save()
                cur_innings.save()
                return HttpResponseRedirect(reverse('match:new_ball'))
        # cur_over.striker.save()
        if wicket:
            if cur_innings.wickets==6 and cur_match.match.first_innings==cur_innings:
                cur_innings.wickets+=1
                bowler.wickets+=1
                bowler.bowler.wickets+=1
                cur_innings.save()
                bowler.save()
                bowler.bowler.save()
                wicket_type = Wicket_Type.objects.get(type='Bold')
                wicket = Wicket(type=wicket_type, player1=bowler.bowler)
                wicket.save()
                batsman.wicket = wicket
                batsman.save()
                return HttpResponseRedirect(reverse('match:end_first_inning'))
            if cur_innings.wickets == 6 and cur_match.match.second_innings == cur_innings:
                cur_innings.wickets += 1
                bowler.wickets += 1
                bowler.bowler.wickets += 1
                cur_innings.save()
                bowler.save()
                bowler.bowler.save()
                wicket_type = Wicket_Type.objects.get(type='Bold')
                wicket = Wicket(type=wicket_type, player1=bowler.bowler)
                wicket.save()
                batsman.wicket = wicket
                batsman.save()
                return HttpResponseRedirect(reverse('match:end_match'))
            if wicket.type == 'Bold':
                return HttpResponseRedirect(reverse('match:bold_wicket'))
            if wicket.type == 'Caught':
                return HttpResponseRedirect(reverse('match:caught_wicket'))
            if wicket.type == 'Run Out':
                return HttpResponseRedirect(reverse('match:runout_wicket'))
            if wicket.type == 'Stumped':
                return HttpResponseRedirect(reverse('match:stumped_wicket'))
            if wicket.type == 'Hit Wicket':
                return HttpResponseRedirect(reverse('match:hit_wicket'))

        return HttpResponseRedirect(reverse('match:new_ball'))


class Bold_Wicket(View):
    def get(self, request):
        bold_wicket_form = Bold_Wicket_Form()
        return render(request, 'bold_wicket.html', {'bold_wicket_form': bold_wicket_form})

    def post(self, request):
        bold_wicket_form = Bold_Wicket_Form(request.POST)
        next_batsman = Sold_Player.objects.get(id=int(request.POST['next_batsman']))
        cur_match = Current_Match.objects.all()[0]
        cur_inning = cur_match.inning
        cur_over = cur_match.over
        batsman = Batting_Scorecard.objects.get(innings=cur_inning, batsman=cur_over.striker)
        bowler = Bowling_Scorecard.objects.get(innings=cur_inning, bowler=cur_over.bowler)
        wicket_type = Wicket_Type.objects.get(type='Bold')
        wicket = Wicket(type=wicket_type, player1=bowler.bowler)
        wicket.save()
        batsman.wicket = wicket
        batsman.save()
        cur_over.striker = next_batsman
        cur_over.save()
        cur_inning.wickets += 1
        cur_inning.save()
        bowler.wickets += 1
        bowler.bowler.wickets += 1
        bowler.save()
        bowler.bowler.save()
        try:
            batting_scorecard = Batting_Scorecard.objects.get(batsman=next_batsman, innings=cur_inning)
            batting_scorecard.come_back = 'Yes'
        except:
            batting_scorecard = Batting_Scorecard(batsman=next_batsman, innings=cur_inning)
        batting_scorecard.save()
        return HttpResponseRedirect(reverse('match:new_ball'))


class Hit_Wicket(View):
    def get(self, request):
        hit_wicket_form = Hit_Wicket_Form()
        return render(request, 'hit_wicket.html', {'hit_wicket_form': hit_wicket_form})

    def post(self, request):
        hit_wicket_form = Hit_Wicket_Form(request.POST)
        next_batsman = Sold_Player.objects.get(id=int(request.POST['next_batsman']))
        cur_match = Current_Match.objects.all()[0]
        cur_inning = cur_match.inning
        cur_over = cur_match.over
        batsman = Batting_Scorecard.objects.get(innings=cur_inning, batsman=cur_over.striker)
        bowler = Bowling_Scorecard.objects.get(innings=cur_inning, bowler=cur_over.bowler)
        wicket_type = Wicket_Type.objects.get(type='Hit Wicket')
        wicket = Wicket(type=wicket_type, player1=bowler.bowler)
        wicket.save()
        batsman.wicket = wicket
        batsman.save()
        cur_over.striker = next_batsman
        cur_over.save()
        cur_inning.wickets += 1
        cur_inning.save()
        bowler.wickets += 1
        bowler.bowler.wickets += 1
        bowler.save()
        bowler.bowler.save()
        try:
            batting_scorecard = Batting_Scorecard.objects.get(batsman=next_batsman, innings=cur_inning)
            batting_scorecard.come_back = 'Yes'
        except:
            batting_scorecard = Batting_Scorecard(batsman=next_batsman, innings=cur_inning)
        batting_scorecard.save()
        return HttpResponseRedirect(reverse('match:new_ball'))


class Caught_Wicket(View):
    def get(self, request):
        catch_wicket_form = Catch_Wicket_Form()
        return render(request, 'catch_wicket.html', {'catch_wicket_form': catch_wicket_form})

    def post(self, request):
        catch_wicket_form = Catch_Wicket_Form(request.POST)
        striker = request.POST['striker']
        next_batsman = Sold_Player.objects.get(id=int(request.POST['next_batsman']))
        caught_by = Sold_Player.objects.get(id=int(request.POST['caught_by']))
        cur_match = Current_Match.objects.all()[0]
        cur_inning = cur_match.inning
        cur_over = cur_match.over
        batsman = Batting_Scorecard.objects.get(innings=cur_inning, batsman=cur_over.striker)
        bowler = Bowling_Scorecard.objects.get(innings=cur_inning, bowler=cur_over.bowler)
        wicket_type = Wicket_Type.objects.get(type='Caught')
        wicket = Wicket(type=wicket_type, player1=bowler.bowler, player2=caught_by)
        wicket.save()
        batsman.wicket = wicket
        batsman.save()
        cur_over.striker = next_batsman
        cur_over.save()
        cur_inning.wickets += 1
        cur_inning.save()
        bowler.wickets += 1
        bowler.bowler.wickets += 1
        bowler.save()
        bowler.bowler.save()
        caught_by.catches += 1
        caught_by.save()
        try:
            batting_scorecard = Batting_Scorecard.objects.get(batsman=next_batsman, innings=cur_inning)
            batting_scorecard.come_back = 'Yes'
        except:
            batting_scorecard = Batting_Scorecard(batsman=next_batsman, innings=cur_inning)
        batting_scorecard.save()
        if striker == 'No':
            cur_over.striker, cur_over.non_striker = cur_over.non_striker, cur_over.striker
            cur_over.save()
        return HttpResponseRedirect(reverse('match:new_ball'))


class Runout_Wicket(View):
    def get(self, request):
        runout_wicket_form = Runout_Wicket_Form()
        return render(request, 'runout_wicket.html', {'runout_wicket_form': runout_wicket_form})

    def post(self, request):
        runout_wicket_form = Runout_Wicket_Form(request.POST)
        striker = request.POST['striker']
        batsman_out = Sold_Player.objects.get(id=int(request.POST['batsman_out']))
        next_batsman = Sold_Player.objects.get(id=int(request.POST['next_batsman']))
        runout_by = Sold_Player.objects.get(id=int(request.POST['runout_by']))
        cur_match = Current_Match.objects.all()[0]
        cur_inning = cur_match.inning
        cur_over = cur_match.over
        batsman = Batting_Scorecard.objects.get(innings=cur_inning, batsman=batsman_out)
        wicket_type = Wicket_Type.objects.get(type='Run Out')
        wicket = Wicket(type=wicket_type, player1=runout_by)
        wicket.save()
        batsman.wicket = wicket
        batsman.save()
        cur_over.save()
        cur_inning.wickets += 1
        cur_inning.save()
        runout_by.runout += 1
        runout_by.save()
        try:
            batting_scorecard = Batting_Scorecard.objects.get(batsman=next_batsman, innings=cur_inning)
            batting_scorecard.come_back = 'Yes'
        except:
            batting_scorecard = Batting_Scorecard(batsman=next_batsman, innings=cur_inning)
        batting_scorecard.save()
        if striker == 'No':
            cur_over.non_striker = next_batsman
            cur_over.save()
        else:
            cur_over.striker = next_batsman
            cur_over.save()
        return HttpResponseRedirect(reverse('match:new_ball'))


class Stumped_Wicket(View):
    def get(self, request):
        stumped_wicket_form = Stumped_Wicket_Form()
        return render(request, 'stumped_wicket.html', {'stumped_wicket_form': stumped_wicket_form})

    def post(self, request):
        runout_wicket_form = Runout_Wicket_Form(request.POST)
        next_batsman = Sold_Player.objects.get(id=int(request.POST['next_batsman']))
        wicketkeeper = Sold_Player.objects.get(id=int(request.POST['wicket_keeper']))
        cur_match = Current_Match.objects.all()[0]
        cur_inning = cur_match.inning
        cur_over = cur_match.over
        batsman = Batting_Scorecard.objects.get(innings=cur_inning, batsman=cur_over.striker)
        bowler = Bowling_Scorecard.objects.get(innings=cur_inning, bowler=cur_over.bowler)
        wicket_type = Wicket_Type.objects.get(type='Stumped')
        wicket = Wicket(type=wicket_type, player1=bowler.bowler, player2=wicketkeeper)
        wicket.save()
        batsman.wicket = wicket
        batsman.save()
        bowler.wickets += 1
        bowler.bowler.wickets += 1
        bowler.save()
        bowler.bowler.save()
        wicketkeeper.runout +=1
        wicketkeeper.save()
        cur_over.striker = next_batsman
        cur_over.save()
        cur_inning.wickets += 1
        cur_inning.save()
        try:
            batting_scorecard = Batting_Scorecard.objects.get(batsman=next_batsman, innings=cur_inning)
            batting_scorecard.come_back = 'Yes'
        except:
            batting_scorecard = Batting_Scorecard(batsman=next_batsman, innings=cur_inning)
        batting_scorecard.save()
        return HttpResponseRedirect(reverse('match:new_ball'))

class End_First_Innings(View):
    def get(self,request):
        return render(request, 'end_first_inning.html', {})
    def post(self,request):
        cur_match = Current_Match.objects.all()[0]
        cur_inning = cur_match.inning
        new_inning = Innings(batting=cur_inning.bowling,bowling=cur_inning.batting)
        new_inning.save()
        cur_match.match.second_innings = new_inning
        cur_match.match.save()
        cur_match.inning = new_inning
        over = Over(innings=new_inning)
        over.save()
        cur_match.over = over
        cur_match.save()
        return HttpResponseRedirect(reverse('match:first_over'))

class End_Match(View):
    def get(self,request):
        end_match_form = End_Match_Form()
        return render(request, 'end_match.html', {'end_match_form' : end_match_form})
    def post(self,request):
        cur_match = Current_Match.objects.all()[0]
        cur_inning = cur_match.inning
        man_of_match = request.POST['man_of_match']
        man_of_match = Sold_Player.objects.get(id=man_of_match)
        cur_match.match.man_of_match=man_of_match
        cur_match.match.save()
        return HttpResponseRedirect(reverse('home'))

class Retire_Player(View):
    def get(self, request):
        retire_player_form = Retire_Player_Form()
        return render(request, 'retire_player.html', {'retire_player_form': retire_player_form})

    def post(self, request):
        retire_player_form = Retire_Player_Form(request.POST)
        next_batsman = Sold_Player.objects.get(id=int(request.POST['next_batsman']))
        cur_match = Current_Match.objects.all()[0]
        cur_inning = cur_match.inning
        cur_over = cur_match.over

        striker = Batting_Scorecard.objects.get(innings=cur_match.inning,
                                                batsman=cur_match.over.striker)
        scorecard = Batting_Scorecard(innings=cur_inning,batsman=next_batsman)
        scorecard.save()
        non_striker = Batting_Scorecard.objects.get(innings=cur_match.inning, batsman=cur_match.over.non_striker)
        if striker.runs > 30:
            prev_batsman = Batting_Scorecard.objects.get(innings=cur_inning,batsman=striker.batsman)
            prev_batsman.retired = 'Yes'
            prev_batsman.save()
            cur_over.striker = next_batsman
            cur_over.save()
        elif non_striker.runs > 30:
            prev_batsman = Batting_Scorecard.objects.get(innings=cur_inning, batsman=non_striker.batsman)
            prev_batsman.retired = 'Yes'
            prev_batsman.save()
            cur_over.non_striker = next_batsman
            cur_over.save()

        return HttpResponseRedirect(reverse('match:new_ball'))

class Clear_Stats(View):
    def get(self, request):
        players = Sold_Player.objects.all()
        for player in players:
            player.runs = 0
            player.wickets = 0
            player.balls = 0
            player.sixes = 0
            player.fours = 0
            player.catches = 0
            player.runout = 0
            player.save()
        tournament_stats = Tournament_Stats.objects.all()[0]
        tournament_stats.sixes = 0
        tournament_stats.fours = 0
        tournament_stats.save()
        points = Points_Table.objects.all()
        for point in points:
            point.won = 0
            point.lost = 0
            point.played = 0
            point.nrr = 0
            point.points = 0
            point.save()
        return HttpResponseRedirect(reverse('home'))

