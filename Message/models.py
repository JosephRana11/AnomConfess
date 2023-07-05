from django.db import models

# Create your models here.
class Message(models.Model):
    Sender = models.CharField(max_length=20 , blank=True)
    Text = models.TextField(max_length=200)