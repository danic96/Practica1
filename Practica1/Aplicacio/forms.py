from django.forms import ModelForm
from models import Movie, Character

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ('user', 'date', 'id')
        
class CharacterForm(ModelForm):
    class Meta:
        model = Character
        exclude = ('user', 'date', 'id')
