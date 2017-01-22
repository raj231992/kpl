from django.contrib import admin
from .models import Player
# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name','category','phone_no')
    class Meta:
        model = Player

admin.site.register(Player,PlayerAdmin)
