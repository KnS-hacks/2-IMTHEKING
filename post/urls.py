from django.urls import path
from .views import * 

urlpatterns = [
    path('upload/', upload, name="upload"),
    path('', main, name="main"),
    path('location/', location, name="location"),
]