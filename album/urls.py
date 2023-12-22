from django.contrib import admin
from django.urls import path,include
from . import views
from album.views import edit_album
urlpatterns = [
    path('add_album',views.add_album,name='add_album'),
    path('edit/<int:id>',edit_album,name='edit_album'),
]
