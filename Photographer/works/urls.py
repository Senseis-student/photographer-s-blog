from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.works, name='works'),
    path('/form_send', views.form_send, name= 'add_form'),
]