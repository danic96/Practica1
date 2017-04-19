from django.db import models

# Create your models here.


class Location(models.Model):
    id = models.PositiveIntegerField(null=False, blank=False, primary_key=True)
    name = models.TextField(max_length=50)

    def __unicode__(self):
        return self.name


class Team(models.Model):
    id = models.PositiveIntegerField(null=False, blank=False, primary_key=True)
    name = models.TextField(max_length=50)
    num_members = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(max_length=100)

    def __unicode__(self):
        return self.name


class Power(models.Model):
    id = models.PositiveIntegerField(null=False, blank=False, primary_key=True)
    name = models.TextField(max_length=50)

    def __unicode__(self):
        return self.name


class Character(models.Model):
    id = models.PositiveIntegerField(null=False, blank=False, primary_key=True)
    name = models.TextField(max_length=50)
    gender = models.TextField(max_length=50)
    description = models.TextField(max_length=100)
    # id_pelicula = models.PositiveIntegerField(null=False, blank=False)
    teams = models.ManyToManyField(Team)
    powers = models.ManyToManyField(Power)

    def __unicode__(self):
        return self.name


class Movie(models.Model):
    id = models.PositiveIntegerField(null=False, blank=False, primary_key=True)
    name = models.TextField(max_length=50)
    deck = models.TextField(max_length=100)
    duration = models.TextField(null=True, blank=True)
    revenue = models.TextField(null=True, blank=True)
    detail_url = models.TextField(max_length=100)
    characters = models.ManyToManyField(Character)
    locations = models.ManyToManyField(Location)

    def __unicode__(self):
        return self.name
