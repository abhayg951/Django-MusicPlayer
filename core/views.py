from django.http import QueryDict
from django.shortcuts import redirect, render
from core.models import Music, Album
from .forms import AddMusicForm


# Create your views here.

def home(request):
    music = Music.objects.all()
    music_list = list(Music.objects.all().values())
    return render(request, "index.html", {
        'music': music,
        "music_list": music_list
    })

def add_music(request):
    form = AddMusicForm()
    if request.method == 'POST':
        # request.POST will return the content of the form
        # request.FILES will return the files(audio_files, cover_image)

        print(f"this is the complete post data:- {request.POST}")

        form = AddMusicForm(request.POST, request.FILES)
        if form.is_valid:
            instance = form.save(commit=False)
            album = form.cleaned_data.get('album')
            print(f"this is instance:- {instance}")
            print(f"album: {album}")
            if album:
                music_album=Album.objects.get_or_create(name=album)
                print(music_album)
                instance.album=music_album[0]
                instance.save()
                return redirect("core:home")
            else:
                instance.save()
                return redirect("core:home")
            
        else:
            print()


    return render(request, "addPage.html",{
        'form':form
    })
