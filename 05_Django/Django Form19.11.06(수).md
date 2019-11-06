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

  - ```
    pilkit
    ```

     

    : Pillow를 쉽게 쓸 수 있도록 도와주는 라이브러리. 다양한 Processors 지원

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

  ```
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

  ```
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

  - `ProcessedImageField`의 인자로 들어가는 옵션들은 수정을 하더라도 다시 migration 하지 않아도 바로바로 적용이 된다.

## 1. 사전 준비

> Django Form을 적용하기 전, 이때까지 우리가 학습했던 HTML Form으로 앱을 구현해보자.

- **프로젝트 생성**

  ```
  $ mkdir 04_django_form
  $ cd 04_django_form
  ```

  ```
  $ django-admin startproject config .
  ```

- **앱 생성**

  ```
  $ python manage.py startapp articles
  ```

- **Article Model**

  ```
  # models.py
  ```

- **URL 설정**

  ```
  # config/urls.py
  ```

  ```
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