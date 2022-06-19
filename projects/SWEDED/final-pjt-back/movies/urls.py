from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/is_rated/', views.is_movie_rated),
    path('<int:movie_pk>/rate/', views.movie_score_rate),
    path('<int:movie_pk>/rate/<username>/', views.score_update),
    path('recommendations/<username>/', views.get_recommendation)
]
