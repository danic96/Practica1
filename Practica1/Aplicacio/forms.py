from django.forms import ModelForm
from models import Movie, Character, Team, Power, Location


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ('user', 'date', 'id')
        
        
class CharacterForm(ModelForm):
    class Meta:
        model = Character
        exclude = ('user', 'date', 'id')
        

class TeamForm(ModelForm):
    class Meta:
        model = Team
        exclude = ('user', 'date', 'id')
        
        
class PowerForm(ModelForm):
    class Meta:
        model = Power
        exclude = ('user', 'date', 'id')
        
        
class LocationForm(ModelForm):
    class Meta:
        model = Location
        exclude = ('user', 'date', 'id')
