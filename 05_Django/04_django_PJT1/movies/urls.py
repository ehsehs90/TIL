from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('<int:movie_pk>/delete/',views.delete),
    path('<int:movie_pk>/update/', views.update),
    path('<int:movie_pk>/edit/',views.edit),
    path('<int:movie_pk>/', views.detail),
    path('create/', views.create),
    path('new/', views.new),
    path('index/', views.index),
]
