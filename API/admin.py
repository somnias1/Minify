from django.contrib import admin

from .models import (
    Album,
    Artist,
    Country,
    Genre,
    Membership,
    Playlist,
    Queue,
    Song,
    User,
    UserFollowing,
)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ("pk", "artist", "album_name", "release_date")
    list_display_links = ("pk", "artist", "album_name", "release_date")
    list_filter = ["artist", "album_name"]
    search_fields = ["album_name"]


admin.site.register(Album, AlbumAdmin)


class ArtistAdmin(admin.ModelAdmin):
    list_display = ("pk", "artist_name", "origin")
    list_display_links = ("pk", "artist_name", "origin")
    list_filter = ["artist_name", "origin"]
    search_fields = ["artist_name"]


admin.site.register(Artist, ArtistAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = ["pk", "country_name"]
    list_display_links = ["pk", "country_name"]
    list_filter = ["country_name"]
    search_fields = ["country_name"]


admin.site.register(Country, CountryAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ["pk", "genre_name"]
    list_display_links = ["pk", "genre_name"]
    list_filter = ["genre_name"]
    search_fields = ["genre_name"]


admin.site.register(Genre, GenreAdmin)


class MembershipAdmin(admin.ModelAdmin):
    list_display = ["pk", "membership_name", "duration"]
    list_display_links = ["pk", "membership_name"]
    list_filter = ["membership_name", "duration"]
    search_fields = ["membership_name"]


admin.site.register(Membership, MembershipAdmin)


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ["pk", "playlist_name"]
    list_display_links = ["pk", "playlist_name"]
    list_filter = ["playlist_name"]
    search_fields = ["playlist_name"]


admin.site.register(Playlist, PlaylistAdmin)


class QueueAdmin(admin.ModelAdmin):
    list_display = ["pk", "user"]


admin.site.register(Queue, QueueAdmin)


class SongAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "album",
        "song_name",
        "track_number",
        "is_explicit",
    ]
    list_display_links = [
        "pk",
        "album",
        "song_name",
        "track_number",
        "is_explicit",
    ]
    list_filter = ["song_name", "album"]
    search_fields = ["song_name"]


admin.site.register(Song, SongAdmin)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ("pk", "username", "membership", "country")
    list_display_links = (
        "pk",
        "username",
        "membership",
    )

    search_fields = [
        "membership",
        "username",
    ]

    list_filter = [
        "country",
        "signup_date",
    ]
