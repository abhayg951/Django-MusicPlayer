from django.db import models
from core.helper import get_music_length
from core.validator import audio_validation


# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.ForeignKey("Album", on_delete=models.SET_NULL, null=True, blank=True)
    time_length = models.DecimalField(decimal_places=2, max_digits=20, blank=True)
    audio_file = models.FileField(upload_to='musics', validators=[audio_validation])
    cover_image = models.ImageField(upload_to='cover_images/')

    def save(self, *args, **kwargs):
        if not self.time_length:
            music_length = get_music_length(self.audio_file)
            self.time_length = music_length
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Album(models.Model):
    name = models.CharField(max_length=200)
