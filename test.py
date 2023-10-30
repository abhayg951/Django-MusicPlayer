from mutagen.mp3 import MP3
from mutagen.id3 import ID3

song = MP3("media_root/musics/Living-Life-In-The-NightPagalWorld.mp3")
music = ID3("media_root/musics/Living-Life-In-The-NightPagalWorld.mp3")   

print(song.info.length.as_integer_ratio)
music_data = music.getall("APIC")[0].data
print(music_data)

file = open('myfile.jpg', 'wb')

file.write(music_data)

file.close()