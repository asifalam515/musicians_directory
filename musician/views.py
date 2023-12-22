from django.shortcuts import render,redirect
from . import form
from musician.form import MusicianForm
from . import models
# Create your views here
def musician(request):
    if request.method == 'POST':
        form=MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('add_musician')
    else:
        form=MusicianForm()
    return render(request,'add_musician.html',{'form':form})

def delete_musician(request,id):
    delMusician=models.Musician.objects.get(pk=id)
    delMusician.delete()
    return redirect('home')