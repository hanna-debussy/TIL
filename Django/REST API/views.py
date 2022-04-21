from urllib import response
from webbrowser import get
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Artist, Music
from .serializers import (
    ArtistListSerializer,
    ArtistSerializer,
    MusicListSerializer,
    MusicSerializer,
)
from music import serializers


@api_view(["GET", "POST"])
def artist_index_create(request):

    def artist_index():
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)

    def artist_create():
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    if request.method == "POST":
        return artist_create()
    else:
        return artist_index()


@api_view(["GET"])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistSerializer(instance=artist)
    return Response(serializer.data)


@api_view(["POST"])
def artist_music_create(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = MusicSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicListSerializer(musics, many=True)
    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def music_detail_update_delete(request, music_pk):
    music = Music.objects.get(pk=music_pk)

    def music_detail():
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    def music_update():
        serializer = MusicSerializer(instance=music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            
    def music_delete():
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    if request.method == "GET":
        return music_detail()

    elif request.method == "PUT":
        return music_update()

    elif request.method == "DELETE":
        return music_delete()