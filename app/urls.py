from django.urls import path, include
from .views import index, getReleases

urlpatterns = [
    path('', index),
    path('getReleases/', getReleases)
]
