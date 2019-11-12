

# User -Article & Comment

###### django 가 프로젝트를 실행시키면, `INSTALLED_APPS` 를 들고오고, 각 Application에 해당하는 model 들을 import 한다. 그래서 import 한 뒤에 사용할 수 있다.

- 만약 User를 사용해서 정의하는 경우, import 되지 않았을 때 사용해야 하는 경우가 발생한다.

  - `get_user_model()`

    - 클래스의 모델이 먼저 import 될 수 있도록 해야한다

  - `settings.AUTH_USER_MODEL`

    - 순서의 영향을 받지 않기 때문에 모델 정의할 때 사용하도록 한다.

      

- user 클래스를 가져오는 법

  - `settings.AUTH_USER_MODEL`

    - return str

    - models.py 에서 모델 정의할 때만 사용

      ```python
      from django.conf import settings
      settings.AUTH_USER_MODEL
      ```

      

  - `get_user_model()`

    - return class

    - `models.py` 제외한 모든 곳

      ```python
      from django.contrib.auth import get_user_model
      get_user_model()
      ```

      

## 1. User - Article

###### 작성한 게시글이 어떤 User의 것인지를 보이도록 로직을 변경해보자

### [CREATE] 게시글 작성자 정보 넣기

#### 1.1 Article 모델 클래스 수정

- 모델 정의
  - 게시글 작성자에 대한 정보를 넣기 위해 Article클래스에 User클래스를 외래키로 설정한다.

   - ```python
     # 수정 전
     class Article(models.Model):
         title = models.CharField(max_length=40)
         content = models.TextField()
         created_at = models.DateTimeField(auto_now_add=True)
         updated_at = models.DateTimeField(auto_now=True)
         
         def __str__(self):
             return f'[{self.pk}] {self.title}'
         
     # 수정 후 (user 컬럼 추가)
     from django.db import models
     from iamgekit.models import ProcessedImageField
     from imagekit.processors import Thumbnail
     from django.conf import settings
     
     class Article(models.Model):
         title = models.CharField(max_length=40)
         content = models.TextField()
         created_at = models.DateTimeField(auto_now_add=True)
         updated_at = models.DateTimeField(auto_now=True)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
         
         # 객체 표시 형식 
         def __str__(self):
             return f'[{self.pk}] {self.title}'
     ```
     
   - 수정 후 makemigrations migrate

     ```shell
     $ python manage.py makemigrations
     $ python manage.py migrate
     ```




- 새로운 게시글을 작성할 때 작성자에 대한 정보를 넣는 로직을 추가한다

  - views.py

    - article이 바로 저장되지 않도록 `article=form.save(commit=False)`를 설정한다
    - `request.user`를 이용해 게시글 작성자를 설정한 뒤, `article.save()` 를 통해 새로운 게시글을 등록한다

    ```python
    @login_required
    def create(request):
        if request.method=='POST':
            form =ArticleForm(request,POST)
            if form.is_valid()
            article=form.save(commit=False)
            article.user=request.user
            article.save()
            return redirect('articles:detail', article.pk)
        
        else:
            form=ArticleForm()
        context ={'form':form,}
        return render(request,'articles/form.html',context)        
           
    ```

### [UPDATE] 게시글 수정 제한

###### 게시글 작성자가 아니면 수정이 불가능하도록 로직을 변경해보자

- detail.html

  - 로그인 한 사용자가 게시글 작성자인 경우에만 수정 버튼이 보이도록 수정한다.

    ```javascript
    {% extends 'base.html' %}
    {% block body %}
    {% load bootstrap4 %}
    
    <div class="container">
        <h2>{{article.title}}</h2>
        <div class="text-align mt-4">
            <p>내용  :  {{article.content}}</p>
            <p>최초 업로드 날짜  :  {{article.created_at}}</p>
            <p>최종 수정 날짜  :  {{article.updated_at}}</p>
        </div>
    
        <a class="ml-auto btn btn-dark"  href="{% url 'articles:index' %}">[INDEX]</a>
    
        <!-- 문제 발생 추가한 코드  -->
        {% if request.user == article.user  %}
        <a class="ml-auto btn btn-dark"  href="{% url 'articles:update' article.pk %}">[EDIT]</a>
        {% endif %}
        <form action="{% url 'articles:delete' article.pk %}" method="POST" style="display : inline;" onclick="return confirm('진짜 삭제할까요...?')">
            {% csrf_token %}
            <input class="ml-auto btn btn-dark"  type="submit" value="DELETE">
        </form>  
        <!-- 여기까지  -->
    
    </div>
    {% endblock  %}
    ```

- 문제발생

  ```python
  {% if request.user == article.user %} 만 추가하면 URL을 통해 접근 가능
  ```

- 문제 해결

  - 아예 view함수에서 막아보기

    - `if request.user == article.user`: 를 추가하여 게시글 작성자인지 확인한다

      - 작성자인 경우, 수정 폼(GET) 또는 수정 로직 수행
      - 작성자가 아닌 경우, 그대로 detail 페이지를 redirect 한다.

      ```python
      @login_required
      def update(request, article_pk):
          article = get_object_or_404(Article, pk=article_pk)
          if request.user == article.user:
      
              if request.method == 'POST':
                  form = ArticleForm(request.POST, instance=article)
      
                  if form.is_valid():
                      article = form.save()
                      return redirect('articles:detail', article_pk)
      
              else :
                  # 빈 값이 아닌 Form의 데이터를 넣어 주는 부분
                  form = ArticleForm(instance=article)
          else:
              return redirect('articles:detail' , article_pk)
          context = {
              'form' : form,
              'article' : article,
          }
          return render(request, 'articles/form.html', context)
      ```

### [DELETE] 게시글 삭제 제한

###### 게시글 작성자가 아니면 삭제가 불가능하도록 로직을 변경하자

- detail.html

  - 로그인한 사용자가 게시글 작성자인 경우에만 삭제 버튼이 보이도록 수정하자

    ```javascript
    {% extends 'base.html' %}
    {% block body %}
    {% load bootstrap4 %}
    
    <div class="container">
        <h2>{{article.title}}</h2>
        <div class="text-align mt-4">
            <p>내용  :  {{article.content}}</p>
            <p>최초 업로드 날짜  :  {{article.created_at}}</p>
            <p>최종 수정 날짜  :  {{article.updated_at}}</p>
        </div>
    
        <a class="ml-auto btn btn-dark"  href="{% url 'articles:index' %}">[INDEX]</a>
    
        <!-- 문제 발생 추가한 코드  -->
        {% if request.user == article.user  %}
        <a class="ml-auto btn btn-dark"  href="{% url 'articles:update' article.pk %}">[EDIT]</a>
        <form action="{% url 'articles:delete' article.pk %}" method="POST" style="display : inline;" onclick="return confirm('진짜 삭제할까요...?')">
            {% csrf_token %}
            <input class="ml-auto btn btn-dark"  type="submit" value="DELETE">
        </form>  
        {% endif %}
        <!-- 여기까지  -->
    
    </div>
    
    {% endblock  %}
    ```

- views.py

  - `if request.user == article.user:`를 추가하여 게시글 작성자인지 확인한다

    - 작성자인경우, 삭제로직을 그대로 수행한다
    - 작성자가 아닌경우, 그대로 detail페이지를 redirect 한다.

    ```python
    @require_POST
    def delete(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        # 지금 사용자가 로그인이 되어있는지 확인
        if request.user.is_authenticated:
            # 로그인한 사용자가 게시글 작성자인지 비교
            if request.user == article.user:
                article.delete()
            # 다를 경우
        	else:
                return redirect('articles:detail', article_pk)
            return redirect('articles:index')   
          
    ```

    

## 2.User-Comment

> ###### comment 가 어떤  User의 것인지를 보이도록 로직을 변경해보자! Comment 는 Article 과 User 정보 2개를 갖는 2중 1:N 관계이다.
>
> - Article 과 User 클래스와 외래키 관계를 맺는다
>
> (ctrl + shift + Q)

#### [CREATE] Comment 작성자 정보 넣기

[articles Application]

- 모델 정의

  - 게시글 작성자에 대한 정보를 넣기 위해 Article 클래스에 User클래스를 외래키로 설정한다

    ```python
    from django.conf import settings
    
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    ```

  - models.py

    ```python
    from django.db import models
    from imagekit.models import ProcessedImageField
    from imageKit.models import Thumbnail
    from django.conf import settings
    
    class Article(model.Model):
        title = models.CharField(max_length=40)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        
        def __str__(self):
            return f'[{self.title}] {self.content}'
    ```

   - 마이그레이션

    ```
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

- 새로운 댓글을 작성할 때 작성자에 대한 정보를 넣는 로직 `comment.user = request.user` 을 추가한다.

- views.py

  - comment가 바로 저장되지 않도록 `comment = form.save(commit=False)`를 설정한다.

  - `request.user`를 이용해 게시글 작성자를 설정한 뒤, `article.save()`를 통해 새로운 게시글을 등록한다.

    ```python
    @require_POST
    def comments_create(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        if request.user.is_authenticated:
            
            comment_form = CommentForm(request.POST)
    
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.article = article
                comment.user = request.user
                comment.save()
    
        return redirect('articles:detail', article_pk)
    ```

[comment user & article 저장 방법 ]

1. 인스턴스 그대로 넣기

   ```python
   @require_POST
   def comments_create(request, article_pk):
       article = get_object_or_404(Article, pk=article_pk)
       if request.user.is_authenticated:
           
           comment_form = CommentForm(request.POST)
   
           if comment_form.is_valid():
               comment = comment_form.save(commit=False)
               comment.article = article
               comment.user = request.user
               comment.save()
   
       return redirect('articles:detail', article.pk)
   ```

   

2. 데이터베이스에 저장되어 있는 형식에 맞춰넣기

   - 인스턴스를 가져오는 `article =get_object_or_404(Article, pk=article_pk) ` 를 작성

   ```python
   @require_POST
   def comments_create(request, article_pk):
       if request.user.is_authenticated:
           
           comment_form = CommentForm(request.POST)
   
           if comment_form.is_valid():
               comment = comment_form.save(commit=False)
               comment.article_id = article_pk
               comment.user = request.user
               comment.save()
   
       return redirect('articles:detail', article_pk)
   ```

##  [ DELETE ] Comment 삭제 제한

> 본인이 작성한 comment만 삭제할 수 있도록 로직을 변경해보자!

- views.py

  - 로그인한 사용자와 댓글 작성자가 같을 경우 삭제를 수행한다.

    - `request.user == comment.user:`

      ```
      @require_POST
      def comments_delete(request, article_pk, comment_pk):
          # 1. 로그인 여부 확인
          if request.user.is_authenticated:
              article = get_object_or_404(Article, pk=article_pk)        
              comment = get_object_or_404(Comment, pk=comment_pk)
      
              # 2. 로그인한 사용자와 댓글 작성자가 같을 경우 삭제를 수행한다.
              if request.user == comment.user:
                  comment.delete()    
          return redirect('articles:detail', article.pk)
      ```

- detail.html

  - `{% if coment.user == request.user %}`를 추가하여 comment 작성자인 경우에만 삭제 버튼을 보이도록 한다.

    ```javascript
    {% extends 'base.html' %}
    {% block body %}
    {% load bootstrap4 %}
    
    <hr>
    
    <p><b>댓글 목록({{comments|length}}개)</b></p>
    <hr>
    {% for coment in comments  %}
    
      <p>[{{forloop.revcounter}} 번 댓글]  {{coment.content}}</p>
      
      {% if coment.user == request.user %}
    
      <form action="{% url 'articles:comments_delete' article.pk coment.pk %}"  method="POST" style="display:inline; max-width:500px;">
        {% csrf_token %}
        {% buttons submit='삭제' layout="inline" %}
        {% endbuttons %}
      </form>
      {% endif %}
    {% endfor %}
    
    {% endblock %}
    ```

