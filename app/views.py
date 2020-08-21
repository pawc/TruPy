from django.http import JsonResponse
from django.shortcuts import render
from .music import get_releases

def index(request):
    return render(request, 'index.html');

def getReleases(request):
    artist = request.GET.get('artist')
    releases = get_releases(artist)
    return JsonResponse(releases, safe=False)