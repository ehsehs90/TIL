# 1. Hashtag

## 1. Hashtag

### 1.1 Model

```pyyhotn

```

- `unique=True`
  - True인 경우, 필드는 테이블을 전체에서 고유한 값이여야 한다
  - 유효성 검사 단계에서 실행되며, 중복값이 있는 모델을 저장하려고하면 `.save()` 메서드로 인해서 에러가 발생한다

````python
title : 출근
content str 타입

1. 사용자가 업로드한 content
"오늘 수능날....난 출근...#행복 하다...ㅋ...옛날생각나ㅔ..또..#감성 #추억 #뿌듯 #수능왕 .split(' ')

2. .split() 메소드로 리스트 형식으로 변환
['오늘' '수능날' '난' '출근' '#행복' '하다' '옛날생각나네'....'#감성','#추억']

3.리스트 반복문 돌리기 : 앞자리가 '#'으로 시작하는 단어를 해시태그 테이블에 등록
    = 같은 해시태그가 오면 unique= True 옵션으로 인해 에러발생. 이를 방지하기 위해 get_or_create() 사용

4. 동시에 해당 게시글 해시태그 목록에 추가해줌
->article.hashtags.add(word)

````

- `get_or_create()`
  - word와 같은 해시태그를 찾고 있으면 기존 객체 반환, 없으면 새로운 객체 생성
  - `hashtag, created = Hashtag.objects.get_or_create(content=word)`
    - 새로운 객체 생성되면 created = True
    - 기존 객체 반환 되면 created = False

### 1.2 CREATE



### 1.3 UPDATE

### 1.4 UPDATE





### 1.5 READ



# 2. Social Login

> 인증, 계정 등록 등을 다루는 여러가지 방법이 존재하는데, 우리는 `**django-allauth`라는 라이브러리를 사용해서 손쉽게 Social Login을 구현해보자**
>
> 대부분의 소셜 로그인을 지원하고 회원가입 시킬 수 있다.



## 2.1 사전준비

- allauth 설치

- ```shell
  $ pip install django-allauth
  ```

  

- `settings.py`

```python

AUTHENTICATION_BACKENDS = (    
    'django.contrib.auth.backends.ModelBackend',
)

INSTALLED_APPS = [
    'articles',
    'accounts',
    'bootstrap4',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
    'django.contrib.sites',
   ...
]

SITE_ID = 1
```

- `config` > `urls.py`

```python
urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
]

```

- migrate

```shell
$ python manage.py migrate
```



## 2.2 KaKao Developers `OAuth`등록

### 2.2.1 앱만들기

- KakaoDevelopers_
  - <https://developers.kakao.com/>
- 

### 2.2.2 플랫폼추가

### 2.2.3 사용자 관리

### 2.2.4 소셜 어플리케이션 추가



