from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django_media_serv import views
from django.contrib.auth import logout, login
from django.contrib.auth.views import LogoutView, LoginView
from django.conf import settings
from django.urls import path

urlpatterns = [
        url(r'^media/', views.getMediaFile, name='getMediaFile'),
]
