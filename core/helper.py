from mutagen.mp3 import MP3


def get_music_length(file):
    music = MP3(file)
    return music.info.length
