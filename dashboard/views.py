from django.shortcuts import render,reverse
from django.views import View
from players.forms import PlayerForm
from players.models import Player
import datetime
from django.http import HttpResponseRedirect
# Create your views here.
class Home(View):
    def get(self,request):
        t = datetime.datetime(2017, 2, 15, 15, 0, 0)
        td = t-datetime.datetime.now()
        time = int(td.total_seconds())
        print time
        return render(request,"index.html",{'time':time})

class Rules(View):
    def get(self,request):
        return render(request,"rules.html",{})

class Players(View):
    def get(self,request):
        players = Player.objects.all()
        return render(request,"players.html",{'players':players})

class Register(View):
    def get(self,request):
        player_form = PlayerForm()
        return render(request,"register.html",{'player_form':player_form})
    def post(self,request):
        player_form = PlayerForm(request.POST,request.FILES)
        if player_form.is_valid():
            form_obj = player_form.save(commit=False)
            form_obj.save()
            return render(request, "register_success.html", {})
        else:
            player_form = PlayerForm()
            context = {
                'player_form': player_form,
                'error_message':'There was an error in the details you provided. Please provide full name and proper image.',
            }
            return render(request, "register.html", context)

class Organizers(View):
    def get(self,request):
        return render(request,"organizers.html",{})