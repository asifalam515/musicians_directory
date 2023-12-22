from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    Album_name=models.CharField(max_length=20)
    musician=models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_release_date=models.DateField()
    rating=models.IntegerField()
    
    def __str__(self) -> str:
        return self.Album_name
    