# dwitter/urls.py

from django.urls import path
from . import login,views

# app_name = "dwitter"

urlpatterns = [
    path('login',login.Login,name='Login'),
    path("logout",login.Logout,name="Logout"),
    path('register',login.AccountRegistration.as_view(), name='register'),
    path('',login.home,name=""),

    path("dashboard", views.dashboard, name="dashboard"),
    path("UserView/<int:pk>", views.UserView.as_view(), name="UserView"),
    path("profile_list/", views.profile_list, name="profile_list" ),
    path("profile/<int:pk>", views.profile, name="profile"),
    
    path('UserView/<int:pk>/create/', views.UserCreate.as_view(), name='create'),
    path('UserView/<int:pk>/delete/', views.UserDelete.as_view(), name='delete'),
    path('UserView/<int:pk>/update/', views.UserUpdate.as_view(), name='update'),

    path('UserView/<int:pk>/comment/', views.CommentView.as_view(), name='comment'),
    path('UserView/<int:pk>/commentCreate/', views.CommentCreate.as_view(), name='commentCreate'),
    path('UserView/<int:pk>/commentDelete/', views.CommentDelete.as_view(), name='commentDelete'),
    path('UserView/<int:pk>/commentUpdate/', views.CommentUpdate.as_view(), name='commentUpdate'),
]