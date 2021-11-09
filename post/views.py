from django.shortcuts import render
from .models import Concert

def upload(request):
    if request.method == "GET":
        return render(request, 'upload.html')
    elif request.method == "POST":
        concert_title = request.POST.get('concert_title', None)
        concert_player = request.POST.get('concert_player', None)
        concert_location = request.POST.get('concert_location', None)
        concert_detail = request.POST.get('concert_detail', None)
        concert_image = request.FILES.get('concert_image', None)
        upload = Concert(concert_title=concert_title, concert_player=concert_player, concert_location=concert_location, concert_detail=concert_detail, concert_image=concert_image)
        upload.save()
        return render(request, 'location.html')
def main(request):
    return render(request, 'main.html')

def location(request):
    return render(request, 'location.html')