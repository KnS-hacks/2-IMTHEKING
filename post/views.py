from django.shortcuts import render, redirect
from .models import Concert
import json
from django.db.models import Q

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
    }
    concertdict.append(content)

    key = request.GET.get('q', "")
    print(key)
    if key:
      concerts = concerts.filter(Q(concert_address__icontains=key))
      print(concerts)
      return render(request, 'main.html', {'concerts' : concerts})

  concertJson = json.dumps(concertdict)
  return render(request, 'main.html', {'concertJson':concertJson, 'addresses':addresses})


def location(request, Concert_id):
    concert=Concert.objects.get(id=Concert_id)
    if request.method == "POST":
      concert.latitude = request.POST.get('latitude', None)
      concert.longitude = request.POST.get('longitude', None)
      concert.concert_address = request.POST.get('concert_address', None)
      concert.save()
      return redirect('/post/detail/' + str(concert.id)) # location => select
    else:
      return render(request, 'selectlocation.html') # location => select

def upload(request):
  if request.method == "GET":
      return render(request, 'upload.html')
  elif request.method == "POST":
      concert = Concert()
      concert.concert_title = request.POST.get('concert_title', None)
      concert.concert_player = request.POST.get('concert_player', None)
      concert.concert_location = request.POST.get('concert_location', None)
      concert.concert_detail = request.POST.get('concert_detail', None)
      concert.concert_datetime = request.POST.get('concert_datetime', None)
      concert.concert_image = request.FILES.get('concert_image', None)
      concert.save()
      return redirect('/post/selectlocation/' + str(concert.id)) # location => select

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
      return redirect('/post/selectlocation/' + str(concert.id))

# def search(request):
#   search_word = request.GET['search']
#   addresses = Concert.objects.filter(concert_address__contains = search_word)

#   return render (request, 'main.html', {'addresses':addresses})
