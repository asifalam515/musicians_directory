from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('add_musician',views.musician,name='add_musician'),
    path('delete_musician/<int:id>',views.delete_musician,name='delete_musician'),
]
