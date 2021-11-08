from django.db import models

class Concert(models.Model):
  concert_title = models.CharField(max_length=40)
  concert_player = models.CharField(max_length=40)
  concert_location = models.CharField(max_length=40)
  concert_detail = models.TextField(default='')
  concert_image = models.ImageField(upload_to='post/', blank=True, null=True)
  latitude = models.FloatField(default=0.0)
  longitude = models.FloatField(default=0.0) 