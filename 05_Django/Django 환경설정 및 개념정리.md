### 1.1 가상환경 설정

- **Why 가상환경?**
  - 글로벌 환경에서 개발을 진행하다보면, 실제 해당 프로젝트에서는 필요없는 라이브러리들이 설치되어있을 수 있다. 내 컴퓨터에서는 정상적으로 돌아가지만, 다른컴퓨터에서 실행했을 때 그 사람이 가지고 잇는 라이브러리와 만나게 되면 돌아가지 않을 수 있다
  - 파이썬 버전도 마찬가지로 특정한 버전에서만 실행되는 경우가 있다
  - 따라서, 지금 이 프로젝트나 필요한 패키지들이 설치된 가상환경에 진입해서 개발을 진행한다
- **Visual Studio Code에서 기본 가상환경 설정하기**
  - `Shift +ctrl + P` 혹은 좌측 하단의 파이썬 버전 클릭해서 우리가 생성한 venv 를 기본값으로 선택해준다
  - 그 다음 VSCode 내장 터미널을 새로 실행하면, 자동으로 `source ~activate` 까지의 명령어가 실행되면서 가상환경으로 진입한다
- **VSCode 환경설정이 꼬이는 경우, 그냥 터미널에서 가상환경 진입명령어를 실행하자!**
  - `source venv/Scripts/activate`(for Windows)
- **앞으로 개발을 진행할때는 반드시 가상환경 진입여부를 확인해야한다**
  - 터미널 명령어 앞에 `(venv)` 혹은 pip list 입력했을 때 적절한 패키지가 깔려있는지 확인( 글로벌에서 계속 진행했을 경우, Flask와 같은 필요없는 패키지들이 깔려있을 것이다.)

```bash
# 가상환경을 설치할 폴더에서 실행
$ pythom -m venv venv

#가상환경 진입
$source venv/Scripts/activate   #venv가 있는 폴더로 들어왔을 때
$source ~venv/Scripts/activate  #venv가 위치하고 잇는 상세 경로로 진입 가능

#가상환경 나오기
$deactivate  #어느 겨올에서나 상관없음
```



### 1.2 장고 설치 

```bash
(venv)
$ pip install django 		 #최신버전설치
$ pip install django==2.1.8  #원하는 버전 설치
```

```bash
#장고 버전 간단하게 확인
$pip list
```



### 1.3 장고 프로젝트 시작 및 개발 진행

```bash
#장고 프로젝트를 담을 폴더 생성
$ mkdir 00_django_intro
# 폴더로 이동
$ cd 00_django_intro
```

```bash
05_Django/00_django_intro/
$ django-admin startproject config . # 현재 폴더를 프로젝트 폴더로 설정! (경로 주의)
```

```
00_django_intro/
	config/
		settings.py
		...
	manage.py
```

```bash
#반드시 manage.py 가 있는 경로에서 명령어 실행
# manage.py : 장고프로젝트와 의사소통하는 상호작용 커맨드라인 유틸리티
$ python manage.py runserver
```

- 터미널에 출력되는 로컬호스트 주소로 들어가서 **로켓**확인
- 이서버는 장고가 제공하는 경량 개발용 서버 - 배포시 절대 이용해선 안된다

### 1.5 Project 폴더 구조 확인

```
config/
	__init__.py
	settings.py
	urls.py
	wsgi.py
```

- ```
  __init__.py
  ```

  - 빈 파일이며, 우리가 다룰 일은 없다.
  - Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시한다.

- ```
  settings.py
  ```

  - 우리가 만드는 웹 서비스의 모든 환경설정이 담긴다. (ex- Application 등록, Static files 설정, Database 설정 등)
  - 즉, Django Project 내의 모든 환경이 저장된 파일이다.

- ```
  urls.py
  ```

  - 웹 서비스의 URL 경로와 View 함수의 연결을 정의한다.

- ```
  wsgi.py
  ```

  - Web Server Gateway Interface
  - 파이썬 웹 프레임워크에서 사용하는 웹 서버 규칙

### 1.5 Application생성

- project  vs Application  차이점?
  - Project는 여러개의 Application을 담는 그릇의 역할을 한다
    - 커다란 장고 프로젝트의 각종 환경설정들이 담긴다
    - 하나의 프로젝트는 여러개의 애플리케이션을 가질 수 있다
  - Application은 실제 웹 서비스에서 어떠한 역할을 수행하는것을 담당한다
    - 예를 들어 게시글을 조회하고 수정,삭제하거나 사용자의 로그인,로그아웃,회원가입등을 하는 모든 행위는 애플리케이션이라는 친구가 수행한다
    - 기본적으로 애플리케이션은 하나의 역할 및 기능 단위로 쪼개는것이 원칙이다. 하지만 장고 개발진에서 어떤식으로 나누라는 기준을 제공하응것은 아니므로 프로젝트를 수행하면서 프로젝트 사정에 맞게 알아서 쪼개면 된다.
    - 애플리케이션 이름은 가능한 **복수형**(ex - pages, names, )등으로 설정한다

```bash
# magage.py 경로 위치 학왼
$ python manage.py startapp pages
```

### 1.6 Application 폴더구조

```
pages/
	admin.py
	apps.py
	models.py
	tests.py
	views.py
```

- ```
  admin.py
  ```

  - 관리자용 페이지를 커스터마이징하는 파일

- ```
  apps.py
  ```

  - 애플리케이션의 구성 정보가 담긴 파일

- ```
  models.py
  ```

  - 애플리케이션에서 사용하는 데이터베이스 정보가 담긴 파일

- ```
  tests.py
  ```

  - 테스트 코드가 담긴 파일

- ```
  views.py
  ```

  - 사용자에게 보여줄 데이터를 가공하는 뷰 함수가 담긴 파일
  - Flask에서 app.py에 정의했던 함수가 담기는 장소

### 1.7  Application등록

프로젝트가 자동으로 애플리케이션을 인식하지 않는다. 따라서 프로젝트의 settings.py에 가서 애플리케이션 등록 절차를 거쳐야 한다.

```python
# config/setting.py


INSTALLED_APPS =[
    # Local apps
    'pages',
    
    # Third party apps
    
    # Django apps
    ...
]
```

### 1.8 추가설정

- `LANGUAGE_CODE = 'ko-kr'`
- `TIME_ZONE = 'Asia/Seoul'`
- 서버 새로고침해서 언어 설정이 바뀌었는지 확인한다

### 1.9 MTV 패턴

- 장고에서는 MTV 패턴이라고 부르지만, 실제로는 MVC패턴과 동일하다
  - `Model` : 데이터베이스를 정의
  - `Template` : 사용자에게 어떻게 데이터를 보여줄 지 정의 ( 예쁘게 담아서 보여줌 )
  - `View` : 사용자에게 어떤 데이터를 보여줄 지 정의 ( 보여줄 데이터 가공)

- 오늘은 Template 과 View를 이용해서 요청 - 응답 구조를 실습한다

- Django에서는 .py 3대장이라고 불리는 친구들이 있다

  - `models.py` : 데이터베이스 관리

  - `views.py` : 페이지 관리 (페이지 하나당 하나의 함수)

  - `urls.py` : URL과 View 함수 매핑

    ​	



## 2.Django request-response 구조 실습

### 코드 작성 순서 (권장)

> 대출창구(views.py)를 만들지도 않았는데 손님을 대출창구로 모시면(urls.py) 컴플레인 받는다. 에러 뿜는다.

- views.py : 보여주고자 하는 페이지의 뷰 함수를 작성한다.
- templates : 사용자에게 보여줄 템플릿 페이지를 작성한다.
- urls.py : 해당 경로로 들어왔을 때 뷰 함수를 실행시킨다.

### 2.1 템플릿 변수(Template Variable)

### 2.2 동적 라우팅 (Variable Routing)

> Why? greeting/도현 , greeting/경희 등의 대한 각각의 수백개의 페이지를 작성하는 수고를 덜 수 있다.

- 함수의 인자로 변수 명을 순서대로 작성한다.

#### hello : 변수 1개 넘기기

- URL을 통해 주어지는 '이름'을 출력한다.

  - views.py

    ```python
    def hello(request, name):
        context = {'name' : name }
        return render(request, 'hello.html', context)
    ```

  - urls.py

    ```python
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        # 동적 라우팅을 위한 변수 설정
        path('hello/<str:name>/', views.hello),
        path('index/', views.index),
        path('introduce/', views.introduce),
        path('dinner/', views.dinner),
        path('image/', views.image),
        path('admin/', admin.site.urls),
    ]
    ```

  - hello.html

    ```html
    <h1>Hello~~~~~~~~</h1>
    <h2>It's {{name}} .</h2>
    ```

​           - radius.html

```
<h1>{{rad}} 인 원의 넓이는 {{result}} 입니다. </h1>
```

#### hello : 템플릿 변수를 여러개 넘기기

- 동적 라우팅을 통해 이름과 저녁 메뉴

  - views.py

    ```python
    def hello(request, name):
        menu = ['초밥', '삼겹살', '치즈돈까스', '살치살 스테이크']
        today_pick = random.choice(menu)
    
        context = {
            'name' : name,
            'pick' : today_pick,
            }
        return render(request, 'hello.html', context)
    ```

  - urls.py

    ```python
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        # 동적 라우팅을 위한 변수 설정
        path('hello/<str:name>/', views.hello),
        path('index/', views.index),
        path('introduce/', views.introduce),
        path('dinner/', views.dinner),
        path('image/', views.image),
        path('admin/', admin.site.urls),
    ]
     
    ```

  - hello.html

    ```html
    <h1>Hello~~~~~~~~</h1>
    <h2>It's {{name}} .</h2>
    <h2>오늘은 {{pick}} 먹어유.</h2>
    ```







### 2.3 실습문제



##  3.DTL (Django Template Laguage)

- 장고에 기본적으로 내장된 템플릿 엔진
- 플라스크에 내장된 jinja2가 내장되어있어서 사용했던 것과 마찬가지다
- 사용자에게 보여줄 데이터를 가공하는 작업이 필요할경우 DTL에 내장된 연산방식을 사용하지말고  되도록이면 view함수 내부에서 데이터를 가공한 뒤 템플릿에게 넘겨주자.

### 3.1 DTL 활용해보기

### 기본 코드

- views.py

  ```python
  from datetime import datetime
  def template_language(request):
      menus = ['짜장면', '탕수육', '짬뽕', '양장피']
      my_sentence = 'Life is short, you need python'
      messages = ['apple', 'banana', 'cucumber', 'mango']
      datetimenow = datetime.now()
      empty_list = []
      context = {
          'menus': menus,
          'my_sentence': my_sentence,
          'messages': messages,
          'empty_list': empty_list,
          'datetimenow': datetimenow,
      }
      return render(request, 'template_language.html', context)
  ```

- urls.py

  ```python
  from django.contrib import admin
  from django.urls import path
  from pages import views
  
  urlpatterns = [
  
      path('template_language/', views.template_language),
      path('hello/<str:name>/', views.hello),
      path('index/', views.index),
      # path('introduce/', views.introduce),
      path('introduce/<str:name>/<str:age>/<str:hobby>/<str:speciality>/', views.introduce),
      path('times/<int:num1>/<int:num2>', views.times),
      path('radius/<int:rad>', views.radius),
      path('imageSize/<str:width>/<str:height>', views.imageSize),
      path('dinner/', views.dinner),
      path('image/', views.image),
      path('admin/', admin.site.urls),
  ]
  ```

#### 주석

- 주석 형식

  ```python
  {% comment %} 주석입니다.  {% endcomment %}
  ```

#### 반복문

- 반복문 형식

  ```python
  {% for menu in menus %}
   
  {% endfor %}
  ```

- template_language.html

  ```python
  <h1>반복문</h1>
  <h4>메뉴판</h4>
  
  <ul>
  {% for menu in menus %}
    <li>{{menu}}</li>
  {% endfor %}
  </ul>
  ```



#### 조건문

- 조건문 형식

  ```python
  {% if 'a'  in 'apple' %}
  
  {% endif %}
  
  
  
  {% if menu == '짜장면' %}
  
  {% else %}
  
  {% endif %}
  ```

- template_language.html

  ```python
  <h1>조건문</h1>
  <h4>메뉴판</h4>
  {% if '짜장면' in menus %}
    <p>짜장면에는 정성이 가득</p>
  {% endif %}
  
  <hr>
  
  <ul>
  {% for menu in menus %}
    {% if menu == '짜장면' %}
      <li>{{menu}} : 짜장면에는 정성이 가득</li>
    {% else %}
      <li>{{menu}}</li>
    {% endif %}
  {% endfor %}
  </ul>
  ```

#### Length Filter

- Length Filter 형식

  - `|length`

    ```
    {% if message|length > 5 %}
    
    {% else %}
    
    {% endif %}
    ```

- template_language.html

  ```
  <h1>Length Filter</h1>
  {% for message in messages %}
    {% if message|length > 5 %}
      <P>{{message}} ... 너무 길어요. 줄여주세요!</p>
    {% else %}
      <P>{{message}} 의 길이는 {{message|length}} 글자!</p>
    {% endif %}
  {% endfor %}
  ```

#### Lorem

- Lorem 형식

  - w : word

  - p :

  - random : 무작위

    ```
    {% lorem %}
    ```

- template_language.html

  ```
  <h1>Lorem Text</h1>
  {% lorem %}
  
  <hr>
  
  {% lorem 3 w%}
  
  <hr>
   {% comment %} 랜덤으로 단어  {% endcomment %}
  {% lorem 4 w random%}
  
  <hr>
  
  {% lorem 4 p %}
  ```

#### 글자수 제한 (Truncate - 자르기)

- Truncate 형식

  ```
  {{my_sentence|truncatewords:3}}
  {{my_sentence|truncatechars:3}}
  ```

- template_language.html

  ```
  <!-- 단어 단위로 자른다. -->
  <p>{{my_sentence|truncatewords:3}}</p>
  
  <!-- 문자 단위로 자른다. / 3번째 포함 X -->
  <p>{{my_sentence|truncatechars:3}}</p>
  
  <!-- 문자 단위로 자른다. / 10번째 포함 X -->
  <p>{{my_sentence|truncatechars:10}}</p>
  ```

  #### 연산

  > 자세한 내용은 [django mathfilters](https://pypi.org/project/django-mathfilters/) 참고

  - 기본적으로, 사용자에게 보여줄 데이터를 가공하는 것은 뷰 함수에서 처리하자

    반드시 필요한 경우에만 연상 필터를 사용한다.

  - 연산 형식

    ```
    {{ 4|add:6}}
    ```

  - template_language.html

    ```
    <h1>연산</h1>
    <!-- 
        기본적으로, 사용자에게 보여줄 데이터를 가공하는 것은 뷰 함수에서 처리하자
        반드시 필요한 경우에만 연상 필터를 사용한다.
    
        django mathfilters
     -->
    <p>{{ 4|add:6}}</p>
    
    <hr>
    ```

    기타

  - 특정 str를 url로 변환

    - urlize

    - template_language.html

      ```
      {{'google.com'|urlize}}
      ```

### 로또 번호 추첨

- 임으로 출력한 로또 번호와 가장 최근에 추첨한 로또 번호 비교해서 당첨여부 확인

  - views.py

    ```python
    # 실습 3
    # 로또 번호 추첨(리스트 + a 활용)
    # 임의로 출력한 로또 번호와 가장 최근에 추첨한 로또 번호 비교해서 당첨여부 확인
    def lotto(request, lottonum, bonus):
    
        # [18,34,39,43,44,45]
        real_lotto = list(map(int, lottonum.strip().split(',')))
        # 잘라서 list
        s_lotto = sorted(real_lotto)
    
        num_list = [i for i in range(1, 47)]
        lotto_list = random.sample(num_list, 6)
        my_bnum = random.choice(num_list)
        s_lotto_list = sorted(lotto_list)
       
        count = 0
        for i, j in zip(s_lotto, s_lotto_list):
            if i == j:
                count += 1
            else : 
                pass
    
        if count == 6:
            rank = "1"
        elif count == 5 and bonus == my_bnum: 
            rank = "2"
        elif count == 5 and bonus != my_bnum: 
            rank = "3"
        elif count == 4: 
            rank = "4"
        elif count == 3: 
            rank = "5"
        else :
            rank = "꽝"
    
    
    
       
        result = '안녕, 수연입니다!'
    
        context = {
            'real_lotto': real_lotto,
            'lotto_list': lotto_list,
            'count': count,
            'rank': rank,
            'bonus': bonus,
            'my_bonus': my_bnum,
        }
        return render(request, 'lotto.html',context)
    ```

  - urls.py

    ```python
    
    urlpatterns = [ 
        			#22,33,44,55,66,77  33
        path('lotto/<str:lottonum>/<int:bonus>', views.lotto),
        path('ispal/<str:word>', views.ispal),
        path('isbirth/', views.isbirth),
        path('template_language/', views.template_language),
        path('hello/<str:name>/', views.hello),
        path('index/', views.index),
        # path('introduce/', views.introduce),
        path('introduce/<str:name>/<str:age>/<str:hobby>/<str:speciality>/', views.introduce),
        path('times/<int:num1>/<int:num2>', views.times),
        path('radius/<int:rad>', views.radius),
        path('imageSize/<str:width>/<str:height>', views.imageSize),
        path('dinner/', views.dinner),
        path('image/', views.image),
        path('admin/', admin.site.urls),
    ]
    
    ```

  - lotto.html

    ```python
    <h1>인생 역전 가능할까요?</h1>
    <h3>당신이 뽑은 로또 번호는... </h3>
    <p>{{lotto_list}}</p>
    
    <h3>실제 로또 번호는... </h3>
    <p>{{real_lotto}}</p>
    
    <h3>실제 보너스 번호는  </h3>
    <p>{{bonus}}</p>
    
    <h3>나의 보너스 번호는  </h3>
    <p>{{my_bonus}}</p>
    
    <h3>맞은 개수 </h3>
    <p>{{count}}</p>
    
    <h3>순위 </h3>
    {% if rank == '꽝' %}
      <p>꽝! 다음 기회에...</p>
    {% else %}
      <p>{{rank}} 등 입니다!</p>
    {% endif %}
    ```

​      

​    **Is it your birthday?**

- 오늘 날짜와 본인 실제 생일 비교해서 , 맞으면 예! 아니면 아니오!

- 날짜 라이브러리 활용

  - views.py

    ```python
    def isbirth(request):
        days = datetime.now()
        if days.month == 10 and days.day == 28:
            result = True
        else : 
            result = False
    
        context = {
            'result': result,
        }
        return render(request, 'isbirth.html',context)
    ```

  - urls.py

    ```python
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        path('isbirth/', views.isbirth),
        path('lotto/<str:lottonum>', views.lotto),
        path('template_language/', views.template_language),
        path('hello/<str:name>/', views.hello),
        path('index/', views.index),
        # path('introduce/', views.introduce),
        path('introduce/<str:name>/<str:age>/<str:hobby>/<str:speciality>/', views.introduce),
        path('times/<int:num1>/<int:num2>', views.times),
        path('radius/<int:rad>', views.radius),
        path('imageSize/<str:width>/<str:height>', views.imageSize),
        path('dinner/', views.dinner),
        path('image/', views.image),
        path('admin/', admin.site.urls),
    ]
    ```

  - isbirth.html

    ```html
    <h1>Is it your birthday?</h1>
    {% if result %}
      <h2>생일 축하해~</h2>
      {% else %}
      <h2>너의 생일이 아니야</h2>
    {% endif %}
    ```

  **회문 판별**

- 오디오는 거꾸로 해도 오디오 -> 회문

- (팰린드롬 / 문자열 슬라이싱 파트 활용 )

  - views.py

    ```python
    def ispal(request, word):
        # 검색 키워드 : 파이썬 문자열 슬라이스
        if word == word[::-1]:
            result = True
        else :
            result = False
        context = {
            'word': word,
            'result': result,
        }
        return render(request, 'ispal.html',context)
    ```

  - urls.py

    ```python
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        path('lotto/<str:lottonum>', views.lotto),
        path('ispal/<str:word>', views.ispal),
        path('isbirth/', views.isbirth),
        path('template_language/', views.template_language),
        path('hello/<str:name>/', views.hello),
        path('index/', views.index),
        # path('introduce/', views.introduce),
        path('introduce/<str:name>/<str:age>/<str:hobby>/<str:speciality>/', views.introduce),
        path('times/<int:num1>/<int:num2>', views.times),
        path('radius/<int:rad>', views.radius),
        path('imageSize/<str:width>/<str:height>', views.imageSize),
        path('dinner/', views.dinner),
        path('image/', views.image),
        path('admin/', admin.site.urls),
    ]
    ```

  - ispal.html

    ```html
    {% if result %}
     <p> {{word}}는 거꾸고 말해도 {{word}}이므로, 회문이다.  </p>
    {% else %}
     <p> {{word}}는 회문이 아니다.  </p>
    {% endif %}
    ```

## 코드 작성 순서 (권장)

> 대출창구 (views.py)를 만들지 않았는데 손님을 대출창구로 모시면 (urls.py), 컴플레인을 받는다. (에러를 뿜는다.)

1. views.py (view 작성)
   - 보여주고자 하는 페이지의 view 함수를 작성한다.
   - 기능 구현 우선
2. templates
   - 사용자에게 보여줄 Template 페이지를 작성한다.
3. urls.py (view 등록)
   - 사용자가 해당 경로로 들어왔을 때 view 함수를 실행한다.

#### github.com/educiao-hphk



