from rest_framework import serializers

from .models import Portfolio, Calification, Artist


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('name',)


class CalificationSerializer(serializers.ModelSerializer):

    artist = ArtistSerializer()

    class Meta:
        model = Calification
        fields = ('artist', 'rate', 'added_at')


class PortfolioSerializer(serializers.ModelSerializer):

    artists = CalificationSerializer(many=True, source='califications')

    class Meta:
        model = Portfolio
        fields = ('id', 'name', 'user', 'artists',)
