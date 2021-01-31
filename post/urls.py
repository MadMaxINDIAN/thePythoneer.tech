# IMPORTS
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('b/comment/<str:blog_title>', views.comment),
    path('b/create_blog', views.create_blog),
    path('b/update_blog/<str:title>', views.update_blog),
    path('b/<str:blog_title>', views.blog),
    path('u/create_user', views.create_user),
    path('u/login_user', views.login_user),
    path('u/logout_user', views.logout_user),
]
