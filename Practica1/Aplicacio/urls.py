from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from rest_framework.urlpatterns import format_suffix_patterns

from django.utils import timezone

from django.views.generic import DetailView, ListView, UpdateView
from models import Movie

from views import MovieCreate, MovieDetail, LoginRequiredCheckIsOwnerUpdateView

from forms import MovieForm

urlpatterns = [
    # List latest 5 restaurants: /Aplicacio/
    url(r'^$',
        ListView.as_view(
            # queryset=Movie.objects.filter(date__lte=timezone.now()).order_by('-date')[:5],
            queryset=Movie.objects.order_by('-id')[:5],
            context_object_name='latest_movie_list',
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
]
