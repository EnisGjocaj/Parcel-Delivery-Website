from django.contrib import admin
from django.urls import path

from . import views

app_name = "userProfile"

urlpatterns = [
    path('', views.profile_showcase, name="profile_showcase"),
    path('profile/modify/', views.profile_modify, name="profile_modify"),
]
