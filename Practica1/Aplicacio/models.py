from django.db import models

# Create your models here.

class Pelicula(models.Model):
    id = models.PositiveIntegerField(null=False, blank=False, primary_key=True)
    nom = models.TextField(max_length=50)
    productors = models.TextField(max_length=100)
    data = models.TextField(max_length=50)
    durada = models.TextField(null=True, blank=True)
    detail_url = models.TextField(max_length=100)

    def __unicode__(self):
        return self.nom

class Personatge(models.Model):
    id = models.PositiveIntegerField(null=False, blank=False, primary_key=True)
    nom = models.TextField(max_length=50)
    genere = models.TextField(max_length=50)
    descripcio = models.TextField(max_length=100)
    id_pelicula = models.PositiveIntegerField(null=False, blank=False)

    def __unicode__(self):
        return self.nom

class Localitzacio(models.Model):
    id = models.PositiveIntegerField(null=False, blank=False, primary_key=True)
    nom = models.TextField(max_length=50)

    def __unicode__(self):
        return self.nom

class Equip(models.Model):
    id = models.PositiveIntegerField(null=False, blank=False, primary_key=True)
    nom = models.TextField(max_length=50)
    num_membres = models.PositiveIntegerField(null=True, blank=True)
    descripcio = models.TextField(max_length=100)

    def __unicode__(self):
        return self.nom

class Productora(models.Model):
    id = models.PositiveIntegerField(null=False, blank=False, primary_key=True)
    nom = models.TextField(max_length=50)

    def __unicode__(self):
        return self.nom

class Relacions(models.Model):
    id_pelicula = models.PositiveIntegerField(null=False, blank=False)
    id_personatge = models.PositiveIntegerField(null=False, blank=False)
