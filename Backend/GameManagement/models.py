from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(User)
    state = models.TextField()  # Store game state as JSON or other format

    def __str__(self):
        return self.name