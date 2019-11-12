from django.contrib import admin
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('<int:movie_pk>/delete/',views.delete, name='delete'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/edit/',views.edit, name='edit'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('index/', views.index, name='index'),
    path('<int:movie_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:movie_pk>/comments/<int:comment_pk>/' ,views.comments_delete, name='comments_delete'),
  
]
