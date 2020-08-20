from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from.music import get_releases

# Create your views here.
def releases(request):
    releases = get_releases('Porcupine Tree')
    return render(request, 'index.html', {
        'releases': releases
    })