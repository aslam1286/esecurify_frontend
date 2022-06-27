from django.shortcuts import render

def index(request):
    return render(request, "dashboard.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def forgot_password(request):
    return render(request, "forgot_password.html")
    

def reset_password(request):
    pass