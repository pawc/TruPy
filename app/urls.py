from django.urls import path, include
from .views import index, getReleases, getRecord, \
    getArtist, getArtists, getReleasesByArtistId

urlpatterns = [
    path('', index),
    #path('getReleases/', getReleases),
    path('getReleasesByArtistsId/', getReleasesByArtistId),
    path('getRecord/', getRecord),
    path('getArtist/', getArtist),
    path('getArtists/', getArtists)
]
