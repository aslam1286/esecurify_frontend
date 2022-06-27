from django.shortcuts import render

def index(requset):
    pass

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def forgot_password(request):
    pass

def reset_password(request):
    pass