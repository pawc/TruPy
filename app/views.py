from django.http import JsonResponse
from django.shortcuts import render
from .music import get_releases, get_record, get_artist, get_artists, get_releases_by_artistId
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
def getRecord(request):
    id = request.GET.get('id')
    record = get_record(id)
    return JsonResponse(record, safe=False)

@xframe_options_exempt
def getArtist(request):
    id = request.GET.get('id')
    artist = get_artist(id)
    return JsonResponse(artist, safe=False)
