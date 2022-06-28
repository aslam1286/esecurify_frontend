from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    # path("", views.index, name="dashboard"),
    path("", views.login, name="login_user"),
    path('logout', views.logout, name='logout_user'),
    path("register", views.register, name="register_user"),
    path("reset_password", views.reset_password, name="reset_password"),
    path("settings", views.settings, name="settings"),
    path("forgot_password", views.forgot_password, name="forgot_password"),
    
]