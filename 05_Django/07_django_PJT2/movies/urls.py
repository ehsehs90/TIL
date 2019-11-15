from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static


app_name = 'movies'


urlpatterns = [
    path('<int:movie_pk>/ratings/new/', views.ratings_new, name='ratings_new'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    
]

