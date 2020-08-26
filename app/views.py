from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render
from .music import get_releases, get_record, get_artist, get_artists, get_releases_by_artistId
from .models import FavRecord

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

def getRecord(request):
    id = request.GET.get('id')
    record = get_record(id)
    is_fav = False
    if len(FavRecord.objects.filter(user=request.user, recordId=id)) > 0:
        is_fav = True
    record['is_fav'] = is_fav
    return JsonResponse(record, safe=False)

def getArtist(request):
    id = request.GET.get('id')
    artist = get_artist(id)
    return JsonResponse(artist, safe=False)

def fav(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        response = HttpResponse()
        FavRecord.objects.create(recordId=id, user=request.user)
        response.status_code = 200
        return response
    else:
        return Http404

def unfav(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        response = HttpResponse()
        record = FavRecord.objects.filter(recordId=id, user=request.user)
        record.delete()
        response.status_code = 200
        return response
    else:
        return Http404