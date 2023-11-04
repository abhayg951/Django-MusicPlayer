from mutagen.mp3 import MP3
from mutagen.id3 import ID3


def get_music_length(file):
    music = MP3(file)
    return music.info.length


def get_music_title(file):
    print(file)
    file_name = str(file)
    print(file_name.rstrip(".mp3"))
    return str(file_name.rstrip(".mp3"))
