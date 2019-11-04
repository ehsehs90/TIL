## 2019 -10-31 (목) 전생직업 APP

###### Faker API 를 활용한 전생직업 App을 만들어보자



### [flow]

<1. 사전 작업>

	- Faker API 사용법 익히기 -> Shell Plus  이용
	-  `jobs` Application 생성

```shell
$ python manage.py startapp student
	- setting.py에 출생신고
	- student 디렉토리에 urls.py 파일 생성 / urls작성 (import 주의)
	- config > urls.py 에 student 앱 경로 바인딩 (import 주의)
	- `Template` 에 student 디렉토리 생성
    - student > models.py 모델 생성
$ python manage.py makemigration
$ python manage.py migrate
$ python manage.py shell
	from student.models import Student
	데이터 등록 student = Studnet()
	student.title = '이도현'
	student.content = '마크다운'
	student.save()
	exit()
Ctrl +Shift + p
open database > sqlite3 : 내가 작업하는 디렉토리 선택
아까 migrate 한 모델Table 잘 있는지 확인
student > view.py (앞으로 student 모델 객체 사용하려면 `임포트` 꼭!)

```







<2. 기능 구현>

- 사용자 이름을 입력받는 함수 (HTML Form 을 통해 건네줌)

  [기본]

   - 이름에 따라 전생의 직업을 알려주는 함수

     - Faker API 를 통해 직업 정보 가져오기

     - 해당 이름을 처음 조회할 때 이름 - 직업정보를 DB에 저장

       즉, 이름을 여러번 조회하더라도 처음 저장된 직업이 바뀌지 않음

  [심화]

  - GIPHY API 를 사용해서 직업에 따른 움짤도 함께 보여주기
  - GIPHY API 회원가입 & API KEY 발급 바딕
    - 공식 문서 보며 요청 보내서 움짤 받아보기
      - 사전에 주소창에 URL + 쿼리 스트링 직접 넣어보면서 사진 정보가 잘 오는지 먼저 테스트하기
  
  ​     
  
  
  
### 1.1 Faker 설치

  ```shell
  $ pip install Faker
  ```

  

  ### 1.1.1 Faker 사용하기

  ###### Shell_plus 를 이용해 Faker를 익혀보자

- Shell_plus 실행

  ```shell
  $ python manage.py shell_plus
  ```

  - Faker import 하기

    ```
    In [1] : from faker import Faker
    ```

  - Faker 생성

    ```python
    In [3] : fake = Faker()
    ```

    - Faker의 name

    ```python
    In [3] : fake = Faker()
    
    In[4] : fake.name
    out[4] : 'dohyun'  
    
    In[4] : fake.address()
    out[4] : '42404 John Plain/111111 , IM 4208'  
    
    
    ```

    - Faker의 text

    ```python
    In [9]: fake.text()
    Out[9]: 'Talk sport its environmental truth. Less political anything food.\nBit later big soon heavy practice. Much agree back speak whom agent media. Population bed once capital network challenge method.'
    
    ```

    - Faker의 job

    ```python
    In [11]: fake.job()
    Out[11]: 'Herpetologist'
    
    In [12]: fake.job()
    Out[12]: 'Runner, broadcasting/film/video'
    
    In [13]: fake.job()
    Out[13]: 'Horticultural consultant'
    ```

  - 한글로 Faker 생성

  ```python
  In [15]: fake=Faker('ko_KR')
  
  In [16]: fake.job()
  Out[16]: '의무기록사'
  
  In [17]: fake.job()
  Out[17]: '악기제조 및 조율사'
  
  In [18]: fake.job()
  Out[18]: '치과기공사'
  
  In [19]: fake.job()
  Out[19]: '간호조무사'
  ```

### 1.2 Jobs Application

#### 1.2.1 Application 생성

```shell
$ python manage.py startapp jobs
```

#### 1.2.1 Application 등록(출생신고)

- settings.py 에 jobs Application을 등록한다

#### 1.2.3 Model 등록 및 Migrate

- models.py

```python
from django.db import models

#create your models here.
class Job(models.Model):
    name = models.CharField(max_length=30)
    past_job = models.TextField()
    

```

- Model 등록 `makemigration`

  ```shell
  $ python manage. py makemigrations
  ```

- Model 등록 확인 `showmigrations`

```shell
$ python manage.py showmigrations
```

- migrate 후 테이블 생성 확인

  ```shell
  $ python manage.py migrate
  ```

### 1.3 관리자 페이지에 등록

  - admin.py

    ```python
    from django.contrib import admin
    from .models import Job
    
    #커스터 마이징 한 ModelAdmin
    class JobAdmin(admin.ModelAdmin):
        list_display = ('pk', 'name', 'past_job')
        
    admin.site.register(Job, JobAdmin)
    ```

### 1.4 Jobs App View와 Template 생성

 `views.py`

```python
import requests
from django.shortcuts import render
from faker import Faker
from .models import Jobs
# view 함수에서 모델객체를 사용하려면 import 해주어야 한다

def create(request):
    name = request.POST.get('name')    #html에서 입력한 이름
    # db 에 있는지 없는지 확인
    # (+) 필터걸기 ( 2개 이상은 에러 발생)
    user = Jobs.objects.filter(name=name).first()
    
    #유저 정보가 있을 때
    if user:
        past_job = user.past_job
        jobs = Jobs(name=name, post_job = past_job)
        
   # 유저 정보가 없을 때
	else:
        # db에 저장
        faker = Faker()
        past_job = faker.job()
        jobs = Jobs(name=name, past_job=past_job)
        
        jobs.save()
    
```

`templates`  

```html
<!-- index.html-->
{% extends 'base.html' %}
{% load static %}


{% block css %}
  <link rel="stylesheets" href="{% static 'stylesheets/sample.css'%}"
{% endblock %}
{% block body %}
{% comment %} {% url 'articles:create' %} {% endcomment %}
<h1 class ="text-center">전생에 무엇이었을까요.....</h1>
{% comment %} <form action="/articles/create/" method="POST"> {% endcomment %}
<form action="/jobs/create/" method="POST">
    {% csrf_token %}
    <hr>
    NAME : <input type="text" name="name">
    {% comment %} past_job: <textarea name ="past_job" cols="10" rows="10"></textarea><br> {% endcomment %}
    <input type ="submit">
</form>
<hr>
 <img src="{% static 'images/wowo.jpg' %}" alt="아이즈원 장원영" weight ="500px">
{% comment %} <a href = "/articles/index">[BACK] </a> {% endcomment %}
{% endblock %}

<!-- create.html -->
{% extends 'base.html' %}

{% block body %}
{% comment %} {% url 'articles:create' %} {% endcomment %}
<h1 class ="text-center">{{jobs.name}}님의 과거는...<hr>
{{jobs.past_job}}</h1>
{% comment %} <form action="/articles/create/" method="POST"> {% endcomment %}
<img src ={{img_url}} alt =  "그림" width="500px" height="500px">
<hr>
{% comment %} <a href = "/articles/index">[BACK] </a> {% endcomment %}
{% endblock %}
```



### 1.5 GIPHY API 사용(GIF)

##### api_key 와 api_url 을 사용해 전생 직업에 맞는 GIF 를 가져와요

```python
    #GIPHY API
    api_key = "EJrj23v________k3iovWjeusslgcm95"
    api_url = "http://api.giphy.com/v1/gifs/search"

    data = requests.get(f'{api_url}?api_key={api_key}&q={past_job}&limit=1&lang=ko').json()
    try:
        img_url = data.get('data')[0].get('images').get('original').get('url')

        #에러나면?
    except IndexError:
        img_url = None


    context ={ 'jobs':jobs ,'img_url':img_url}

    return render(request, 'jobs/create.html',context)

def index(request):
    return render(request, 'jobs/index.html')
```

