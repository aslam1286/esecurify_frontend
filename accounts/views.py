from telnetlib import STATUS
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, "dashboard.html")

def login(request):
    return render(request, "login.html")

def logout(request):
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        print("request.post>>>>>", request.POST)
        return JsonResponse({"retcode":1})
    return render(request, "register.html")

def forgot_password(request):
    return render(request, "forgot_password.html")
    
def reset_password(request):
    pass

def settings(request):
    return render(request,'settings.html')
