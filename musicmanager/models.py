from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class ArtistGroup(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(Artist, related_name='groups')
    formed_date = models.DateField(blank=True, null=True)
    disbanded_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Release(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='releases')
    group = models.ForeignKey(ArtistGroup, on_delete=models.CASCADE, related_name='releases', blank=True, null=True)

    def __str__(self):
        return self.title

class Recording(models.Model):
    title = models.CharField(max_length=255)
    duration = models.DurationField()
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name='recordings')

    def __str__(self):
        return self.title

class AudioFile(models.Model):
    recording = models.ForeignKey(Recording, on_delete=models.CASCADE, related_name='audio_files')
    file = models.FileField(upload_to='audio_files/')
    format = models.CharField(max_length=50)
    bitrate = models.IntegerField()

    def __str__(self):
        return f"{self.recording.title} - {self.format}"