## Static File

- static files 기본 경로

  - 기본적으로 애플리케이션 안에 있는 `static` 디렉토리를 탐색해서 정적파일을 가져온다

- `{% load static %}`

  - 해당 페이지에 정적 파일들을 불러와서 사용하겠다고 선언한다
  - 일반적으로는 HTML 문서 상단에 위치한다
  - 상속받는 {% extends '[]' %} 태그가 존재하면, 태그 밑에 위치한다

  ```html
  {% extends 'base.html' %}
  {% load static %}
  ```

  

- `{% static %}`

  - 해당하는 경로에 있는 파일에 대해서 django 가 접근할 수 있는 절대 URL 경로를 생성한다

  - 실제 파일이 위치한 경로는 아니다!

    - 127.0.0.0:8000**/static/**articles/images/love.jpg

      -  [최상위 경로]

        - /static/ : 최상위 경로

        ```
        # 웹 사이트에서 사용할 정적 파일의 최상위 URL 경로
        STATIC_URL = '/static/'
        ```



## 1.  Static Files Customizing

###### static 파일의 경로를 커스터 마이징하여 사용할 수 있다



### 1.1 Static 디렉토리 생성

 - Application 아래에 static 폴더를 생성하여 이미지를 넣는다

   ```python
   articles/
   	__pycache__
       migrations
       static/
       	articles/
           	image/
               	love.jpg
   ```

   

 - index.html 에 해당 이미지를 띄운다

    - index.html

       - `{% load static %}` 을 반드시 추가한다

         ```html
         {% extends 'base.html' %}
         {% load  static %}
         {% block body %}
           <h1 class="text-center">Articles</h1>
           <hr>
         
           <img class="mx-auto" src="{% static 'articles/image/love.jpg' %}" alt="" style="display : block">
         
           <hr>
             <a href="{% url 'articles:create' %}">[NEW]</a>
           <hr>
         
           {% for article in articles %}
             <p>[{{article.pk}}] : {{article.title}}</p>
             <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
         
           <hr>
           
           {% endfor %}
           <hr>
         
         {% endblock  %}
         ```

         - 이때의 img 경로는 개발자도구로 확인해 보면 /static/articles/image/love.jpg

         

### 1.2 settings.py 수정

- 정적 파일이 위치한 경로를 설정한다

  - 앞으로 static 파일을 찾을 때, 아래 설정한 경로에 찾아가서 탐색한다

    - 개발 단계에서 사용 --> 실제 프로덕션 배포 단계에서는 다른 방식을 사용한다
    - `settings.py`

    ```python
    # config/ assets 로 Application에서 사용하는 정적 파일들을 가져온다.
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'config', 'assets'),
    ]
    ```

    

### 1.3 assets 디렉토리 생성

 - config/ assets 폴더 생성한 뒤, 모든 application 의 static 디렉토리 하위 폴더 및 파일들을 가져온다.

   ```
   config/
   	__pycache__
   	assets/
   		articles/
   			image/
   				love.jpg
   ```

   

### 1.4 Article Model 수정

###### image 필드를 추가하기

- 수정 전

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체 표시 형식 수정
    def __str__(self):
        return f'[{self.pk}] : {self.title} '
```

- 수정 후

  - 원래대로라면, 새로운 필드를 추가하고 나면, makemigrations할떄, 아딴 값을 넣을 것인지 Django 가 물어본다. 기본적으로 blank= False 이기 때문이다

  - `blank=True`

    - '빈 문자열' 이 들어가도 된다
    - `기본값으로 어떤 것을 넣을거야?` 라는 절차가 생략된다
    - 기본 값을 물어보는 절차가 생략되기 떄문에, 바로 `migrate`가 수행된다

    ```python
    from django.db import models
    
    class Article(models.Model):
        title = models.CharField(max_length=40)
        content = models.TextField()
    
        # 원래 대로 라면, 새로운 필드를 추가하고 나면, makemigrations 할때, 
        # 어떤 값을 넣을 것인지 Django 가 물어본다. 기본적으로 blank = False이기 때문이다.
        # blank=True : '빈 문자열' 이 들어가도 된다.
        image = models.ImageField(blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    
        # 객체 표시 형식 수정
        def __str__(self):
            return f'[{self.pk}] : {self.title} '
    ```



- Model 수정

  - makemigrations

    ```shell
    $ python manage.py makemigarions
    ```

  - Pillow 설치

    ```shell
    $ pip install Pillow
    ```

  - 다시 makemigrations
  
    ```shell
    $ python manage.py makemigrations
    ```
  
  - show로 확인하기
  
    ```shell
    $ python manage.py showmigrations
    ```
  
  - migrate 실행
  
    ```shell
    $ python manage.py migrate
    ```
  
  
  - sqlite 3 로 확인



## 2. 사용자 이미지 업로드

#### 사용자로부터 이미지 업로드 받아서 데이터 베이스에 저장하기

- `views.py`

  - request를 통해 Form으로 부터 이미지파일을 받을 때 `entype="multipart/form-data"으로 설정한다

    - POST 로 전송되는 Text와 파일을 따로 전송한다

      그래서 image는 POST가 아닌 **FILES** 로 찾는다

      `image = request.FILES.get('image')` 를 통해 이미지를 저장한다

      ```python
      # 사용자로부터 데이터를 받아서 DB에 저장하는 함수
      def create(request):
      
          # POST 요청 -> 게시글 생성 로직 수행
          if request.method == 'POST':
              title = request.POST.get('title')
              content = request.POST.get('content')        
              
              # POST로 전송되는 Text와 파일을 따로 전송한다.
              image = request.FILES.get('image')
              article = Article(title=title, content=content, image=image)
      
              article.save()    
              article_pk = article.pk
              return redirect('articles:detail', article_pk) # 2 URL Namespace
      
          # GET 요청 -> 사용자에게 폼 보여주기
          else :
              return render(request, 'articles/create.html')
      
      ```

- create.html

  - entype

    a. application/x-www-form-urlencoded

    	- 기본 값
    	- 모든 문자 인코딩

    b. multipart/form-data

    	- 파일 형태 첨부 시 필수 사용 / 데이터를 나누어 전송한다
    	- POST로 전송되는 Text와 파일을 따로 전송한다

    c. text/plaon

    	- 인코딩 x -> 사실상 사용하지 않는다

    ```html
    {% extends 'base.html' %}
    
    {% block body %}
      <h1 class="text-center">NEW</h1>
      <form action="{% url 'articles:create' %}", method="POST" enctype="multipart/form-data">
      {% csrf_token %}
        <label for="title">TITLE </label>
        <input type="text" id="title" name="title" > <br>
        <label for="content">CONTENT </label>
        <textarea type="text" id="content" name="content" cols="30" rows="10"> </textarea> <br>
    
        <input for="image"></label>
        <input type="file" name="image" id="image" accept="image/*" ><br>
    
        <input type="submit">
      </form>
    
      <hr>
      <a href="{% url 'articles:index' %}">[BACK]</a>
    
    {% endblock  %}
    ```

- admin 페이지에서 확인하기

  - admin.py

    ```python
    from django.contrib import admin
    from .models import Article
    from .models import Comment
    
    # Register your models here.
    
    class ArticleAdmin(admin.ModelAdmin):
        list_display = ('pk', 'title', 'content', 'image', 'created_at', 'updated_at',)
    
    class CommentAdmin(admin.ModelAdmin):
        list_display = ('pk', 'content', 'created_at', 'updated_at',)
    
    admin.site.register(Article, ArticleAdmin)
    admin.site.register(Comment, CommentAdmin)
    ```

- admin 페이지에서 이미지 저장 확인하기



##### [문제점] 이미지가 제대로 나오지 않는다

1. 이미지 저장되는 위치
   - 이미지 저장되는 위치가 App 밖에 저장되어 있어요!
2. img 가 db에 삽입되지 않음
   - 오타일 가능성 & migrate 확인(모델링)



## 3. 업로드 이미지 파일 저장 위치 Customizing

###### 업로드된 이미지 파일이 저장되는 위치도 커스터마이징해서 사용할 수 있다



- `settings.py` 수정

  - `MEDIA_URL` : 업로드된 파일의 주소를 만들어 주는 역할

  - MEDIA_ROOT : 실제로 파일이 업로드 된 다음에 어디로 배치가 될지

    ```python
    #MEDIA Files
    MEDIA_URL = '/media'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```

- config/ `urls.py`

  - `static()`

    - 첫번째 인자 : 어떤 URL 을 정적으로 추가할 지 (Media file)
    - 두번째 인자 : 실제 해당 미디어 파일은 어디에 있는지 ?

    ```python
    # settings 불러오기
    from django.conf import settings
    # static() 불러오기
    from django.conf.urls.static import static
    
    
    urlpatterns = [
        path('jobs/', include('jobs.urls') ),
        path('articles/', include('articles.urls') ),
        path('students/', include('students.urls') ),
        path('admin/', admin.site.urls),
    ]
    
    # static()
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    
    ```

    

##  4. 업로드 이미지 수정

> input type이 file 일 경우, value 값을 지정할 수 없다.
>
> - 이미지 파일은 바이너리 데이터 (하나의 덩어리)로 들어가서, 텍스트를 수정하듯이 일부만 수정하는 것이 불가능하다.
>
> **당장의 해결 방법은?**
>
> - 새로운 사진을 덮어씌우는 방식을 사용한다.
>
>   똑같은 사진을 업로드 하도록 **유도**한다. (임시 방편)
>
>   - 사진 파일을 업데이트 페이지에 띄운다.
>
>     만약, 이미지가 없는 경우 'no_image.jpg'를 띄운다.
>
>     **이미지가 있는 경우 VS 이미지가 없는 경우**



### 4.1 이미지가 있는 경우

> 부분 수정이 불가능하기 때문에 새로운 사진 업로드를 수행하도록 한다. 단, 기존에 사용자가 업로드 했던 이미지를 재 업로드하도록 유도하기 위해 기존의 이미지를 화면에 띄운다.





###  4.2 이미지가 없는 경우

> 샘플 이미지 (static/ image/ no_image.jpg) 를 넣어두고, 이미지 없는 게시글은 샘플 이미지가 나오도록 한다.



- no_image.jpg 이미지 파일의 아래와 같이 넣는다.



###  4.3 이미지 수정 코드

> 이미지가 없는 게시글에 이미지를 추가해보자!



- 수정하는 Update 로직 변경

  - `detail.html` 내 이미지 여부 확인

    ```html
    {% if article.image %}
      <p class="mx-auto" >업로드 되어있는 사진</p>
      <img class="mx-auto" src="{{article.image.url}}" alt="{{article.image}}" style="display : block; width : 50%">
    
    {% else %}
      <p class="mx-auto" >사진이 없어요....</p>  
      <img class="mx-auto" src="{% static 'articles/image/no_image.png' %}" alt="no_image" style="display : block">
    {% endif %}
    ```

  - `update.html` 내 이미지 여부 확인

    ```html
    {% if article.image %}
      <p class="mx-auto" >업로드 되어있는 사진</p>
      <img class="mx-auto" src="{{article.image.url}}" alt="{{article.image}}" style="display : block;">
    
    {% else %}
      <p class="mx-auto" >사진이 없어요....</p>  
      <img class="mx-auto" src="{% static 'articles/image/no_image.png' %}" alt="no_image" style="display : block">
    {% endif %}
    ```

  - form의 enctype 설정

    `enctype="multipart/form-data"` 설정!

    ```html
    <form action="{% url 'articles:update' article.pk %}", method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        <label for="title">TITLE </label>
        <input type="text" id="title" name="title" value={{article.title}} > <br>
    
        <label for="content">CONTENT </label>
        <textarea type="text" id="content" name="content" cols="30" rows="10">{{article.content}} </textarea> <br>
    
        <input type="submit">
        <label for="image">IMAGE </label>
        <input type="file" id="image" name="image"  > <br>
    </form>
    ```

  - views.py

    ```python
    # 수정된 내용을 전달 받아서 DB에 저장 (반영)
    def update(request, article_pk):
    
        article = Article.objects.get(pk=article_pk)
    
        # POST 요청 -> DB 수정사항 반영
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            image = request.FILES.get('image')
    
            article.image = image
            article.title = title
            article.content = content
            article.save()
    
            return redirect('articles:detail', article_pk)
    
        # GET 요청 -> 사용자에게 수정 Form 전달
        else :
            context = {
                'article' : article,
            }
    
            return render(request, 'articles/update.html', context)
    ```

