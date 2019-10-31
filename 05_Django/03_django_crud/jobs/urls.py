from django.urls import path
from . import views



#여기서 앱 네임을 지정해줄 수 있다! -- 앱이 많아지면 힘들어지므로
app_name = 'jobs'


urlpatterns = [
   
    # path('<int:student_pk>/', views.detail, name = 'detail'), # READ Logic - Detail
    # path('create/', views.create, name ='create'),  # CREATE Logic - 데이터베이스에 저장
    # path('new/', views.new, name ='new'),    #CREATE Logic - 사용자에게 폼 전달
    path('index/', views.index ), #READ Logic - Index
    path('create/', views.create),
]