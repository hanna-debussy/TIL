from django.urls import path
from . import views

app_name = "music"

urlpatterns = [
    path("artist/", views.artist_index_create),
    path("artist/<artist_pk>/", views.artist_detail),
    path("artist/<artist_pk>/music/", views.artist_music_create),
    path("music/", views.music_list),
    path("music/<music_pk>/", views.music_detail_update_delete),
]
