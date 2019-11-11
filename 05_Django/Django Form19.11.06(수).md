# 19.11.06(수) Django Form

## 0. Image Resizing

- Python & Django 이미지 관련 라이브러리

  ```
  # 설치 순서 주의! (의존성 있음)
  
  $ pip install Pillow
  $ pip install pilkit
  $ pip install django-imagekit
  ```

  - `Pillow` : PIL(Python Image Library) 프로젝트에서 fork 되어서 나온 라이브러리. PIL은 Python3를 지원하지 않기 때문에 Pillow를 많이 씀

  - `pilkit`: Pillow를 쉽게 쓸 수 있도록 도와주는 라이브러리. 다양한 Processors 지원
    - Thumbnail
    - Resize
- Crop ...
  
- `django-imagekit` : 이미지 썸네일 Helper
  
- **INSTALLED_APPS 등록**

  ```
  # settings.py
  INSTALLED_APPS = [
      ...
      'imagekit',
      ...
  ]
  ```

- 모델 수정

  ```python
  class Article(models.Model):
      ...
      # image = models.ImageField(blank=True)
      image = ProcessedImageField(
          processors=[Thumbnail(200, 300)],   # 처리할 작업
          format='JPEG',                  # 이미지 포맷
          options={'quality': 90},        # 각종 추가 옵션
          upload_to='articles/images',    # 저장 위치
          # 실제 경로 -> MEDIA_ROOT/articles/images
      )
      ...
  ```

- Migration

  ```shell
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

  - `ProcessedImageField`의 인자로 들어가는 옵션들은 수정을 하더라도 다시 migration 하지 않아도 바로바로 적용이 된다.

## 1. 사전 준비

> Django Form을 적용하기 전, 이때까지 우리가 학습했던 HTML Form으로 앱을 구현해보자.

- **프로젝트 생성**

  ```shell
  $ mkdir 04_django_form
  $ cd 04_django_form
  ```

  ```
  $ django-admin startproject config .
  ```

- **앱 생성**

  ```shell
  $ python manage.py startapp articles
  ```

- **Article Model**

  ```python
  # models.py
  
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

- **URL 설정**

  ```python
  # config/urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  
  
  urlpatterns = [   
      path('articles/', include('articles.urls')),
      path('admin/', admin.site.urls),
  ]
  ```

  ```python
  # articles/urls.py
  
  
  ```

- **base.html 생성** (부트스트랩 적용X)

- **Index 페이지** (-> 모든 게시글 보여주기)

  ```
  # views.py
  def index(request):
      pass
  ```

  ```
  <!-- index.html -->
  ```

- **Create 페이지**

  ```
  # views.py
  def create(request):
      pass
  ```

  ```
  <!-- create.html -->
  ```

- **Detail 페이지**

  ```
  # views.py
  def detail(request, article_pk):
      pass
  ```

  ```
  <!-- detail.html -->
  ```



## 2. Django Form

###### Django에서 제공하는 Form 클래스를 이용해서 편리하게 폼 정보를 관리하고 유효성 검증을 진행하고, 비유효 field 에 대한 에러 메세지를 결정한다

###### 즉, HTML으로 Form 입력을 관리하던 것을 Django에서 제공하는 Form 클래스로 바꿔보는 작업을 해보자.



#### 1.1 Form 장점

- Form의 장점 ( -> 자동화 )

  - `blank=True` 와 같은 옵션을 따로 지정해주지 않으면, HTML 태그에 required  옵션 자동으로  붙여준다
  - 기존에 max_length와 같은 조건을 어길 경우 에러 페이지를 출력했는데, Django Form 을 써서 에러메세지를 출력해 준다

  

  

- `Article Form Class`정의

  - forms.py

    ```python
    from django import forms
    
    class ArticleForm(forms.Form):
        title = forms.CharField(max_length=40)
        content = forms.CharField()
    ```

- `views.py` 로직 변경

  - 바인딩 과정 
    - Form 인스턴스를 생성하고, 전달받은 데이터를 채운다
    - 인스턴스에 데이터를 채워서, 유효성 검증을 진행한다
      - **유효성 검증**
        - 유효성 검증이 끝난 form 은 dict형태로 뽑혀나온다
        - `cleaned_data`를 통해 dict안의 데이터를 검증한다
      - Form 으로 전달받는 형태 2가지
        - a. GET요청 : 비어있는 Form 전달
        - b. 유효성 검증 실패 : 에러 메세지도 담겨서 Form 전달
  - views.py

  ```python
  def create(request):
      # POST 요청 -> 데이터를 받아서 DB에 저장
      if request.method == 'POST':
  
          form = ArticleForm(request.POST)
          embed()
          if form.is_valid():
              # cleaned_data를 통해 딕셔너리 안 데이터를 검증한다.
              title = form.cleaned_data.get('title')
              content = form.cleaned_data.get('content')
              article = Article.objects.create(title=title, content=content)
          return redirect('articles:detail', article.pk)
      else:
          form = ArticleForm()
  
  
      context = {'form': form}
      return render(request, 'articles/create.html', context)
  ```

  - create.html

  ```html
  {% block body %}
  
  <form action="" method="POST">
    {% csrf_token %}
    {% comment %} 
    {{form.as_p}}: 각각의 input 태그를 p 태그로 감싼다.
    {{form.as_table}}: 각각의 input 태그를 테이블 태그로 감싼다.
    {% endcomment %}
    {{form.as_p}}
    <input type="submit" value="작성"> <br>
  </form>
  
  {% endblock  %}
  ```

  
  
  

### [IPython]

###### 실행 도중 원하는 위치에 shell을 실행할 수 있다

###### Ipython을 이용해 Django Form유효성 검증 전/후 를 확인한다.

- IPython 의 embed를 import 한다
  
    ```python
    from IPython import embed
  ```
  
  - Django Form 유효성 검증 전/후 확인
  
  ```shell
  In [1]: form
Out[1]: <ArticleForm bound=True, valid=Unknown, fields=(title;content)>
  
  In [2]: request.POST
  Out[2]: <QueryDict: {'csrfmiddlewaretoken': ['U1J7RiHKAesPTziSAwvboujPOKqSrouK01pu2DMCXZ6EgiSDLwjJehiLLhOMzHsl'], 'title': ['dfsdfsd'], 'content': ['sdfsdf']}>
  
  In [3]: type(form)
  Out[3]: articles.forms.ArticleForm
  
  In [4]: form.is_valid()
  Out[4]: True
  
  In [5]: form
  Out[5]: <ArticleForm bound=True, valid=True, fields=(title;content)>
  
  In [6]: form.cleaned_data
  Out[6]: {'title': 'dfsdfsd', 'content': 'sdfsdf'}
  
  In [7]: type(form.cleaned_data)
  Out[7]: dict
  
  In [8]: form.cleaned_data.get('title')
  Out[8]: 'dfsdfsd'
  
  In [9]: exit()
  ```
  

  
### Django Form Customizing

  ###### forms.py를 Customizing하여 다양한 형태의 Django Form을 구성할 수 있다.

  - [ 1 ] forms.py

    ```python
    from django import forms
    
    class ArticleForm(forms.Form):
        title = forms.CharField(
            max_length=40, 
            # HTML TAG 와 동일
            label='제목',
        )
        content = forms.CharField()
    ```

    - ![1573460942793](C:\Users\student\Desktop\TIL\05_Django\assets\1573460942793.png)

- [2]forms.py

  ```python
  from django import forms
  
  class ArticleForm(forms.Form):
      title = forms.CharField(
      	max_length=40,
      	label='제목'
      	widget=forms.TextInput(
          	attrs={
                  'class' : 'title',
                  'placeholder': "제목을 입력해주세요",
              }
          )
      )
      content = forms.CharField()
  ```

  - ![1573461065832](C:\Users\student\Desktop\TIL\05_Django\assets\1573461065832.png)

- [ 3 ] forms.py

  ```python
  from django import forms
  
  class ArticleForm(forms.Form):
      title = forms.CharField(
          max_length=40, 
          # HTML TAG 와 동일
          label='제목',
          widget=forms.TextInput(
              attrs={
                  'class' : 'title',
                  'placeholder' : '제목을 입력해주세요~',
              }
          )
      )
      content = forms.CharField(
          label='내용',
          widget=forms.Textarea(
              attrs={
                  'class' : 'content',
                  'placeholder' : '내용을 입력해주세욥',
                  'rows' : 5,
                  'cols' : 30,
              }
          )
      )
  ```

  ​	-  ![1573461102759](C:\Users\student\Desktop\TIL\05_Django\assets\1573461102759.png)

  #### get_object_or_404 ( NOT FOUND)

- 500 에러는 내부 서버 오류로, '서버에 오류가 발생하여 요청을 처리할 수 없다'는 의미이다.  예를 들어 articles/410989 와같이 존재하지 않는 상세정보 페이지를 요청하면 500 에러가 발생한다

- 하지만 이 경우엔 사용자의 요청이 잘못된 경우이기 때문에 '서버에 존재하지 않는 페이지에 대한  요청'이라는 의미를 가진 404 에러를 돌려주어야 한다.

  - 500 에러를 돌려주면 " 깃 폭파했네요?" 라는 말이 나올거고,
  
    (서버의 잘못)
  
  -  404 에러를 돌려주면 "아, 선생님이 주소를 잘못 줬거나 내가 잘못 쳤구나"... 라는 말이 나올 것( 사용자의 부주의 )
  
  
  
- get_object_or_404 를 불러온다

```python
# views.py
from django.shortcuts import render, redirect, get_object_or_404

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context= {'article': article}
    return render(request, 'articles/detail.html', context)
```

### DELETE

- `views.py`

```python
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)
```

- `detail.html`

  - form 태그를 사용해 DELETE 버튼 생성

  ```html
  {% block body %}
  
  <p>제목  :  {{article.title}}</p>
  <p>내용  :  {{article.content}}</p>
  <p>최초 업로드 날짜  :  {{article.created_at}}</p>
  <p>최종 수정 날짜  :  {{article.updated_at}}</p>
  
  <a href="{% url 'articles:index' %}">[INDEX]</a>
  <a href="{% url 'articles:update' article.pk %}">[EDIT]</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit" value="[DELETE]"> <br>
  </form>
  
  
  {% endblock  %}
  ```

  

### UPDATE

- `views.py`

  - 2가지 Form  형식

    a. GET요청 -> 초기값을 Form 에 넣어서 사용자에게 던져줌

    b. POST -> is_valid가 False 가 리턴되었을때, 오류메세지를 포함해서 사용자에게 던져줌

```python
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        # 두번째 인자로 article 인스턴스를 넘겨준다. (instance 키워드 인자!)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # article 인스턴스를 넘겨주어 폼 초기값을 채운다.
        form = ArticleForm(instance=article)
    context = {'form': form}
    return render(request, 'articles/form.html', context)
```



## 3. Django ModelForm

- 개념
  - Django의 큰 특징 중 하나
  -  Model 클래스 정의와 비슷하게 Form 클래스를 선언할 수 있다
- 역할
  1. HTML 입력 폼 생성 : `as_p()` ,` as_table()`
  2. 유효성 검증 : `is_valid()`
  3. 검증 통과한 값 딕셔너리로 제공 : `cleaned_data`

######    DJango Model Form

1. Model Form 클래스를 상속받아 사용한다
2. 메타 데이터로 Model정보를 건네주면, ModelForm이 자동으로 field에 맞춰 input을 생성해준다
   - 메타데이터
     - 데이터의 데이터
       - 사진 한장 -> 촬영장비, 이름 환경 등... 사진에 대한 데이터



- `Form` vs `ModelForm`

  ```python
  #forms.py
  class ArticleForm(forms.Form):
  	title = forms.CharField
      content = forms.CharField
  
  #Django ModelForm
  #Django 가 건네받은 모델을 기준으로 폼 양식에 필요한 대부분을 전부 만들어준다.
  
  from .models import Article
  
      class ArticleForm(forms.ModelForm):
          class Meta:
              model=Article
              fields='__all__'
  ```
  
- 전체코드

```python
# ModelForm
# 1. ModelForm 클래스를 상속받아 사용한다.
# 2. 메타데이터로 Model 정보를 건네주면, ModelForm이 자동으로 field에 맞춰 input을 생성해준다.
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'title',
                'placeholder': '제목 입력해라...'
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'content',
                'placeholder': '내용 입력해라...',
                'rows': 5,
                'cols': 30
            }
        )
    )

    # 메타데이터: 데이터의 데이터
    # ex) 사진 한장 (-> 촬영장비이름, 촬영환경 등)
    class Meta:
        model = Article
        fields = ('title', 'content',)
        # fields = '__all__'
```

