
from django.conf import settings
from django.db import models

# Create your models here.

class Continent(models.Model):
    name = models.CharField(max_length=255)
    logo = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Country(models.Model):
    name = models.CharField(max_length=255)
    continent = models.ForeignKey(Continent, models.SET_NULL, blank=True, null=True)
    logo = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Association(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    logo = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Competition(models.Model):
    name = models.CharField(max_length=255)
    association = models.ForeignKey(Association, models.SET_NULL, blank=True, null=True)
    logo = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class FootballTeam(models.Model):
    team_name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    continent = models.ForeignKey(Continent, models.SET_NULL, blank=True, null=True)
    domestic_league = models.ForeignKey(Competition, models.SET_NULL, blank=True, null=True)
    logo = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class BetCode(models.Model):
    BetStatus = models.TextChoices("BetStatus", "IN_PROGRESS SUCCESS LOST")
    
    home_team = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)
    bet = models.CharField(max_length=255)
    odd = models.DecimalField(max_digits=6, decimal_places=2)
    ht_home_score = models.IntegerField(null=True, blank=True)
    ht_away_score = models.IntegerField(null=True, blank=True)
    ft_home_score = models.IntegerField(null=True, blank=True)
    ft_away_score = models.IntegerField(null=True, blank=True)
    remark = models.BooleanField(null=True, blank=True, default=False)
    bet_status = models.CharField(choices=BetStatus, max_length=13, default="IN_PROGRESS")
    match_time = models.DateTimeField()
    competition = models.CharField(max_length=255, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class BookCodeInfo(models.Model):
    book_code = models.CharField(max_length=255)
    total_odd = models.DecimalField(max_digits=6, decimal_places=2)
    ticket_date = models.DateTimeField()
    placed_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    # image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    description = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.post}'


# class Likes(models.Model):
#     post = models.ForeignKey(
#         Post, on_delete=models.CASCADE, related_name='likes')
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     likes = models.BooleanField(default=False)
#     placed_at = models.DateTimeField(auto_now_add=True)
