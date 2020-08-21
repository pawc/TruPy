from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .music import get_releases, get_release
from django.views.decorators.clickjacking import xframe_options_exempt

def index(request):
    return render(request, 'releases.html');

def getReleases(request):
    artist = request.GET.get('artist')
    releases = get_releases(artist)
    return JsonResponse(releases, safe=False)

@xframe_options_exempt
def getRelease(request):
    id = request.GET.get('id')
    release = get_release(id)
    return render(request, 'release.html', {
        'artist': release.get('artist'),
        'title': release.get('title'),
        'year': release.get('year'),
        'label': release.get('label'),
        'img_url': release.get('img_url')
    })