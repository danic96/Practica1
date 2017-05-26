from django.contrib.auth.models import User, Group
from rest_framework import serializers

from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer

from Aplicacio.models import Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='Aplicacio:movie-detail')
    # cridar a les altres


    user = CharField(read_only=True)

    class Meta:
        model = Movie
        fields = ('uri', 'user', 'id', 'name', 'deck', 'duration', 'revenue', 'detail_url')

# les altres
