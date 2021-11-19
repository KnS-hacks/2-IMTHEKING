from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# Create your models here.

class User(AbstractUser):

   username = None
   
   username = models.CharField(default="username", max_length=64)
   email = models.EmailField(default="email", max_length=64, unique=True)
   password = models.CharField(default="password", max_length=64)

   objects = UserManager()

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []


   def __str__(self): 
        return self.username