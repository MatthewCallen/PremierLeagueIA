from django.urls import path

from . import views
#Creates defined urls for each page/view in my project
urlpatterns = [
    path('', views.home_view, name="homeview"),  #Url definition to go to homepage
    #path('stats/<string:stat>', views.stat_view, name='stat_view'),
    path('stats/', views.stat_view, name='stat_view'), #Url definition to go to stats page
    path('addteams/', views.add_team_view, name = 'add_team_view'),  #Url definition to go to add teams page(** only use this to add more objects, not accessible by user **)
    path('comparison/', views.comparison_view, name='comparison_view'), #Url definition to go to comparison page
    path('comparison-display/', views.comparison_view, name='comparison_view'),#Url definition to go to comparison page(this page links off of comparison url)
    path('description/', views.description_view, name='description_view')
]