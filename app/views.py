from django.http import JsonResponse
from django.shortcuts import render
from .music import get_releases, get_release, get_artist, get_artists, get_releases_by_artistId
from django.views.decorators.clickjacking import xframe_options_exempt

def index(request):
    return render(request, 'releases.html', {
        'username': request.user.username,
        'is_authenticated': request.user.is_authenticated
    })

def getReleases(request):
    artist = request.GET.get('artist')
    releases = get_releases(artist)
    return JsonResponse(releases, safe=False)

def getReleasesByArtistId(request):
    artistId = request.GET.get('artistId')
    releases = get_releases_by_artistId(artistId)
    return JsonResponse(releases, safe=False)

def getArtists(request):
    artist = request.GET.get('artist')
    artists = get_artists(artist)
    return JsonResponse(artists, safe=False)

@xframe_options_exempt
def getRelease(request):
    id = request.GET.get('id')
    release = get_release(id)
    return render(request, 'release.html', {
        'artist': release.get('artist'),
        'title': release.get('title'),
        'year': release.get('year'),
        'label': release.get('label'),
        'img_url': release.get('img_url'),
        'tracks': release.get('tracks')
    })

@xframe_options_exempt
def getArtist(request):
    id = request.GET.get('id')
    artist = get_artist(id)
    return render(request, 'artist.html', {
        'name': artist.get('name'),
        'profile': artist.get('profile'),
        'img_url': artist.get('img_url')
    })