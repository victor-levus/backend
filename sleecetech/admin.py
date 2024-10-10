from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Message)
class SleeceMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject', 'message', 'created_at']