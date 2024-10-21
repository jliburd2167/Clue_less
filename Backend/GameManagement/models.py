from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(User)
    state = models.TextField()  # Store game state as JSON or other format

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=100)
    in_room = models.ForeignKey('RoomHallway', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class RoomHallway(models.Model):
    name = models.CharField(max_length=100)
    is_room = models.BooleanField(default=True)
    can_guess = models.BooleanField(default=True)
    has_secret_passageway = models.BooleanField(default=False)
    connections = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return self.name


class Player(models.Model):
    player_name = models.CharField(max_length=100)
    current_location = models.ForeignKey(RoomHallway, on_delete=models.SET_NULL, null=True)
    holding_cards = models.ManyToManyField('Card', blank=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    card_type = models.CharField(max_length=100)  # "person", "weapon", "room"
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GameSession(models.Model):
    players = models.ManyToManyField(Player)
    active = models.BooleanField(default=True)
    turn_counter = models.IntegerField(default=0)
    round_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# Additional models can be added as needed