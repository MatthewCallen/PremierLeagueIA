from django import forms
from .models import Stats

class StatsForm(forms.ModelForm):
    class Meta: 
        model = Stats
        fields = ['team', 'year', 'wins', 'losses', 'points', 'goals_scored', 'goals_allowed', 
        'goals_per90', 'assists_per90', 'clean_sheets', 
        'table_finish']



    Stat_Choices = [
        ('Wins'),
        ('Draws'),
        ('Losses'),
        ('Points'),
        ('Goals Scored'),
        ('Goals Allowed'),
        ('Goals per 90'),
        ('Assists per 90'),
        ('Clean Sheets'),
        ('Table Finish')
    ]
    # class UserForm(forms.Form):
    #     stat_choice = forms.CharField(label='Choose Stat to Filter', widget=forms.Select(choices=Stat_Choices))
