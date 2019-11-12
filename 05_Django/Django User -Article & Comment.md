# User -Article & Comment

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

#### 1.1 Article 모델 클래스 수정

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
     class Article(models.Model):
         title = models.CharField(max_length=40)
         content = models.TextField()
         created_at = models.DateTimeField(auto_now_add=True)
         updated_at = models.DateTimeField(auto_now=True)
         user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
         
         def __str__(self):
             return f'[{self.pk}] {self.title}'
     ```

   - 수정 후 makemigrations migrate

     ```shell
     $ python manage.py makemigrations
     $ python manage.py migrate
     ```

     

      - 

#### 1.2 

#### 1.3





## 2.User-Comment

#### 2.1 Comment 모델 클래스 수정

- ```python
  
  ```

- 

#### 2.2

#### 2.3





