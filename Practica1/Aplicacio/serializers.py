from django.contrib.auth.decorators import login_required
from rest_framework import serializers

from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer

from Aplicacio.models import Movie, Character, Team, Power, Location


class MovieSerializer(serializers.HyperlinkedModelSerializer):
	uri = HyperlinkedIdentityField(view_name='Aplicacio:movie_detail_API')
	
	
	user = CharField(read_only=True)
	
	class Meta:
		model = Movie
		fields = ('uri', 'user', 'id' ,'name', 'duration', 'revenue', 'detail_url')
		
		
class CharacterSerializer(serializers.HyperlinkedModelSerializer):
	uri = HyperlinkedIdentityField(view_name='Aplicacio:character_detail_API')
	
	
	user = CharField(read_only=True)
	
	class Meta:
		model = Character
		fields = ('uri', 'user', 'id' ,'name', 'gender', 'description', 'teams', 'powers')
		
		
class TeamSerializer(serializers.HyperlinkedModelSerializer):
	uri = HyperlinkedIdentityField(view_name='Aplicacio:team_detail_API')
	
	
	user = CharField(read_only=True)
	
	class Meta:
		model = Team
		fields = ('uri', 'user', 'id' ,'name', 'num_members', 'description')
		
		
class PowerSerializer(serializers.HyperlinkedModelSerializer):
	uri = HyperlinkedIdentityField(view_name='Aplicacio:power_detail_API')
	
	
	user = CharField(read_only=True)
	
	class Meta:
		model = Power
		fields = ('uri', 'user', 'id' ,'name', 'description')
		
		
class LocationSerializer(serializers.HyperlinkedModelSerializer):
	uri = HyperlinkedIdentityField(view_name='Aplicacio:location_detail_API')
	
	
	user = CharField(read_only=True)
	
	class Meta:
		model = Location
		fields = ('uri', 'user', 'id' ,'name', 'deck')
