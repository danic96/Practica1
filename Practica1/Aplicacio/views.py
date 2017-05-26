from django.shortcuts import render
from django.http import HttpResponse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView

from rest_framework import generics

from models import Movie, Character
from forms import MovieForm, CharacterForm

from Practica1.serializers import MovieSerializer


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

# HTML Views

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    template_name = 'Aplicacio/form.html'
    form_class = MovieForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MovieCreate, self).form_valid(form)

class MovieDetail(DetailView):
    model = Movie
    template_name = 'Aplicacio/movie_detail.html'

    """
    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context
    """

class CharacterCreate(LoginRequiredMixin, CreateView):
    model = Character
    template_name = 'Aplicacio/form.html'
    form_class = CharacterForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CharacterCreate, self).form_valid(form)

### RESTful API views ###

class APIMovieList(generics.ListCreateAPIView):
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class APIMovieDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
