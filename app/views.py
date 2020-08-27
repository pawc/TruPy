from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render
from .music import get_releases, get_record, get_artist, get_artists, get_releases_by_artistId
from .models import FavRecord, ShelfRecord, WishRecord
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html', {
        'username': request.user.username,
        'is_authenticated': request.user.is_authenticated,
        'profile_controls_available': True
    })

def users(request):
    return render(request, 'users.html', {
        'username': request.user.username,
        'is_authenticated': request.user.is_authenticated,
        'profile_controls_available': False
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
    is_shelf = False
    is_wish = False

    if request.user.is_authenticated:
        if len(FavRecord.objects.filter(user=request.user, recordId=id)) > 0:
            is_fav = True
        if len(ShelfRecord.objects.filter(user=request.user, recordId=id)) > 0:
            is_shelf = True
        if len(WishRecord.objects.filter(user=request.user, recordId=id)) > 0:
            is_wish = True

    record['is_fav'] = is_fav
    record['is_shelf'] = is_shelf
    record['is_wish'] = is_wish
    record['is_user_authenticated'] = request.user.is_authenticated
    return JsonResponse(record, safe=False)

def getArtist(request):
    id = request.GET.get('id')
    artist = get_artist(id)
    return JsonResponse(artist, safe=False)

@login_required
def fav(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        response = HttpResponse()
        if len(FavRecord.objects.filter(recordId=id, user=request.user)) == 0:
            FavRecord.objects.create(recordId=id, user=request.user)
        response.status_code = 200
        return response
    else:
        return Http404

@login_required
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

@login_required
def shelf(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        response = HttpResponse()
        if len(ShelfRecord.objects.filter(recordId=id, user=request.user)) == 0:
            ShelfRecord.objects.create(recordId=id, user=request.user)
        response.status_code = 200
        return response
    else:
        return Http404

@login_required
def unshelf(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        response = HttpResponse()
        record = ShelfRecord.objects.filter(recordId=id, user=request.user)
        record.delete()
        response.status_code = 200
        return response
    else:
        return Http404

@login_required
def wish(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        response = HttpResponse()

        if len(WishRecord.objects.filter(recordId=id, user=request.user)) == 0:
            WishRecord.objects.create(recordId=id, user=request.user)
        response.status_code = 200
        return response
    else:
        return Http404

@login_required
def unwish(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        response = HttpResponse()

        record = WishRecord.objects.filter(recordId=id, user=request.user)
        record.delete()
        response.status_code = 200
        return response
    else:
        return Http404

@login_required
def getFavs(request):
    favs = FavRecord.objects.filter(user=request.user)
    results = []
    for fav in favs:
        record = get_record(fav.recordId)
        results.append({
            'recordId': fav.recordId,
            'artist': record['artist'],
            'artistId': record['artistId'],
            'title': record['title']
        })

    return JsonResponse(results, safe=False)

@login_required
def getShelf(request):
    shelf = ShelfRecord.objects.filter(user=request.user)
    results = []
    for s in shelf:
        record = get_record(s.recordId)
        results.append({
            'recordId': s.recordId,
            'artist': record['artist'],
            'artistId': record['artistId'],
            'title': record['title']
        })

    return JsonResponse(results, safe=False)

@login_required
def getWish(request):
    wishes = WishRecord.objects.filter(user=request.user)
    results = []
    for wish in wishes:
        record = get_record(wish.recordId)
        results.append({
            'recordId': wish.recordId,
            'artist': record['artist'],
            'artistId': record['artistId'],
            'title': record['title']
        })

    return JsonResponse(results, safe=False)

@login_required
def getUsers(request):
    users = User.objects.all()
    results = []
    for user in users:
        results.append({
            'name': user.username
        })

    return JsonResponse(results, safe=False)