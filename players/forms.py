from django.forms import ModelForm
from .models import Player


class PlayerForm(ModelForm):
    class Meta:
        exclude = ['pool']
        model = Player
        labels = {
            'name': 'Full Name',
            'phone_no': 'Phone Number',
            'pic': 'Profile Picture (Provide a picture where face is clearly visible)',
            'prev_exp': 'Previous Cricket Experience',
            'kpl_exp': 'Previous KPL Experience',
            'manager':'Want to be a Team Manager?'
        }
