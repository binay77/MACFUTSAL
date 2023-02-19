from django.db import models

# Create your models here.
class Game_Updates(models.Model):
    Team_1= models.CharField(max_length=20,null=False)
    Team_2= models.CharField(max_length=20,null = False)
    title= models.CharField(max_length=100,null = False)
    Final_Score = models.CharField(max_length=20,null = False)
    Goal_Scorers_TEAM_1 = models.CharField(max_length=500,null = False)
    Goal_Scorers_TEAM_2 = models.CharField(max_length=500,null = False)



    def __str__(self):
        return self.title