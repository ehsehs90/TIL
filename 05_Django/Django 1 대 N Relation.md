## 1 : N Relation

- Foreigh Key(외래키)

  - 참조 키의 값으로는 부모 테이블에 존재하는 키의 값 만을 넣을 수 있다

    참조 무결성을 위해 참조 키를 사용하여 부모 테이블의 유일한 값을 참조(-> 부모 테이블의 기본 키를 참조)

  - 참조 키의 값이 부모 테이블의 기본키일 필요는 없지만 유일해야 한다.

## 1. Modeling(`models.py`)

- possible values for `on_delete`
  - `cascade` : 부모 객체가 삭제되면 참조하는 객체도 삭제한다
  - `PROTECT` : 참조가 되어 있는 경우 오류 발생
  - `SET_NULL` : 부모 객체가 삭제되면 모든 값을 NULL로 치환(NOT NULL 조건이면 불가능)
  - `SET_DEFAULT` : 모든 값이 DEFAULT 값으로 치환( 해당 값이 DEFAULT 값이 지정 되어있어야 함)
  - `SET()` 특정 함수 호출
  - `DO_NOTHING` : 아무것도 하지 않는다. 다만 DB필드에 대한 SQL ON DELETE 제한 조건이 설정되어 있어야 한다.

## 2. ORM 실습

- 댓글 생성 및 조회

- 먼저 Comment Model을 정의한다

  - `models.py`

  ```python
  
  class Comment(models.Model):
      # related_name: 부모 테이블에서 역으로 참조할 때 기본적으로 모델이름_set형식으로 불러온다
      # related_name 이라는 값을 설정해서 _set명령어를 임의로 변경할 수 있다.
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      content = models.CharField(max_length=250)
      created_at =models.DateTimeField(auto_now_add=True)
      updated_at = models.DateField(auto_now=True)
      
      # Model Level에서 Metadata 설정
      class Meta:
          ordering = ['-pk',]
  
      def __str(self):
          return self.content
  ```

- comment 모델 설정했으면 `makemigrations` 와 `migrate` 해서 DB에 테이블을 생성한다.

- comment 은 article 모델의 ForeignKey

  - migrate 중 

  - 만약 `Default 값` 설정 안내가 나오면?
    
    - 만약 데이터가 있었다면 어떤 값으로 할래? 1
    
    - migrate 후 sqlite3 확인
    
      
    
  -  Admin에서 관리할 수 있도록 `class` 등록 하기!

  ```python
  from .models import Article, Comment
  
  class CommentAdmin(admin.ModelAdmin):
  
  
      list_display = ('pk','content','created_at','updated_at',)
  
  
  admin.site.register(Comment, CommentAdmin)
  ```

## 2. ORM 실습

###### shell_plus 를 이용해 댓글을 생성하고 조회하자

#### 2.1 댓글 생성

- 하드코딩으로 comment 에 데이터 넣기
  - shell_plus 실행

```shell
$python manage.py shell_plus

```

- shell_plus로 Comment 생성

```bash
comment = Comment()
article = Article.objects.get(pk=3)  #3번 게시글에 코멘트 달게요
comment.content= " 집 가기 15 분전"
comment.article = article
comment.save()   #db에 저장하기
Comment,objects.all()
exit()
```

- 해당 Comment 의 article의 title 가져오기

```shell
comment.article.title
```



![1572857620504](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572857620504.png)

- 데이터가 성공적으로 들어온 것을 확인할 수 있어요

#### 2.2 댓글 조회

- **1:N Relation 활용하기**

  - Article(1)  : Comment(N) ->`comment_set`

    - **article.comment** 형태로는 가져올 수 없다. 

    - 게시글에 몇 개의 댓글이 있는지 Django ORM 측에서 보장할 수가 없다.

    - 하나의 Article에 달려있는 Comments 확인하기
  
      `article.comment_set.all()`
  
      
  
  - Comment(N): Article(1)-> `article`
  
    - 댓글의 경우, `comment.article `형태로 접근할 수 있다
    
    - 어떤 댓글이든 본인이 참조하고 있는 게시글이 반드시 있다.
    
      따라서 이런 식으로 접근할 수 있다.
      
      `comment.article`



## [related_name]

- 부모 테이블에서 역으로 참조한다
- Article에서 Comments를 가져올 때, 기본적으로 [모델이름]_set 형식으로 불러온다
- related_name 값을 설정해서 _set 명령어를 임의로 변경할 수 있다
- models.py 작성 예

```python
from django.db import models

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, 
    related_name='comments')
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Model Level 에서 MetaData 설정
    class Meta:
        ordering = ['-pk',]

    # 객체 표시 형식 수정
    def __str__(self):
        return self.content
```



