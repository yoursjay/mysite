from django.contrib import admin
from django.urls import path,include
from .views import blog_page,blog_detial

urlpatterns = [
    path('', blog_page,name='blog_page'),
    path('<int:blog_pk>',blog_detial,name='blog_detial')
]