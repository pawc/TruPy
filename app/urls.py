from django.urls import path, include
from .views import index, getReleases, getRelease

urlpatterns = [
    path('', index),
    path('getReleases/', getReleases),
    path('getRelease/', getRelease)

]
