from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Article
from movies.models import GetRate
from movies.serializers import MovieSerializer


class ProfileSerializer(serializers.ModelSerializer):


    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title', 'content', 'pk', )

    articles = ArticleSerializer(many=True)

    class MovieRateSerializer(serializers.ModelSerializer):
        def to_representation(self, instance):
            res = super().to_representation(instance)
            res.update({'movie': MovieSerializer(instance.movie).data})
            return res

        class Meta:
            model = GetRate
            fields = ('movie', 'score', 'short_comment')

    rated_movies = MovieRateSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'articles', 'rated_movies')

