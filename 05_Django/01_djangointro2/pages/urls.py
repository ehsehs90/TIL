from django.urls import  path
from . import views

urlpatterns = [
       path('static_sample/',views.static_sample),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('make/', views.art),
    path('result/', views.result),    
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('',views.index),
]
