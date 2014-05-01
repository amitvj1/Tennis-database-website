from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.

class SignUp(models.Model):
    sqlQuery = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
class Player(models.Model):
    search_player = models.CharField(max_length=120)
class H2H(models.Model):
    player_1 = models.CharField(max_length=120)
    player_2 = models.CharField(max_length=120)
class recentResult(models.Model):
    Tournament_Name = models.CharField(max_length=120)
    year = models.CharField(max_length=120, verbose_name="Year")
class searchResult(models.Model):
    Player_Name = models.CharField(max_length=120)
    Tournament_Name = models.CharField(max_length=120)
    year = models.CharField(max_length=120, verbose_name="Year")
class individualRank(models.Model):
    player_name = models.CharField(max_length=120)
class playerByRank(models.Model):
    player_rank = models.IntegerField();
class completeRanking(models.Model):
    player_rank = models.IntegerField();
    #def __unicode__(self):
      #  return smart_unicode(self.email)