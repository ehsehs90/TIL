from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('update/', views.update, name='update'),
    path('password/', views.password, name='password'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),

]