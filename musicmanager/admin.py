from django.contrib import admin
from .models import Artist, ArtistGroup, Release, Recording, AudioFile

# Register your models here.
admin.site.register(Artist)
admin.site.register(ArtistGroup)
admin.site.register(Release)
admin.site.register(Recording)
admin.site.register(AudioFile)
