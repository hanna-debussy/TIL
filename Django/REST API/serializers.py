from rest_framework import serializers
from .models import Artist, Music


# 모든 가수의 정보 반환: id, name
class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ("id", "name", )


# 상세 가수의 정보 생성/반환: id, name, music_set, music_count
class ArtistSerializer(serializers.ModelSerializer):
    music_count = serializers.IntegerField(source="music_set.count", read_only=True)

    class Meta:
        model = Artist
        fields = ("id", "name", "music_set", "music_count", )


# 모든 음악 정보 반환: id, title
class MusicListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Music
        fields = ("id", "title", )


# 상세 음악의 정보 생성/반환: id, title, artist
class MusicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Music
        fields = ("id", "title", "artist", )
        read_only_fields = ("artist", )