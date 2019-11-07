from django.urls import path
from . import views



##여기서 앱 네임을 지정해줄 수 있다! -- 앱이 많아지면 힘들어지므로
app_name = 'articles'


urlpatterns = [
    # create / update url 통합하기
    # GET (edit) / POST (update)
    # GET(new) / POST (create)
    path('<int:article_pk>/comments/<int:comment_pk>/delete/',views.comments_delete, name="comments_delete"),
    path('<int:article_pk>/comments/',views.comments_create, name='comments_create'),
    path('<int:article_pk>/update/',views.update , name='update'),
    path('<int:article_pk>/delete/', views.delete, name= 'delete'),
    path('<int:article_pk>/', views.detail ,name ='detail'), #READ Logic - Index   
    path('index/', views.index ,name ='index'), #READ Logic - Index
    path('create/', views.create, name='create')

]