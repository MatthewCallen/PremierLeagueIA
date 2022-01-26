from django.db import models
from colorfield.fields import ColorField

#Defines all parts of an object within a stats class: Every object(all teams) in stats class contains all of these attributes
class Stats(models.Model):
    team = models.TextField()
    year = models.TextField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()
    points = models.IntegerField()
    goals_scored = models.IntegerField()
    goals_allowed = models.IntegerField()
    goals_per90 = models.FloatField()
    assists_per90 = models.FloatField()
    clean_sheets = models.IntegerField()
    table_finish = models.IntegerField()
    color = ColorField(default='#FF0000')
    logo = models.FileField(blank=True, null=True)

    class Meta: #Defines name to display in admin page
        verbose_name_plural = "Team Stats"
    def __str__(self): #Defines how object teams are displayed in admin page(Ex: Arsenal 2015-2016)
        return self.team +" " + self.year
