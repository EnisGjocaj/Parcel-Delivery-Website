from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from . forms import LoginForm

from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name="core/login.html", authentication_form=LoginForm), name="login"),
    #  path('track-parcel/', views.track_parcel, name='track_parcel'),
]
