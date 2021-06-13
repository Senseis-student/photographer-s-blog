from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('id<int:post_id>', views.view_post, name='view_post'),
    path('id<int:post_id>/add_new_comment', views.add_new_comment, name= 'add_comment')
]