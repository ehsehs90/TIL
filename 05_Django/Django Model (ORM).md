## 19.10.30(수) : Django Model (ORM)

- 장고MTV 패턴
  - Model
    - 특정한 데이터의 구조(모양)에 대한 정보를 가지고 있다 (->데이터의 모양을 정의하는 곳)
    - 하나의 모델 클래스는 실제 DB에는 하나의 테이블로 매핑된다
    - 컬럼에 대한 정보, 해당 데이터에 대한 정보를 정의하는 곳
  - Template
  - View

- Model 로직
  -   데이터베이스 컬럼(열) 과 어떠한 타입으로 정의할 것인지에 대한 정보를 `django.db.models`라는 곳에서 상속받아서 정의한다
  - 모든 필드들은 NOT NULL 조건이 붙는다
  - 각각의 클래스 변수는 데이터베이스 필드를 나타낸다

### 1.1Migration

 - `makemigrations`
    - 실제 데이터베이스 테이블을 만들기 전에 설계도를 그려보는 작업	
      	- Python 코드로 데이터베이스 설계도를 작성한다
   - migrations폴더에서 확인할 수 있다 (`0001_initial.py`,...)
- `sqlmigrate`
  - 데이터베이스에 실제로 반영하기 전에 **설계한 Python 코드가 SQL문으로 바뀐 모습을 확인**해볼수 있다.
- `showmigrations`
  - migration 설계도를 작성했는데, 이 **설계도가 실제 DB 에 반영되었는지 여부**를 확인
- `migrate`
  - `makemigrations`로 만든 설**계도를 실제 데이터베이스(sqlite3)에 반영**한다
  - 모델의변경사항과 데이터베이스 스키마를 동기화한다

## 2. ORM_CRUD

- ORM을 리턴되는 형식

  - QuerySet : 다수의 객체가 담김(파이썬 리스트 다루는 것과 비슷)
  - Query : 단일객체

- `모델명.Objects.명령`

  - `objects` : 모델 클래스 정보를 토대로 실제 데이터베이스에 쿼리(SQL)를 날려서 데이터베이스와 의사소통 하는 통역사(매니저) 역할

- **우리가 ORM 을 사용하는 이유?**

  - SQL문에 종속되지 않고 데이터를 객체 형태로 다루기 위해(프로그래밍언어만 알아도 DB를 다룰 수 있음)
    
### 2.1  Create

  ```sqlite
  #첫번째 방법
  article = Article()
  article.title =''
  article.content =''
  article.save()
  
  
  #두번째 방법 : 함수에서 키워드 인자 넘겨주는 방식
  article = Article (title='',content='')
  article.save()
  
  
  #세번째 방법  : 쿼리셋 객체 생성과 DB 저장을 한번에 해결
  Article.objects.create(title='sasa',content='sasa')
  ```

  ```sqlite
  #유효성 검증
  article.full_clean()
  ```

  

### 2.2 Read

```sqlite
# (파이썬 리스트와 비슷한) QuerySet 리턴
articles1 = Article.ojbects.all()
articles2 =Article.objects.filter()



#필터기능
Article.objects.filter(title='first')
Article.objects.filter(pk=100)


#정렬기능 

Article.objects.all()
articles = Article.objects.order_by('-pk')   #내림차순
articles


Article.objects.all()
articles = Article.objects.order_by('pk')    #오름차순
articles


#쿼리셋 리턴을 list 처럼 사용할 수 있다
articles = Art
```



### 2.3 Update

```sqlite

```

### 2.4 Delete

```bash

```





### 2.5 Django_extensions

기본 Django Shell은 직접 모델을 import 해주어야 하는 불편함이 있었지만

`shell_plus` 는 필요한 모델을 자동으로 import 해주기 때문에 편리하다.

- 설치하기

``` bash
$ pip install  django-extensions
```

- 앱 등록하기

```python
#settings.py
INSTALLED_APPS =[
    ...
    'django_extensions',
    ...
]
```

- shell 실행하기

```bash
$ python manage.py shell_plus
```

```python
# Shell Plus Model Imports
from articles.models import Article
...
Ipython 7.9.0 -- An enhanced Interactive Python. Type '?' for help.
```

