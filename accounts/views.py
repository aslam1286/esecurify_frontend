from django.shortcuts import render

def index(requset):
    pass

def login(request):
    return render(request, "login.html")

def register(request):
    pass

def forgot_password(request):
    pass

def reset_password(request):
    pass