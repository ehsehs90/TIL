## Image Resizing

### 1. 라이브러리 설치

- python & Django 이미지 관련 라이브러리

  ```shell
  #설치 순서 주의! (의존성 있음)
  $ pip install Pillow
  $ pip install pilkit
  $ pip install django-imagekit
  ```

  - `pillow`: PIL (Python Image Library) 프로젝트에서 fork 되어서 나온 라이브러리. Python3를 지원하지 않기 때문에 Pillow를 많이 씀

  - `pilkit`: Pillow를 쉽게 쓸 수 있도록 도와주는 라이브러리

    다양한 Processors 지원

    - Thumbnail
    - Resize
    - Crop ....

  - `django-imagekit`: 이미지 썸네일 Helper

### 2. APP등록

- INSTALLED_APPS 등록

```python
#settings.py
INSTALLED_APPS = [
    ....
    'imagekit',
    ....
]
```

- 라이브러리 설치 확인

  ```shell
  $ pip list
  ```



### 3. Modeling

- 기존의 models.py

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

 - models.py 에 밑의 코드를 추가한다

```python
#models.py
from imagekit.models import ProcessedImageField
from imagekit.processprs import Thumbnail

  image = ProcessedImageField(
        processors=[Thumbnail(200, 300)],   # 처리할 작업
        format='JPEG',                       # 이미지 포멧
        options={'quality':90},              # 각종 추가 옵션
        upload_to='articles/images/',        # 저장위치
        #실제 경로 -> MEDIA_ROOT/articles/images
    )
```

- models.py변경

  ```python
  from django.db import models
  from imagekit.models import ProcessedImageField
  from imagekit.processors import Thumbnail
  
  class Article(models.Model):
      title = models.CharField(max_length=40)
      content = models.TextField()
  
      image = ProcessedImageField(
          processors=[Thumbnail(200,300)],    # 처리할 작업
          format='JPEG',              # 이미지 포맷
          options={                   # 각종 추가 옵션
              'quality' : 90
          },
          upload_to = 'articles/image' # 저장 위치
          # 실제 경로 : MEDIA_ROOT/articles/image
      )
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      # 객체 표시 형식 수정
      def __str__(self):
          return f'[{self.pk}] : {self.title} '
  ```

### 4.Migration

```shell
$ python manage.py makemigration
$ python manage.py migrate
```

- ProcessedImageField의 인자로 들어가는 옵션들은 수정을 하더라도 다시 migration 하지 않아도 된다.