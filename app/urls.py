from django.urls import path, include
from .views import index, getReleases, getRelease, \
    getArtist, getArtists, getReleasesByArtistId

urlpatterns = [
    path('', index),
    path('getReleases/', getReleases),
    path('getReleasesByArtistsId/', getReleasesByArtistId),
    path('getRelease/', getRelease),
    path('getArtist/', getArtist),
    path('getArtists/', getArtists)
]
