## 19.11.07 Django Form 마무리

### 1. URL Resolver

- CREATE 로직과 UPDATE 로직이 같은 form.html을 공유하고 있는데, 둘 다 <h1>CREATE</h1> 라는 헤더가 출력되고 있다

  - `URL Resolver`을 적용해 이를 해결해보자!

- URL Resolver 는 사용자가 요청한 URL과 장고 내부로 들어오는 URL 사이에서 번역 역할을 해준다.

  - `request.resolver_match.url_name == 'create'` : request로 들어오는 url 의 이름이 'create'인지 확인
  
    - `urls.py`에 등록된 url의 이름을 작성한다
    
      ```javascript
      {% block body %}
      {% if request.resolver_match.url_name == 'create' %}
      <h1 class ='text-center'>CREATE</h1>
      {% else %}
      <h1 class = "text-center">UPDATE</h1>
      {% endif %}
      
      {% if request.resolver_match.url_name == 'create' %}
      <a href={% url 'articles:index ' %}>[INDEX]</a>
      {% else %}
      < a href = {% url 'articles:detail' article.pk %}[DETAIL]</a>
    {% endif %}
      {% endblock %}
      ```
    ```
    
    ```
    
  - form.html
  
  ```html
  {% extends 'base.html' %}
  {% load bootstrap4 %}
  {% block body %}
  
  {% if request.resolver_match.url_name == 'create' %}
  <h1 class="text-center">CREATE</h1>
  {% else %}
  <h1 class="text-center">UPDATE</h1>
  {% endif %}
  
  <hr>
  <div class="container mx-auto">
    <form action="" method="POST" class="mx-auto" style="max-width:500px;">
      {% csrf_token %}
      <div class="text-center">
        {% bootstrap_form form layout="inline" %}
        {% buttons submit='제출' reset='초기화' %}
        {% endbuttons %}
        {% comment %} <input type="submit" value="작성"> <br> {% endcomment %}
      </div>
    </form>
  </div>
  
  {% if request.resolver_match.url_name == 'create' %}
  <a href="{% url 'articles:index' %}">[BACK : INDEX]</a>
  {% else %}
  <a href="{% url 'articles:detail' article.pk %}">[BACK : DETAIL]</a>
  {% endif %}
  
  {% endblock  %}
  ```
  
  

### 2. Django BootStrap

- django-bootstrap4 설치

```shell
$ pip install django-bootstrap4
```

- 출생신고 app등록

  - settings.py

  ```python
  INSTALLED_APPS = [
     	...
      'bootstrap4',
      ...    
  ]
  ```

- `bootstrap4` 을 load한다 
  
  - bootstrap 을 적용할 템플릿에 반드시 `{% load bootstrap4 %}` 를 적용해야한다.
  - `<https://django-bootstrap4.readthedocs.io/en/latest/quickstart.html>` 을 참고

```html
<!-- base.html --> 상단에
{% load bootstrap4 %}

<title>
{% bootstrap_css %}
</title>

<body>
{% bootstrap_javascript jquery='full' %} 
</body>
```

### 3. Comment - ModelForm

#### 1. Comment 모델 생성

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at  =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    # Model Level에서 Metadata 설정
    class Meta:
        ordering = ['-pk',]

    def __str(self):
        return self.content
```

- makemigrations 와 migrate

  ```shell
  $ python manage.py makemigrations
  $ python manage.py migrate
  $ python manage.py showmigrations(?)
  ```

#### 2. Comment ModelForm 생성

```python
class CommentForm(forms.ModelForm):   
    content = forms.CharField(
        label='내용 입력 하세요',
        widget=forms.Textarea(
            attrs={
                'class':'content',
                'placeholder':'댓글입력해',
                'rows':5,
                'cols':30,
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content',)      
        #원하는것만 필드에 나타나게 할 수 있다 
        #('title','content',)
```

- `view.py` 
  - detail함수에 CommentForm() 인스턴스 넣어주고 context에 담아 보낼 수 있도록 한다
  - comments_create 함수 생성

```python
from .forms import ArticleForm, CommentForm


def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    # 첫번째인자 class 두번째인자 pk
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    context = {'article': article,
                'comment_form': comment_form,
                 }
    return render(request,'articles/detail.html',context)

def comments_create(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    if request.method =='POST'
        pass

```

#### 3. `admin.py` 등록   


   ```python
   from django.contrib import admin
   from .models import Article, Comment
   # Register your models here.
   
   class CommentAdmin(admin.ModelAdmin):
   
       list_display = ('pk','content','created_at','updated_at',)
   
   # admin.site.register(Article, ArticlesConfig)
   admin.site.register(Comment, CommentAdmin)
   
   ```

   - 만약 admin계정이 없다면?

     - admin 계정 생성 !

       ```shell
       $ pyhton manage.py createsuperuser
       ```

       

 - `url.py`

   ```
   urlpatterns=[
   path(),
   ]
   ```

   




### 4. View Decorators

#### Django가 제공하는 decorator 활용하기



#### 4.1  require_POST

- view함수가 POST 메서드 요청만 승인하도록 하는 데코레이터

- 일치하지 않는 요청이면 405 Method Not Allowed 에러 발생시킴

- require_POST import 하기

  ```python
  from django.views.decorators.http import require_POST
  ```



#### 4.2 require_POST 사용하기

- `views.py`
  - @require_POST 는 **POST요청만 수행하는 뷰 함수**에 쓴다
  - 이걸 사용하면 POST여부를 확인하는 코드는 필요없어진다 

```python
from django.views.decorators.http import require_POST


@require_POST
def delete(request, article_pk):    
    article = Article.objects.get(pk=article_pk)    
        article.delete()    
        return redirect('/articles/index/')
```

- 이 외에도 POST 로직만 사용하는 뷰 함수에 사용할 수있다

  ```python
  #수정 전
  def comments_create(request, article_pk):
      article = get_object_or_404(Article, pk = article_pk)
      if request.method =='POST':
          comment_form = CommentForm(request.POST)
          if comment_form.is_valid():
              comment = comment_form.save(commit=False)
              comment.article =article
              comment.save()
              return redirect('articles:detail', article.pk)
      return redirect('articles:detail', article.pk)
  
  
  #수정 후
  @require_POST
  def comments_create(request, article_pk):
      article = get_object_or_404(Article, pk = article_pk) 
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.article =article
          comment.save()
          return redirect('articles:detail', article.pk)
  ```

  ```python
  #수정 전
  def comments_delete(request, article_pk, comment_pk):
      article = get_object_or_404(Article, pk = article_pk)
      if request.method =='POST':
          comment = article.comment_set.get(pk=comment_pk)
          comment.delete()
          return redirect('articles:detail', article_pk)
      else:
          return redirect('articles:detail', article_pk)
      
  #수정 후
  @require_POST
  def comments_delete(request, article_pk, comment_pk):   
      article = get_object_or_404(Article, pk = article_pk) 
      comment = article.comment_set.get(pk=comment_pk)
      comment.delete()
      return redirect('articles:detail', article_pk)
  ```

  









```python
# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=30,
#         #HTML Tag 와 동일
#         label = '제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class':'title',
#                 'placeholder':'제목을 입력하세요',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class' : 'content',
#                 'placeholder' : '내용을 입력해',
#                 'rows' : 5,
#                 'cols' :30,
#             }
#         )
#     )
# 메타데이터 사용하려면 모델  import필요

# ModelForm
# 1. ModelForm 클래스를 상속받아 사용한다
# 2. 메타데이터로 Model정보를 건네주면, ModelForm이 자동으로 field 에 맞춰 input 을 생성해준다.
```

