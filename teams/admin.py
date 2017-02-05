from django.contrib import admin
from .models import Team,Member
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name','manager','captain','money']
    class Meta:
        model = Team

class MemberAdmin(admin.ModelAdmin):
    list_display = ['team','player','price']
    class Meta:
        model = Member

admin.site.register(Team,TeamAdmin)
admin.site.register(Member,MemberAdmin)

