from django.urls import path
from .views import index, getFavs, getShelf, getWish, getRecord, \
    getArtist, getArtists, getReleasesByArtistId, fav, unfav, \
    shelf, unshelf, wish, unwish, users, getUsers

urlpatterns = [
    path('', index),
    path('getFavs', getFavs),
    path('getShelf', getShelf),
    path('getWish', getWish),
    path('getReleasesByArtistsId/', getReleasesByArtistId),
    path('getRecord/', getRecord),
    path('getArtist/', getArtist),
    path('getArtists/', getArtists),
    path('fav/', fav),
    path('unfav/', unfav),
    path('shelf/', shelf),
    path('unshelf/', unshelf),
    path('wish/', wish),
    path('unwish/', unwish),
    path('users/', users),
    path('getUsers/', getUsers)
]
