from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import UserProfile


def index(request):
    return render(request, "dashboard.html")

def login(request):
    
    return render(request, "login.html")

def logout(request):
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        user_data = request.POST
        first_name = user_data['first-name']
        last_name = user_data['first-name']
        email = user_data['email']
        password = user_data['email']
        confirm_password = user_data['confirm-password']
        if password == confirm_password:
            user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = email,
                password = password,
            )
            UserProfile(
                user = user
            ).save()
            return JsonResponse({"retcode":1})
        else:
            return JsonResponse({"retcode":0})
    return render(request, "register.html")

def forgot_password(request):
    return render(request, "forgot_password.html")
    
def reset_password(request):
    pass

def settings(request):
    return render(request,'settings.html')
