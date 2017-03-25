from django.db import models

# Create your models here.

class Pelicula(models.Model):
    nom = models.TextField(max_length=50)
    web = models.TextField(max_length=100)

    def __unicode__(self):
        return self.nom