from django import forms
from .models import Stats

class StatsForm(forms.ModelForm):
    class Meta: 
        model = Stats
        fields = ['team', 'year', 'wins', 'losses', 'points', 'goals_scored', 'goals_allowed', 
        'goals_per90', 'assists_per90', 'clean_sheets', 
        'table_finish']

