from django.db import models

# Create your models here.
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

    class Meta:
        verbose_name_plural = "Feedback"
    def __str__(self):
        return self.team +" " + self.year
