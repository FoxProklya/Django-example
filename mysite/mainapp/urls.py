from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.conf.urls import re_path

urlpatterns = [
    path('',  views.index, name='index'),
    path('contact/',  views.contact, name='contact'),
]

#urlpatterns = [
#    re_path(r'$', views.index, name='index'),

#]﻿
