# 1. Like

> `user` 는 여러개의 `Article`에 좋아요 표시를 할 수 있고
>
> `Article`은 여러명의 `User` 에게 좋아요를 받을 수 있다

### 1.1 Model 설정

- `blank=True`

  - 최초 작성되는 글에는 좋아요가 없고, 글이 작성되더라도 좋아요를 받지 못할 수도 있다.
  - 이 옵션을 줘서 유효성 검사를 통과한다
  - 실제 데이터베이스에는 null 이들어가는게 아니라 빈스트링 ('` `') 형태로 들어간다

  ```python
  from django.conf import settings
  
  class Article(models.Model):
      title = models.CharField(max_length=40)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
  
  ```

  

- 현재 상황에서 `related_name`설정은 필수
  - `like_users`필드에 related_name을 쓰지 않으면, User 입장에서 ㅁarticle_set을 사용할 경우 user필드를 그져올 지 like_users필드를 갖고 올지 인식하지 못한다
  - related_name설정과 함께 해당 필드는 article_set과 같은 방식으로 호출하지 못하고, like_users방식으로 호출해야한다
- 사용할 수 있는 ORM기능(명령어)
  - `user.article_set.all()`: 유저가 작성한 게시글 전부 (1:N)
  - `user.like_articles.all()` : 유저가 좋아요 누른 게시글 전부 (M:N)
  - `article.user`: 게시글 작성한 유저 - (1:N)
  - `article.like_users`: 게시글 좋아요 누른 유저 전부 (M : N)



### 1.2 View & URL

- `exists() & filter()`

  - filter() : 특정한 조건에 맞는 레코드들을 가져온다.
  - exists() : 최소한 하나의 레코드가 존재하는지 여부를 말해준다.

- `get() & filter()`

  - get() : 데이터가 없는 경우 에러 발생
  - filter() : 데이터가 없으면 빈 쿼리셋을 리턴





### 1.3 Template

#### 1.3.1 Template 분리 (_article.html)

- 모듈화한 템플릿은 제목 앞에 언더스코어(_) 붙여주는 것이 코딩 컨벤션

  ```python
  articles/
  	templates/
      	articles/
          	_article.html
              index.html
              ...        
          
  ```

  

- Bootstrap Card 컴포넌트를 사용해서 예쁘게 꾸며보자

  - Bootstrap 공식 홈페이지 > Documentation > cards

    ```html
    <!-- articles/index.html -->
    ...
    <div class="row">
        {% for article in articles %}
        	{% include 'articles/_article.html' %}
        {% endfor %}  
    </div>
    ```

    ```python
    <!-- articles/_article.html -->
    <div class ="col-12 col-md-6">
    	카드디자인
    </div>
    ```

    

#### 1.3.2 Font-Awesome 아이콘 적용

> Font-Awesome 홈페이지 가입 후 kits 로 들어가 코드 복사

```html
<!-- base.html-->

<head>
  ...  
  <!-- FontAwesome -->
  <script src="https://kit.fontawesome.com/0b59b957c4.js" crossorigin="anonymous"></script>
</head>

```

```html
<!-- articles/_article.html -->
...
 <div class="col-12 col-md-6 mb-3">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{article.title}}</h5>
        <p class="card-text">       
        <a href="{% url 'articles:like' article.pk %}"> 
        <!-- 사용자가 좋아요 누른 상태 -> 꽉찬 하트 -->
          {% if request.user in article.like_users.all %}
            <i class="fas fa-heart"></i>            
          <!-- 사용자가 좋아요 안 누른 상태 -> 빈 하트-->
          {% else %}
            <i class="far fa-heart"></i>
          {% endif %}
          </a><br>
        
        {{article.like_users.all|length}}명이 좋아요
        {{article.created_at}}</p><br>        
        
        <a href="{% url 'articles:detail' article.pk %}" class="btn btn-primary">상세보기</a>
      </div>
    </div>
  </div>
```



# 2. Profile 페이지

> 각 유저마다 프로필 페이지를 만들어주자

- User 에 대해서 CRUD 로직을 구현한다고 생각하면, READ(Detail)에 속한다

### 2.1 View & URL

- User에 대한 CRUD 로직 대부분을 accounts 앱에서 구현했으므로,  Profile페이지 역시 accounts 앱에 구현해보자.

```python
# accounts/views.py


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
```

```python
# accounts/urls.py
```

