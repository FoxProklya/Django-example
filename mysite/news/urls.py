from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.conf.urls import re_path

from django.views.generic import ListView, DetailView
from news.models import Articles

urlpatterns = [
    path('',  ListView.as_view(queryset=Articles.objects.all().order_by('-date')[:20],template_name='news/posts.html')),

    re_path(r'^(?P<pk>\d+)$' , DetailView.as_view(model = Articles , template_name='news/post.html')),
]
# ?P одна группа
# <pk> праймори кей id

# \d проверка на число
# \d+ проверка на несколько чисел
# $ конец строки


#ListView много, DetailView одно

#urlpatterns = [
#    re_path(r'$', views.index, name='index'),

#]﻿
