from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name="homeview"),
    #path('stats/<string:stat>', views.stat_view, name='stat_view'),
    path('stats/', views.stat_view, name='stat_view'),
    path('addteams/', views.add_team_view, name = 'add_team_view'),    
    path('filter/', views.filter_view, name = 'filter_view')
]