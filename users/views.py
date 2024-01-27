from django.shortcuts import render

def home(request):
    return render(request, 'users/home.html')

def signin(request):
    return render(request, 'users/signin.html')

def signup(request):
    return render(request, 'users/signup.html')