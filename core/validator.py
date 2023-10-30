from mutagen.mp3 import MP3
from django.core.exceptions import ValidationError
import os


def audio_validation(file):
    try:
        audio = MP3(file)

        if not audio:
            raise TypeError()

        file_check = True

    except Exception as e:
        file_check = False

    if not file_check:
        raise ValidationError("Unsupported file type.")

    valid_file_extensions = ['.mp3']
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extensions:
        raise ValidationError("Unsupported File Extension")
