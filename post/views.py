from django.shortcuts import render, redirect
from .models import Concert
import json


# Create your views here.
def main (request):
  concerts = Concert.objects.all()

  concertdict = []
  for concert in concerts:
    content = {
      "title": concert.concert_title,
      "palyer": concert.concert_player,
      "datetime": concert.concert_datetime,
      "address": concert.concert_address,
      "latitude": str(concert.latitude),
      "longitude": str(concert.longitude),
      "id": concert.id,
    }
    concertdict.append(content)

  concertJson = json.dumps(concertdict)
  return render(request, 'main.html', {'concertJson':concertJson})

def location(request):
    return render(request, 'selectlocation.html') # location => select

def upload(request):
  if request.method == "GET":
      return render(request, 'upload.html')
  elif request.method == "POST":
      concert_title = request.POST.get('concert_title', None)
      concert_player = request.POST.get('concert_player', None)
      concert_location = request.POST.get('concert_location', None)
      concert_detail = request.POST.get('concert_detail', None)
      concert_datetime = request.POST.get('concert_datetime', None)
      concert_image = request.FILES.get('concert_image', None)
      upload = Concert(concert_title=concert_title, concert_player=concert_player, concert_location=concert_location, concert_detail=concert_detail, concert_image=concert_image, concert_datetime=concert_datetime)
      upload.save()
      return render(request, 'selectlocation.html') # location => select
# 게시글 불러오기
def detail(request, Concert_id):
  concert = Concert.objects.get(id=Concert_id)
  return render(request, 'detail.html', {'concert':concert})

# 게시글 삭제하기
def delete(request, Concert_id):
  concert = Concert.objects.get(id=Concert_id)
  concert.delete()
  return redirect('/')

# 게시글 수정하기

def update(request, Concert_id):
  concert = Concert.objects.get(id=Concert_id)

  if request.method == "GET":
      return render(request, 'upload.html')
  elif request.method == "POST":
      concert.concert_title = request.POST.get('concert_title')
      concert.concert_player = request.POST.get('concert_player', None)
      concert.concert_location = request.POST.get('concert_location', None)
      concert.concert_detail = request.POST.get('concert_detail', None)
      concert.concert_datetime = request.POST.get('concert_datetime', None)
      concert.concert_image = request.FILES.get('concert_image', None)
      concert.save()
      return redirect('/post/detail/' + str(concert.id))