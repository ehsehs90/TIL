## 19.10.30(수) Django CRUD 구현

### 0. 사전작업

### 0.1 프로젝트 생성

```bash
$ django-admin startproject config .
```

### 0.2 애플리케이션 생성

```bash
$ python manage.py startapp articles
```

```python
#settings.py : 출생신고 까먹지 말자
INSTALLED_APPS = [
    'articles',
    ...
]

```

### 0.3 URL 분리(위임)

```python
# 경로설정
TEMPLATES = [
    {
       ...
        'DIRS': [os.path.join(BASE_DIR,'config','templates')],
            ...
    }
]
```

```python
#config/urls.py
from django.urls import path, include

urlpatterns = [
    # 사용자 요청 경로가 articles/로 시작하면 articles 앱 안에 있는 		urls.py로 이동!
    path('articles/', include('articles.urls')),
]
```

```python
# articles/urls.py
from . import views

urlpatterens = [
    #articles/ 로 요청했을 경우 index 함수 실행
    path('', views.index),
]
```





### 0.4 템플릿 경로 커스터마이징 + `base.html` 만들기

- 29일(화) 수업내용 확인
- 아래 코드 템플릿이 깨질 경우 base.html에 Bootstrap CSS, JS 파일 적용했는지 확인한다(슬랙 공지사항으로 `base.html` 드렸어요)

### 01. 데이터베이스 모델링

- 데이터베이스 모델링

`models.py`

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'
```

`makemigrations`:설계도 만들기

```bash
$ python manage.py makemigrations
```

```
03_django_crud/
	config/
    articles/
    	migrations/
        	0001_initial.py
```

`migrate` : 실제 DB에 반영하기

```bash
$ python manage.py migrate
```

- 추가정보

  - `showmigrations ` :  makemigrations를 통해 만든 설계도가 실제DB에 반영된 상태인지 아닌지 확인

  - `sqlmirate`:실제 DB에 반영하기 전 SQL쿼리문으로 바뀐 모습 확인

    ```bash
    $ python manage.py sqlmigrate
    ```

    

### 1.CREATE

- 기본적으로 두 개의 뷰 함수로 구성된다.
  	1. 사용자에게 HTML Form 을 던져줄 함수
   	2. HTML Form 에서 데이터를 전달받아서 실제 DB에 전달하는 함수

```python
#articles/views.py

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article(title=title, content=content)
    article.save()
    return render(request, 'articles/create.html')

```

```html
<!-- articles/new.html -->
{% extends 'base.html' %}

{% block body %}
<h1 class ="text-center">NEW</h1>
<form action="/articles/create/" method="GET">
    {% csrf_token %}
    TITLE : <input type="text" name="title"><br>
    CONTENT: <textarea name ="content" cols="30" rows="10"></textarea><br>
    <input type ="submit">
</form>
<hr>
<a href = "/articles/index">[BACK] </a>
{% endblock %}

<!-- articles/ create.html -->
{% extends 'base.html' %}
{% block body %}
<h1> 글 작성이 완료됐습니다 </h1>
<hr>
{% endblock %}
```

- 데이터가 정상적으로 저장됐는지 확인하기 위해 admin 페이지로 들어가보자

  - admin 계정 생성

    ```bash
    $ python manage.py createsuperuser
    ```

  - `admin.py`등록

    ```python
    from django.contrib import admin
    from .models import Article
    
    
    # Register your models here.
    class ArticleAdmin(admin.ModelAdmin):
        list_display = ('pk', 'title','created_at','updated_at',)
    admin.site.register(Article, ArticleAdmin)
    ```

- 메인 페이지에서 게시글 목록이 나오게 해보자 (Read - Index로직)

```python
# articles/views.py

def index(request):
    articles = Article.objects.all()[::-1]
    context = {'articles':articles}
    return render(request, 'articles/index.html',context)
    
```

```html
<!-- articles/index.html -->

{% extends 'base.html' %}
{% block body %}


<h1 class ="text-center"> articles의 index.html입니다</h1>
<a href = "/articles/new/"> [new] </a>
<hr>
{% for article in articles %}
	<p>글 번호 : {{article.pk}}</p>
	...
	<p>수정시각 : {{article.updated_at}}</p>
	<hr>
{% endfor %}
{% endblock %}
```

- 게시글 작성 요청 방식을 GET에서 POST 방식으로 바꾸어보자
  - 지금은 GET요청으로 보내고 있어서 쿼리스트링에 데이터가 노출되고 있다. 이는 우리 서버의 데이터 구조가 노출될 위험도 있고, URL 경로로만 게시글 작성이 가능하면 서버 폭파의 위험성이 증가한다.
  - POST 요청으로 바꾸어 HTTP body에 내용을 숨기고 작성자의 신원을 확인하는 절차를 거치도록 하자.

```html
<!-- articles/new.html -->
{% extends 'base.html' %}

{% block body %}
<h1 class ="text-center">NEW</h1>
<form action="/articles/create/" method="POST">
    {% csrf_token %}}
    TITLE : <input type="text" name="title"><br>
    CONTENT: <textarea name ="content" cols="30" rows="10"></textarea><br>
    <input type ="submit">
</form>
<hr>
<a href = "/articles/index">[BACK] </a>
{% endblock %}
```

```python
#articles/views.py

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content= request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()    
    
    return render(request,'articles/create.html')
```

- 지금은 게시글 작성을 완료한 뒤 "게시글 작성이 완료됐어요"라는 어색한 로직으로 구현되어 있다.
  - 데이터베이스에게 게시글 작성이 완료되면 메인페이지로 `redirect`시켜버리자

```python
from django.shortcuts import render, redirect

def create(request):
    title = request.POST.get('title')
    content= request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()    
    
    return redirect('/articles/')
```

### 2.READ(Detail 페이지)

게시글 목록이 출력되는 메인페이지에서 글 내용, 수정 시각 등 모든 정보를 보여줄 필요는 없다. **메인페이지에선 글 번호, 글 제목과 같은 기본적인 내용**만 보여주고, **사용자가 클릭했을 때 게시글 상세정보 페이지로 이동**하도록 만들어보자.

```python
#views.py : Variable Routing 적용
# 사용자로부터 요청한 URL로부터 게시글 PK 값을 건네받는다.
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article' : article}
    return render(request,'articles/detail.html', context)

```

```python
# urls.py : Variable Routing 적용
# 사용자가 게시글을 조회할 때 articles/1, articles/2 처럼 게시글들 중에 1번 게시글, 게시글들 중에 2번 게시글과 같은 모습으로 접근하는것이 자연스럽다.
urlpatterns = [
    path('<int:article_pk>',views.detail), 
    ...
]

```

```html
<!-- detail.html -->
{% extends 'base.html' %}

{% block body %}
<h1 class="text-center">DETAIL</h1>
<p>글 번호 : {{article.pk}}</p>
<p>글 제목 : {{article.title}}</p>
<p>글 내용 : {{article.content}}</p>
<p>생성 시각 : {{article.created_at}}</p>
<p>수정 시각 : {{article.updated_at}}</p>
<hr>
<a href="/articles/index">[back]</a>
{% endblock %}

<!-- index.html -->
{% extends 'base.html' %}

{% block body %}
<h1 class ="text-center"> articles의 index.html입니다</h1>
<a href = "/articles/new/"> [new] </a>
<hr>
{% for article in articles %}
<p>[{{article.pk}}] {{article.title}}</p>
<a href="/articles/{{article.pk }}">[DETAIL]</a>
<hr>
{% endfor %}
{% endblock %}
```



### 3.UPDATE

```python
# 사용자한테 게시글 수정 폼을 전달
# 사용자가 게시글을 수정할 때 원래의 게시글 내용이 필요하다 - article_pk값필요

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/edit.html', context)


## 수정 내용 전달받아서 DB에 저장(반영)
def update(request, article_pk):

	# 1. 수정할 게시글 인스턴스 가져오기
	article = Article.objects.get(pk=article_pk)   
	# 2. 폼에서 전달받은 데이터 덮어쓰기
	article.title=request.POST.get('title')
	article.content = request.POST.get('content')    
	#3. DB저장    
	article.save()
	# 4. 저장 끝났으면 게시글 Detail로 이동시키기
	return redirect(f'/articles/{article.pk}/')  
```
```python
#urls.py

path('<int:article_pk>/update/', views.update, name ='update'), 
path('<int:article_pk>/edit/', views.edit, name ='edit'), 
#  UPDATE Logic - 폼 전달
```



```html
<!-- update.html -->

{% extends 'base.html' %}

{% block body %}

<h1 class ="text-center"> CREATE </h1>
<form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}}
    TITLE : <input type="text" name="title" value="{{article.title}}"><br>  <!-- input 할 때 값 미리 채워주는것 value-->
    CONTENT: <textarea name ="content" cols="30" rows="10">
    {{article.content}}
    
    </textarea><br> <!--value 기능? 이따로 없음 :: texetarea 열고 닫히는 구간에 넣어준다--> 
    <input type ="submit">
</form>
<hr>
<a href = "{% url 'articles:detail' article.pk %}">[BACK] </a>


{% endblock %}
```



### 4.DELETE

```python
#views.py : Variable Routing 적용
# 사용자로부터 요청한 URL로부터 게시글 PK 값을 건네받는다.
def delete(request, article_pk):
    article= Article.objects.get(pk=article_pk)
    article.delete()
    

    return redirect('/articles/index/')
```

```python
# urls.py : Variable Routing 적용

urlpatterns = [
    path('<int:article_pk>/delete/',views.delete), 
    ...
]

```

```python

```

