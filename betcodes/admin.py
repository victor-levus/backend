from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.FootballClub)
class FootballClubAdmin(admin.ModelAdmin):
    list_display = ['club_name', 'country', 'continent', 'domestic_league', 'logo']


@admin.register(models.BetCode)
class BetCodeAdmin(admin.ModelAdmin):
    list_display = ['home_team', 'away_team', 'bet', 'ht_home_score', 'ht_away_score', 'ft_home_score', 'ft_away_score', 'match_time']

@admin.register(models.BookCodeInfo)
class BookCodeInfoAdmin(admin.ModelAdmin):
    list_display = ['book_code', 'total_odd', 'ticket_date']

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'created_at', 'user']
    list_select_related = ['user']

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'created_at', 'user', 'post', 'parent']
    list_select_related = ['user', 'post']
