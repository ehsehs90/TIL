from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('<int:article_pk>/edit/', views.edit),
    path('<int:article_pk>/update/', views.update),
    path('<int:article_pk>/', views.detail),
    path('<int:article_pk>/delete/', views.delete),
    path('index/', views.index),
    path('new/', views.new),
    path('create/', views.create)
]