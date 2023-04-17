"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import main, about, blog_post, blog_post_add_comment, \
                        create_new_post, update_post, delete_post, \
                        show_user_profile, change_password, register_user, \
                        login_user

urlpatterns = [
    path('blogs/', main, name='blogs'),
    path('about/', about),
    path('', main, name='blogs'),
    path('blogs/<slug:slug>/', blog_post, name='blog_post'),
    path('blogs/<slug:slug>/comment', blog_post_add_comment),
    path('create/', create_new_post),
    path('blogs/<slug:slug>/update', update_post),
    path('blogs/<slug:slug>/delete', delete_post),
    path('profile/<str:username>/', show_user_profile),
    path('profile/<str:username>/change_password', change_password),
    path('register', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', main)

]
