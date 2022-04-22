from rest_framework import serializers
from .models import Actor, Movie, Review


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    
    class MovieListSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('title', )

    movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('id', 'movies', 'name', )
        read_only_fields = ('movies', )


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview', )


class MovieSerializer(serializers.ModelSerializer):

    class ActorListSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Actor
            fields = ('name', )

    class ReviewListSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = ('title', 'content', )

    actors = ActorListSerializer(many=True)
    review_set = ReviewListSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'actors', 'review_set', 'title', 'overview', 'release_date', 'poster_path',)


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content', )


class ReviewSerializer(serializers.ModelSerializer):
 
    class MovieListSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('title', )

    movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'movies', 'title', 'content', )
        read_only_fields = ('movies', )
