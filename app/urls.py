from django.urls import path, include
from .views import index, getReleases, getRecord, \
    getArtist, getArtists, getReleasesByArtistId, fav

urlpatterns = [
    path('', index),
    path('getReleasesByArtistsId/', getReleasesByArtistId),
    path('getRecord/', getRecord),
    path('getArtist/', getArtist),
    path('getArtists/', getArtists),
    path('fav/', fav)
]
