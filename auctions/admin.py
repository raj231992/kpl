from django.contrib import admin
from .models import Current_Player,Sold_Player,Refresh_Data
# Register your models here.
class Sold_PlayerAdmin(admin.ModelAdmin):
    list_display = ['player','price']
    class Meta:
        model = Sold_Player

admin.site.register(Current_Player)
admin.site.register(Refresh_Data)
admin.site.register(Sold_Player,Sold_PlayerAdmin)
