from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView

from models import Movie, Character, Team, Power, Location, MovieReview
from forms import MovieForm, CharacterForm, TeamForm, PowerForm, LocationForm

from django.core.urlresolvers import reverse

from rest_framework import generics

from Aplicacio.serializers import MovieSerializer, CharacterSerializer, TeamSerializer, PowerSerializer, LocationSerializer




# Security Mixins
class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'Aplicacio/form.html'


class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    template_name = 'Aplicacio/form.html'
    form_class = MovieForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MovieCreate, self).form_valid(form)


class CharacterCreate(LoginRequiredMixin, CreateView):
    model = Character
    template_name = 'Aplicacio/form.html'
    form_class = CharacterForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CharacterCreate, self).form_valid(form)


class TeamCreate(LoginRequiredMixin, CreateView):
    model = Team
    template_name = 'Aplicacio/form.html'
    form_class = TeamForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TeamCreate, self).form_valid(form)


class PowerCreate(LoginRequiredMixin, CreateView):
    model = Power
    template_name = 'Aplicacio/form.html'
    form_class = PowerForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PowerCreate, self).form_valid(form)


class LocationCreate(LoginRequiredMixin, CreateView):
    model = Location
    template_name = 'Aplicacio/form.html'
    form_class = LocationForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LocationCreate, self).form_valid(form)


class MovieDetail(DetailView):
    model = Movie
    template_name = 'Aplicacio/movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = MovieReview.RATING_CHOICES
        return context


class CharacterDetail(DetailView):
    model = Character
    template_name = 'Aplicacio/character_detail.html'


class TeamDetail(DetailView):
    model = Team
    template_name = 'Aplicacio/team_detail.html'


class PowerDetail(DetailView):
    model = Power
    template_name = 'Aplicacio/power_detail.html'


class LocationDetail(DetailView):
    model = Location
    template_name = 'Aplicacio/location_detail.html'


def deleteMovie(requests, pk):
	movie = get_object_or_404(Movie, pk=pk)
	movie.delete()

	return HttpResponseRedirect(reverse('Aplicacio:movie_list'))

def deleteCharacter(requests, pk):
	character = get_object_or_404(Character, pk=pk)
	character.delete()

	return HttpResponseRedirect(reverse('Aplicacio:character_list'))

def deleteTeam(requests, pk):
	team = get_object_or_404(Team, pk=pk)
	team.delete()

	return HttpResponseRedirect(reverse('Aplicacio:team_list'))

def deletePower(requests, pk):
	power = get_object_or_404(Power, pk=pk)
	power.delete()

	return HttpResponseRedirect(reverse('Aplicacio:power_list'))


def deleteLocation(requests, pk):
	location = get_object_or_404(Location, pk=pk)
	location.delete()

	return HttpResponseRedirect(reverse('Aplicacio:location_list'))

@login_required()
def review(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if MovieReview.objects.filter(movie=movie, user=request.user).exists():
        MovieReview.objects.get(movie=movie, user=request.user).delete()
    new_review = MovieReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        movie=movie)
    new_review.save()
    return HttpResponseRedirect(reverse('Aplicacio:movie_detail', args=(movie.id,)))


# API

class APIMovieList(generics.ListCreateAPIView):
	model = Movie
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer


class APIMovieDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Movie
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer


class APICharacterList(generics.ListCreateAPIView):
	model = Character
	queryset = Character.objects.all()
	serializer_class = CharacterSerializer


class APICharacterDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Character
	queryset = Character.objects.all()
	serializer_class = CharacterSerializer


class APITeamList(generics.ListCreateAPIView):
	model = Team
	queryset = Team.objects.all()
	serializer_class = TeamSerializer


class APITeamDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Team
	queryset = Team.objects.all()
	serializer_class = TeamSerializer


class APIPowerList(generics.ListCreateAPIView):
	model = Power
	queryset = Power.objects.all()
	serializer_class = PowerSerializer


class APIPowerDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Power
	queryset = Power.objects.all()
	serializer_class = PowerSerializer


class APILocationList(generics.ListCreateAPIView):
	model = Location
	queryset = Location.objects.all()
	serializer_class = LocationSerializer


class APILocationDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Location
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
