from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.urls import reverse


def index(request):
    return render(request, "dashboard.html")

def login(request):
    if request.method == 'POST':
        user_data = request.POST
        email = user_data['email']
        password = user_data['password']
        user = authenticate(request, username=email, password=password)
        
        if not user or user.userprofile.is_deleted:
            print("Hello")
            
            return render(request, 'login.html', {'error': 'Invalid username or password!'})
        auth_login(request, user)
        
        return JsonResponse({
            "retcode": 1
        })
        
    else:
        user = request.user
        if not user.is_authenticated:
            return render(request, 'login.html')
    return HttpResponseRedirect(reverse('accounts:dashboard'))


    
    return render(request, "login.html")

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('accounts:login_user'))

def register(request):
    if request.method == 'POST':
        user_data = request.POST
        first_name = user_data['first-name']
        last_name = user_data['last-name']
        email = user_data['email']
        password = user_data['password']
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
