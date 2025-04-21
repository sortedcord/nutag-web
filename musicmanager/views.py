from django.shortcuts import render
from .models import Artist, Release, Recording

def home(request):
    artists = Artist.objects.all()
    releases = Release.objects.all()
    recordings = Recording.objects.all()
    return render(request, 'musicmanager/index.html', {
        'artists': artists,
        'releases': releases,
        'recordings': recordings,
    })