from django.urls import path

from . import views

urlspattens = [
    path('', views.index, name='index'),
]