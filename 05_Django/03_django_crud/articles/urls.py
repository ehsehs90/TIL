from django.urls import path
from . import views



##여기서 앱 네임을 지정해줄 수 있다! -- 앱이 많아지면 힘들어지므로
app_name = 'articles'


urlpatterns = [
    path('<int:article_pk>/update/', views.update, name ='update'), 
    path('<int:article_pk>/edit/', views.edit, name ='edit'), #  UPDATE Logic - 폼 전달
    path('<int:article_pk>/delete/', views.delete, name ='delete'), #  DELETE Logic
    path('<int:article_pk>/', views.detail, name = 'detail'), # READ Logic - Detail
    path('create/', views.create, name ='create'),  # CREATE Logic - 데이터베이스에 저장
    path('new/', views.new, name ='new'),    #CREATE Logic - 사용자에게 폼 전달
    path('index/', views.index ,name ='index') #READ Logic - Index
]