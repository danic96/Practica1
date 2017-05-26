from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from rest_framework.urlpatterns import format_suffix_patterns

from django.utils import timezone

from django.views.generic import DetailView, ListView, UpdateView
from models import Movie, Character

from views import MovieCreate, CharacterCreate, MovieDetail, LoginRequiredCheckIsOwnerUpdateView, \
	APIMovieList, APIMovieDetail


from forms import MovieForm

from rest_framework.urlpatterns import format_suffix_patterns

# movies1 = Movie.objects.order_by('-id')[:5] + Character.objects.order_by('-id')[:5]
data = {'movies': Movie.objects.order_by('-id')[:5],
		'characters': Character.objects.order_by('-id')[:5]}

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

     # Create a movie, /Aplicacio/movies/create/
     url(r'^movies/create/$',
        MovieCreate.as_view(),
        name='movie_create'),

     # Movie details, ex.: /Aplicacio/movies/1/
    url(r'^movies/(?P<pk>\d+)/$',
        MovieDetail.as_view(),
        name='movie_detail'),

     # Edit movie details, ex.: /Aplicacio/movies/1/edit/
    url(r'^movies/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Movie,
            form_class=MovieForm),
        name='movie_edit'),

     # Create a movie character, ex.: /Aplicacio/charcters/create/
    url(r'^characters/create/$',
        CharacterCreate.as_view(),
        name='character_create'),

# API

	url(r'^api/movie/$',
        APIMovieList.as_view(),
		name='movie-list'),

    url(r'^api/movie/(?P<pk>\d+)/$',
        APIMovieDetail.as_view(),
		name='movie-detail'),

]

# Format suffixes

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'xml'])
