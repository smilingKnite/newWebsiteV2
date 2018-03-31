from django.conf.urls import url
from django.contrib import admin

from . import models, views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^photos$', views.photos),
    url(r'^designs$', views.designs),
    url(r'^me$', views.me),
    url(r'^work$', views.work),
]
