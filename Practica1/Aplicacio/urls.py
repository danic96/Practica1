from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from rest_framework.urlpatterns import format_suffix_patterns

from django.utils import timezone

from django.views.generic import DetailView, ListView, UpdateView
from models import Movie

urlpatterns = [
    # List latest 5 restaurants: /Aplicacio/
    url(r'^$',
        ListView.as_view(
            # queryset=Movie.objects.filter(date__lte=timezone.now()).order_by('-date')[:5],
            queryset=Movie.objects.order_by('-id')[:5],
            context_object_name='latest_movie_list',
            template_name='Aplicacio/movie_list_victor.html'),
        name='movie_list_victor'),
]
