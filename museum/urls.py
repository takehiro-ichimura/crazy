from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('posts', views.post_list, name='post_list'),
    path('', views.top, name='top'),
    path('posts/<int:post_id>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]