from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from rest_framework.urlpatterns import format_suffix_patterns

from django.utils import timezone

from django.views.generic import DetailView, ListView, UpdateView
from models import Movie, Character, Team, Power, Location

from views import MovieCreate, CharacterCreate, TeamCreate, MovieDetail, CharacterDetail, TeamDetail, LoginRequiredCheckIsOwnerUpdateView


from forms import MovieForm, CharacterForm, TeamForm

data = {'movies': Movie.objects.order_by('-id')[:5], 
		'characters': Character.objects.order_by('-id')[:5],
		'teams': Team.objects.order_by('-id')[:5],
		'powers': Power.objects.order_by('-id')[:5],
		'locations': Location.objects.order_by('-id')[:5]}

urlpatterns = [
    # List latest 5 of everything: /Aplicacio/
    url(r'^$',
        ListView.as_view(
            queryset=data,
            context_object_name='latest_all_list',
            template_name='Aplicacio/index_list.html'),
        	name='index_list'),
     
    # List all movies: /Aplicacio/movies/
    url(r'^movies/$',
        ListView.as_view(
            queryset=Movie.objects.all,
            context_object_name='movie_list',
            template_name='Aplicacio/movie_list.html'),
        	name='movie_list'),
        	
    # List all characters: /Aplicacio/characters/
    url(r'^characters/$',
        ListView.as_view(
            queryset=Character.objects.all,
            context_object_name='character_list',
            template_name='Aplicacio/character_list.html'),
        	name='character_list'),
        	
    # List all teams: /Aplicacio/teams/
    url(r'^teams/$',
        ListView.as_view(
            queryset=Team.objects.all,
            context_object_name='team_list',
            template_name='Aplicacio/team_list.html'),
        	name='team_list'),
     
    # Create a movie, /Aplicacio/movies/create/
    url(r'^movies/create/$',
        MovieCreate.as_view(),
        name='movie_create'),
        
    # Create a character, ex.: /Aplicacio/charcters/create/
    url(r'^characters/create/$',
        CharacterCreate.as_view(),
        name='character_create'),
        
    # Create a team, ex.: /Aplicacio/teams/create/
    url(r'^teams/create/$',
        TeamCreate.as_view(),
        name='team_create'),
        
    # Movie details, ex.: /Aplicacio/movies/1/
    url(r'^movies/(?P<pk>\d+)/$',
        MovieDetail.as_view(),
        name='movie_detail'),
        
    # Character details, ex.: /Aplicacio/characters/1/
    url(r'^characters/(?P<pk>\d+)/$',
        CharacterDetail.as_view(),
        name='character_detail'),
        
    # Team details, ex.: /Aplicacio/teams/1/
    url(r'^teams/(?P<pk>\d+)/$',
       	TeamDetail.as_view(),
        name='team_detail'),
        
    # Edit movie details, ex.: /Aplicacio/movies/1/edit/
    url(r'^movies/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Movie,
            form_class=MovieForm),
        name='movie_edit'),
        
    # Edit character details, ex.: /Aplicacio/characters/1/edit/
    url(r'^characters/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Character,
            form_class=CharacterForm),
        name='character_edit'),
        
    # Edit teams details, ex.: /Aplicacio/teams/1/edit/
    url(r'^teams/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Team,
            form_class=TeamForm),
        name='team_edit'),
]
