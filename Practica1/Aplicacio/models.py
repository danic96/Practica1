from django.db import models

# Create your models here.


class Movie(models.Model):
    id = models.PositiveIntegerField(null=False, blank=False, primary_key=True)
    name = models.TextField(max_length=50)
    deck = models.TextField(max_length=100)
    duration = models.TextField(null=True, blank=True)
    revenue = models.TextField(null=True, blank=True)
    detail_url = models.TextField(max_length=100)


    def __unicode__(self):
        return self.nom


class Character(models.Model):
    id = models.PositiveIntegerField(null=False, blank=False, primary_key=True)
    name = models.TextField(max_length=50)
    gender = models.TextField(max_length=50)
    description = models.TextField(max_length=100)
    # id_pelicula = models.PositiveIntegerField(null=False, blank=False)

    def __unicode__(self):
        return self.nom


class Location(models.Model):
    id = models.PositiveIntegerField(null=False, blank=False, primary_key=True)
    name = models.TextField(max_length=50)

    def __unicode__(self):
        return self.nom


class Team(models.Model):
    id = models.PositiveIntegerField(null=False, blank=False, primary_key=True)
    name = models.TextField(max_length=50)
    num_members = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(max_length=100)

    def __unicode__(self):
        return self.nom


class Power(models.Model):
    id = models.PositiveIntegerField(null=False, blank=False, primary_key=True)
    name = models.TextField(max_length=50)

    def __unicode__(self):
        return self.nom


class RelationMovieCharacter(models.Model):
    id_movie = models.PositiveIntegerField(null=False, blank=False)
    id_character = models.PositiveIntegerField(null=False, blank=False)


class RelationCharacterTeam(models.Model):
    id_character = models.PositiveIntegerField(null=False, blank=False)
    id_team = models.PositiveIntegerField(null=False, blank=False)


class RelationMovieLocation(models.Model):
    id_movie = models.PositiveIntegerField(null=False, blank=False)
    id_location = models.PositiveIntegerField(null=False, blank=False)


class RelationCharacterPower(models.Model):
    id_character = models.PositiveIntegerField(null=False, blank=False)
    id_power = models.PositiveIntegerField(null=False, blank=False)
