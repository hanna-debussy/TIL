from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_safe
from .models import Movie, Genre

from django.core.paginator import Paginator

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context ={
        'movies': page_obj,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = movie.genres.all().values_list('name', flat=True)
    context = {
        'movie': movie,
        'genres':genres,
    }
    return render(request, 'movies/detail.html', context)

from django.db.models import Q

@require_safe
def recommended(request, movie_pk):
    # 만약 장르가 한개면 -> 그 장르의 평점 순으로 10개 출력
    # 2개 이상이면 -> 앞의 두개 장르의 평점 순으로 5개씩 출력
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie_genres = movie.genres.all().values_list('id', flat=True)
    genre_count = len(movie_genres)
    recommended_list = []

    if genre_count == 1:
        genre = get_object_or_404(Genre, pk=movie_genres[0])
        recommended_list.extend(list(genre.movie.filter(~Q(id=movie.pk)).order_by('-vote_average').values('title', 'vote_average','overview', 'id')[:10]))
    
    elif genre_count >= 2:
        for i in range(2):
            genre = get_object_or_404(Genre, pk=movie_genres[i])
            recommended_list.extend(list(genre.movie.filter(~Q(id=movie.pk)).order_by('-vote_average').values('title', 'vote_average','overview', 'id')[:5]))
    context = {
        'recommended_list' : recommended_list 
    }
    return render(request, 'movies/recommended.html', context)