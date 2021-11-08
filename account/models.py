from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  nickname = models.CharField(max_length=40)

  def __str__(self):
    return self.nickname