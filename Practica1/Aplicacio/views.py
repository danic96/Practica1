from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView

from models import Movie, Character, Team, Power, Location
from forms import MovieForm, CharacterForm, TeamForm, PowerForm, LocationForm

from django.core.urlresolvers import reverse


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

    """
    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context
    """

    
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
    
    
def deleteLocation(requests, pk):
	location = get_object_or_404(Location, pk=pk)
	location.delete()
	return HttpResponseRedirect(reverse('Aplicacio:location_list'))

    

        
