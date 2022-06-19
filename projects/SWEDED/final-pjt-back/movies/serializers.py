from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, GetRate, Genre

User = get_user_model()


class GetRateSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('movie_id', 'title', )

    movie = MovieSerializer(read_only=True)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = GetRate
        fields = ('movie', 'user', 'score', 'short_comment', )


class MovieSerializer(serializers.ModelSerializer):
    
    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ( 'name', 'genre_id')
    
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'overview',
        'release_date', 'vote_average', 'vote_count',
        'poster_path', 'genres', )

