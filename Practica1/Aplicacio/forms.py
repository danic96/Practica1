from django.forms import ModelForm
from models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ('user', 'date', 'id', 'characters', 'locations')
