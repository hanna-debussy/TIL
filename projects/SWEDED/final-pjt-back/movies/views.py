from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Movie, GetRate, Genre
from .serializers import GetRateSerializer, MovieSerializer
from movies import serializers
import random

User = get_user_model()


# Create your views here.
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('-release_date')[:12]
        serializer1 = MovieSerializer(movies, many=True)
        top_movies = Movie.objects.order_by('-vote_average')[:12]
        serializer2 = MovieSerializer(top_movies, many=True)
        
        return Response([serializer1.data, serializer2.data])


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET'])
def is_movie_rated(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    is_rated = movie.scores.filter(user=request.user).exists()

    result = {
        "is_rated": is_rated,
    }
    rated_score = 0

    if is_rated:
        rated_score = movie.scores.filter(user=request.user).values('score')
        return Response([result, rated_score])
    else:
        return Response([result, rated_score])


@api_view(['POST'])
def create_movie(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            serializer = GetRateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def movie_update_or_delete(request, article_pk):
    movie = get_object_or_404(Movie, pk=article_pk)

    def update_movie():
        if request.user == movie.user:
            serializer = GetRateSerializer(instance=movie, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    def delete_movie():
        if request.user == movie.user:
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    if request.user.is_superuser:
        if request.method == 'PUT':
                return update_movie()
        elif request.method == 'DELETE':
                return delete_movie()


@api_view(['POST'])
def movie_score_rate(request, movie_pk):
    movie = get_object_or_404(Movie, movie_id=movie_pk)
    user = request.user

    serializer = GetRateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, movie=movie)
        return Response(serializer.data)


@api_view(['PUT'])
def score_update(request, movie_pk, username):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = get_object_or_404(User, username=username)
    score = get_object_or_404(GetRate, movie=movie, user=user)

    if request.user == score.user:
        serializer = GetRateSerializer(instance=score, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def get_recommendation(request, username):
    user = get_object_or_404(User, username=username)
    movies = user.rated_movies.values('movie')           # 내가 평가한 movies id들의 object 집합
    weights = [0, 0, 0]

    categories = [
        [12, 28, 53, 18, 80],                            # 가장 대중적
        [14, 16, 27, 35, 878, 10749, 10752],
        [36, 37, 99, 9648, 10402, 10751, 10770],         # 가장 비대중적 (180개 기준 20개 이하 영화)
    ]

    for movie in movies: 
        movie_id = movie['movie']
        movie = get_object_or_404(Movie, pk=movie_id)

        if movie.scores.filter(user=user).values('score')[0]['score'] >= 3:
            for genre in movie.genres.all():                # 해당 영화의 모든 장르 뽑아와서
                for idx, category in enumerate(categories): # 카테고리 가져오는 거
                    if genre.genre_id in category:          # 1번 카테고리에 들어가면
                        weights[idx] += ((idx+1)/5) + 1     # weights[1] += 1 + 보정
        else:
            for genre in movie.genres.all():                # 해당 영화의 모든 장르 뽑아와서
                for idx, category in enumerate(categories): # 카테고리 가져오는 거
                    if genre.genre_id in category:          # 1번 카테고리에 들어가면
                        weights[idx] -= ((idx+1)/5) + 0.5   # weights[1] -= 0.5 + 보정

    max_weight = weights.index(max(weights))

    # categories[max_weight](카테고리 속 id들) 해당 id에 해당하는 영화들 filter
    
    recommended_movies = []

    all_movies = Movie.objects.all()
    recommend_genres = random.sample(categories[max_weight], 2) 

    for movie in all_movies:

        for x in movie.genres.values('genre_id'):       # 그 영화가 가진 장르의 {id=값}들의 queryset list
            for recommend_genre in recommend_genres:
                if recommend_genre == x['genre_id']:    # 그 쿼리셋의 gnere_id key인 value == 우리가 가진 장르
                    recommended_movies.append(movie)
    

    ramdom_recommendations = random.sample(recommended_movies, 6)
    serializer = MovieSerializer(ramdom_recommendations, many=True) 

    return Response(serializer.data)
    

# TMDB가 제공하는 API 데이터들을 db로 가져오기
import requests
import json

TMDB_API_KEY = '<API_KEY>'


def get_movie_datas():
    total_data = []
    for i in range(1, 4):
        request_url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=ko-KR&page={i}&region=KR"
        # request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        # request_url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('poster_path', ''):
                if movie.get('genre_ids', ''):
                    fields = {
                        'movie_id': movie['id'],
                        'title': movie['title'],
                        'overview': movie['overview'],
                        'release_date': movie['release_date'],
                        'vote_average': movie['vote_average'],
                        'vote_count': movie['vote_count'],
                        'poster_path': movie['poster_path'],
                        'genres': movie['genre_ids'],
                    }

                    data = {
                        "pk": movie['id'],
                        "model": "movies.movie",
                        'fields': fields,
                    }

                    total_data.append(data)

    with open("now_playing_data.json", "w", encoding="utf-8") as w:
    # with open("popular_data.json", "w", encoding="utf-8") as w:
    # with open("top_rated_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, ensure_ascii=False)

# get_movie_datas()


def get_genre_datas():
    total_data = []

    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR"
    genres = requests.get(request_url).json()

    for genre in genres['genres']:
        fields = {
            'genre_id': genre['id'],
            'name': genre['name'],
        }

        data = {
            "pk": genre['id'],
            "model": "movies.genre",
            "fields": fields,
        }

        total_data.append(data)

    with open("genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, ensure_ascii=False)

# get_genre_datas()

