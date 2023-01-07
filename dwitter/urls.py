# dwitter/urls.py

from django.urls import path
from .views import dashboard, profile_list, profile,DetailUserView
from . import login

# app_name = "dwitter"

urlpatterns = [
    path('login',login.Login,name='Login'),
    path("logout",login.Logout,name="Logout"),
    path('register',login.AccountRegistration.as_view(), name='register'),
    path('',login.home,name=""),

    path("dashboard", dashboard, name="dashboard"),
    path("profile_list/",profile_list, name="profile_list" ),
        path("profile/<int:pk>", DetailUserView.as_view(), name="DetailUserView"),
    path("profile/<int:pk>", profile, name="profile"),


]