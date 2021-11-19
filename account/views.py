from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from .models import User
from django.contrib import auth
from django.contrib.auth import login

# Create your views here.

def login(request):
    return render(request,'login.html')

def signin(request):
    if request.method == "GET":
        return render(request, 'signin.html')
    elif request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is None:
            print("인증 실패")
            return  render (request, 'signin.html')
        else: 
            print("인증 성공")
            auth.login(request, user)
            return render(request, 'fi.html')
            response.set_cookie('email', email)
            response.set_cookie('password', password)
            return response
    return render(request, 'fi.html')

def signup(request):
    if request.method == "POST":
        email = request.POST.get('email', False)
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        re_password = request.POST.get('re_password', False)
        if password != re_password :
            return render(request, 'signup.html' , {'error' : 'password incorrect!'})
        else:
           user = User.objects.create_user(email, password)
           user.re_password = re_password
           user.username = username
           user.save()

           return redirect('/')

    return render(request, 'signup.html')

def logout(request):
    if request.method == "POST" :
        auth.logout(request)
        return redirect('/', {'caution':'로그아웃 되었습니다'})
    
def fi(request):
    return render(request, 'fi.html')