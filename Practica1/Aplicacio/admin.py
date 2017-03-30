from django.contrib import admin

# Register your models here.
from Aplicacio.models import Pelicula, Personatge, Localitzacio, Equip, Productora, Relacions
admin.site.register(Pelicula)
admin.site.register(Personatge)
admin.site.register(Localitzacio)
admin.site.register(Equip)
admin.site.register(Productora)
admin.site.register(Relacions)