from django.contrib import admin

# Register your models here.

from Aplicacio.models import Movie, Character, Location, Team, Power
admin.site.register(Movie)
admin.site.register(Character)
admin.site.register(Location)
admin.site.register(Team)
admin.site.register(Power)
