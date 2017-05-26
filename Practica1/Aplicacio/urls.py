from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from rest_framework.urlpatterns import format_suffix_patterns

from django.utils import timezone

from django.views.generic import DetailView, ListView, UpdateView
from models import Movie, Character, Team, Power, Location

from views import MovieCreate, CharacterCreate, TeamCreate, LocationCreate, PowerCreate, MovieDetail, CharacterDetail, TeamDetail, PowerDetail, LocationDetail, LoginRequiredCheckIsOwnerUpdateView

from forms import MovieForm, CharacterForm, TeamForm, PowerForm, LocationForm

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
        	
    # List all powers: /Aplicacio/powers/
    url(r'^powers/$',
        ListView.as_view(
            queryset=Power.objects.all,
            context_object_name='power_list',
            template_name='Aplicacio/power_list.html'),
        	name='power_list'),
        	
    # List all locations: /Aplicacio/locations/
    url(r'^locations/$',
        ListView.as_view(
            queryset=Location.objects.all,
            context_object_name='location_list',
            template_name='Aplicacio/location_list.html'),
        	name='location_list'),
     
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
        
    # Create a power, ex.: /Aplicacio/powers/create/
    url(r'^powers/create/$',
        PowerCreate.as_view(),
        name='power_create'),
        
    # Create a location, ex.: /Aplicacio/locations/create/
    url(r'^locations/create/$',
        LocationCreate.as_view(),
        name='location_create'),
        
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
        
    # Power details, ex.: /Aplicacio/powers/1/
    url(r'^powers/(?P<pk>\d+)/$',
       	PowerDetail.as_view(),
        name='power_detail'),
        
    # Locations details, ex.: /Aplicacio/locations/1/
    url(r'^locations/(?P<pk>\d+)/$',
       	LocationDetail.as_view(),
        name='location_detail'),
        
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
        
    # Edit powers details, ex.: /Aplicacio/powers/1/edit/
    url(r'^powers/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Power,
            form_class=PowerForm),
        name='power_edit'),
        
    # Edit locations details, ex.: /Aplicacio/locations/1/edit/
    url(r'^locations/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Location,
            form_class=LocationForm),
        name='location_edit'),
        
    """
    # Delete locations details, ex.: /Aplicacio/locations/1/delete/
    url(r'^locations/(?P<pk>\d+)/delete/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Location,
            form_class=LocationForm),
        name='location_delete'),
        
    """
    
    """
    # Delete locations details, ex.: /Aplicacio/locations/1/delete/
    url(r'^locations/(?P<pk>\d+)/delete/$', 
    		Delete.as_view(), 
    		name='delete_location'),
   	"""
]
