from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from datetime import date

# Create your models here.


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    deck = models.TextField(max_length=100)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def get_absolute_url(self):
        return reverse('Aplicacio:location_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    num_members = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(max_length=100)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def get_absolute_url(self):
        return reverse('Aplicacio:team_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name


class Power(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=100)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def get_absolute_url(self):
        return reverse('Aplicacio:power_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name


class Character(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    gender = models.TextField(max_length=50)
    description = models.TextField(max_length=100)
    teams = models.ManyToManyField(Team, blank=True)
    powers = models.ManyToManyField(Power, blank=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def get_absolute_url(self):
        return reverse('Aplicacio:character_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    deck = models.TextField(max_length=100, blank=True)
    duration = models.TextField(null=True, blank=True)
    revenue = models.TextField(null=True, blank=True)
    detail_url = models.TextField(max_length=100)
    characters = models.ManyToManyField(Character, blank=True)
    locations = models.ManyToManyField(Location, blank=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def get_absolute_url(self):
        return reverse('Aplicacio:movie_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name

    def averageRating(self):
        reviewCount = self.moviereview_set.count()
        if not reviewCount:
            return 0
        else:
            ratingSum = sum([float(review.rating) for review in self.moviereview_set.all()])
            return ratingSum / reviewCount


class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True


class MovieReview(Review):
    movie = models.ForeignKey(Movie)

    class Meta:
        unique_together = ("movie", "user")
