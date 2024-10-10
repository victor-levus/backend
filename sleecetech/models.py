from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = PhoneNumberField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
