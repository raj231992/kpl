from django.shortcuts import render
from django.views import View
from .models import Team
# Create your views here.


class Team_Display(View):
    def get(self,request):
        teams = Team.objects.all()
        context = {
            'teams':teams
        }
        return render(request,'teams.html',context)
