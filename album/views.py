from django.shortcuts import render,redirect
from . import forms
from . import models
from album.forms import AlbumForm
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album_form=AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form=AlbumForm()
        
    return render(request,'add_album.html',{'form':album_form})

def edit_album(request,id):
    album=models.Album.objects.get(pk=id)
    album_form=AlbumForm(instance=album)
    if request.method == 'POST':
        album_form=AlbumForm(request.POST,instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    else:
        album_form=AlbumForm(instance=album)
        
    return render(request,'add_album.html',{'form':album_form})



