from django.shortcuts import render
from .models import User

def signup (request):
  return render (request, "signup.html")

def login (request):
  return render (request, "login.html")
