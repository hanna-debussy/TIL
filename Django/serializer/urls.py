from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('actors/', views.actor_list, name='actor_list'),
    path('actors/<int:actor_pk>/', views.actor_detail, name='actor_detail'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('<int:movie_pk>/reviews/', views.create_review, name='create_review'),
]
