from django.shortcuts import render
from .models import Match
from django.views import View
# Create your views here.

class Match_Display(View):
    def get(self,request):
        matches = Match.objects.all().order_by('id')
        return render(request,'schedule.html',{'matches':matches})
