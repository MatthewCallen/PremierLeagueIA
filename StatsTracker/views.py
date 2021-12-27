from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .forms import StatsForm
from .models import Stats
import csv

# Create your views here.


def stat_view(request):
    #Get all teams in database 
    # all_teams = Teams.objects.get()
    all_teams = Stats.objects.all()
    context = {"teams": all_teams}

    # Stat_Choices =[
    #     ('Wins'),
    #     ('Draws'),
    #     ('Losses'),
    #     ('Points'),
    #     ('Goals Scored'),
    #     ('Goals Allowed'),
    #     ('Goals per 90'),
    #     ('Assists per 90'),
    #     ('Clean Sheets'),
    #     ('Table Finish')
    # ]

    # class UserForm(forms.Form):
    #     stat_choice = forms.CharField(label='Choose Stat to Filter', widget=forms.Select(choices=Stat_Choices))

    return render(request, "stats.html", context = context)

    #context = {"teams": all_teams}
    #return HttpResponse("Hello World. At Stats Tracker Index.")
    
def add_team_view(request):
    with open("stats.csv", "r") as f:
        reader = csv.reader(f, delimiter = '\t')
        for item in reader:
            new_team = Stats()
            entries = csv.reader(item, delimiter = ",")
            for entry in entries:
                new_team.team = entry[0]
                new_team.year = entry[1]
                new_team.wins = entry[2]
                new_team.draws = entry[3]
                new_team.losses = entry[4]
                new_team.points = entry[5]
                new_team.goals_scored = entry[6]
                new_team.goals_allowed = entry[7]
                new_team.goals_per90 = entry[8]
                new_team.assists_per90 = entry[9]
                new_team.clean_sheets = entry[10]
                new_team.table_finish = entry[11]
                print(entry)
            new_team.save()

    return render(request, "add-teams.html")

def home_view(request):
    return render(request, "homeview.html")

    from django import forms
def filter_view(request):
    return render(request, 'filterview.html')

# FRUIT_CHOICES= [
#     ('orange', 'Oranges'),
#     ('cantaloupe', 'Cantaloupes'),
#     ('mango', 'Mangoes'),
#     ('honeydew', 'Honeydews'),
#     ]

# class UserForm(forms.Form):
#     first_name= forms.CharField(max_length=100)
#     last_name= forms.CharField(max_length=100)
#     email= forms.EmailField()
#     age= forms.IntegerField()
#     favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))
