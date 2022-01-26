from django.shortcuts import render
from django.http import HttpResponse, response
from django import forms
from .forms import StatsForm
from .models import Stats
import csv

# Creates all views within my project


def stat_view(request): #View for stat page works
    #Get all teams in database 
    # all_teams = Teams.objects.get()
    #all_teams = Stats.objects.all()

    query = request.GET.get('dropdown') #Uses dropdown menu to filter by each stat within stat page
    if query is None:
        all_teams = Stats.objects.all() #If dropdown menu is not used to filter, display normal stat page
    elif query == 'table_finish':
        all_teams=Stats.objects.all().order_by(query) #If dropdown menu is used to filter, order based on table finish for all teams from least to greatest(only stat where lower number is better)
    else:
        all_teams = Stats.objects.all().order_by('-' + query) #If dropdown menu is used to filter, order based on user chosen stat for all teams from greatest to least



    context = { #returns these attributes
        "teams": all_teams, 
        "query": query,
    }

    return render(request, "stats.html", context = context)

    #context = {"teams": all_teams}
    #return HttpResponse("Hello World. At Stats Tracker Index.")
    
def add_team_view(request): #View to add teams to database
    with open("stats.csv", "r") as f: #Takes in csv file where all data is located
        reader = csv.reader(f, delimiter = '\t') 
        for item in reader:
            new_team = Stats() #Creates a new team object
            entries = csv.reader(item, delimiter = ",")  #Searches through csv to find where each stat is(knows it's at a new stat when it encounters a ,)
            for entry in entries: 
                new_team.team = entry[0] #Each stat is added into the new team object
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
                new_team.save()

    return render(request, "add-teams.html") #returns what is written in the html file

def home_view(request):
    return render(request, "homeview.html") #returns what is written in the html file

    from django import forms

def comparison_view(request):
    all_teams = Stats.objects.all()
    compare_error = ""
    if request.method == "POST":
        if request.POST.get("team_one_selection") and request.POST.get("team_two_selection"): #Checking buttons to compare teams
            if request.POST.get("team_one_selection") == "-1" or request.POST.get("team_two_selection") == "-1":  #Error to check whether the user has selected both teams
                compare_error = "Please select two teams"                                                         #-1 represents ID of the team objects(-1 means no object was found/default)
            elif request.POST.get("team_one_selection") == request.POST.get("team_two_selection"):  #Error to check whether the two selected teams are different
                compare_error = "Please select two different teams"
            else:
                team_one = Stats.objects.get(id=request.POST.get("team_one_selection"))#Gets ID from dropdown menu of team 1
                team_two = Stats.objects.get(id=request.POST.get("team_two_selection"))#Gets ID from dropdown menu of team 2
                context = {
                    "team_one": team_one,
                    "team_two": team_two,
                }          #adds to context so these variables can be used in html file
                return render(request, "comparison-display.html", context)

            #lookup, Stats.objects.get(name, year)
                
        # elif response.POST.get("team_two_selection"):

    context = {
        "teams": all_teams, 
        "compare_error": compare_error,
        #pass in teams
    }
    return render(request, "comparison.html", context)

def description_view(request):
    return render(request, "description.html") #returns what is written in the html file
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


        # <!--
        #     <td class={% if dropdown ="col" ? highlighted : regular%}
        # -->