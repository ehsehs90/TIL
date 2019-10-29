## 10.10.29(화) : Start Django 2

### 1. HTML Form Tag

- **스태틱웹 vs 다이내믹 웹**
  - `스태틱 웹` : 단순히 html 페이지 여러개로 구성되어있는 사이트
  - `다이내믹 웹`  : 데이터베이스에 변동을 주어서 데이터베이스에 따라 웹 사이트의 내용이 바뀌는 웹 서비스
- Form 를 통해서 사용자로부터 정보를 받거나 정보를 가공하거나 하는 로직을 구현했었는데, 결국 **다이내믹 웹을 구현하기 위해서는 Form 을 통해서 정보를 요청하는 절차가 반드시 필요**하다.

- `<form></form>`
  - 사용자로부터 제공받은 데이터를 서버 측에 전송해주는 역할
  - 사용자가 여러 정보를 입력할 수 있는 수단을 제공 -> input 태그를 통해!
    - `<form action="/new/">` : 어디로 보낼 것인지 서버측 경로를 지정
    - `<form action="" method ="GET">` :  요청 방식을 무엇으로 할 것인지 지정
- `<input>`
  - Form 태그안에서 가장 중요한 태그!  사용자로부터 어떠한 정보를 입력받는 태그
  - `<input type="">` : 사용자가 입력할 데이터의 종류 지정
  - `<input type ="" name="">` : 서버측에서 사용자가 입력한 값을 가져올 이름으로 사용



### 2. HTML Form - GET 요청

### 2.1 기본 개념

- 요청의 종류 중 GET  요청은 서버로부터 정보를 조회하는데 사용한다. 데이터를 서버로 전송할 때 쿼리스트링을 통해 전송한다

- **서버의 데이터(리소스)를 변경시키지 않는 요청**이고, HTML 파일을 조회할 때 사용한다. 우리는 서버에 GET요청을 하면, HTML 문서 한장을 받는다

- throw & catch

  ```html
  
  <!--throw -->
  
  <form action ="/catch" method = "GET">
      <input type="text" name = "message">
      <input type="submit" value="던지자">
  </form>
  
  
  <!--catch -->
  
  <h1>니가 보낸 정보를 잘 받았고,
  그 정보의 내용은 {{ message}} 야</h1>
  
  ```

### 2.2 실습

```python
# 아스키 아트

#아스키 아티 ASCII ARTII
#사용자로부터 텍스트 입력받는 페이지
def art(request):
     
    return render(request,'pages/art.html')
 
 #/make?text=ASCII+art

#텍스트 받아서 아스키 아트로 보여주는 페이지
def result(request):
    text = request.GET.get('text') 
    
    #2. ASCII API 로 요청을 보내서 응답 결과를 변수에 담는다 (폰트 정보를)
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text 
    #3. 가져온 폰트들을 리스트 형태로 바꾼다    
    fonts= fonts.split('\n')
    #4. 폰트 하나를 랜덤으로 선택한다
    font=random.choice(fonts) 
    #5. 사용자가 입력한 단어와 랜덤으로 선택한 폰트 정보를 API에게 요청한다
    result = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}').text
    #6. 최종 결과물을 사용자에게 돌려준다.
    return render(request, 'pages/result.html', {'result':result})
```



### 3. HTML Form - POST 요청

- CRUD
  - Create : 생성
  - Read : 조회
  - Update : 수정
  - Delete : 삭제

### 3.1 기본 개념

- POST 요청은 GET 요청처럼 쿼리스트링에 데이터가 노출되는것이 아니라, **HTTP Body에 담겨서 전송** 된다
  - GET 요청 -> Read
  - POST 요청 -> Create, Update, Delete
- POST 요청은 데이터(리소스)를 수정/삭제 시키는 로직이기 때문에, 똑같은 요청을 여러번 시도하게되면 서버에서 응답하는 결과는 다를 수 있다.

- 원칙적으로 POST요청을 보냈는데 HTML 파일을 그려주는(render)응답은 해서는 안된다. HTML 파일을 그려주는 응답은 GET요청에서만 사용한다
  - ex) 사용자가 로그인을 하는 로직은 POST요청을 통해서 이루어진다. 로직 마지막에 어떤 정보를 변수로 넘겨서 HTML파일을 넘겨주는 로직을 구현하는 것이 아니라, 로그인이 끝나면 메인페이지(`'/'`)등으로 redirect 시켜주는 로직을 구현해야한다. 

- `{% csrf_token %}`

  - CSRF 공격을 막기 위한 최소한의 신원 확인 장치
  - 장고 내부적으로 CSRF 공격을 막기 위한 미들웨어가 기본적으로 적용되어 있다.

  

```python
#setting.py

<MIDDLEWARE = [
    ...
    'django.middleware.csrf.CsrfViewMiddleware',
    ...
]
```

- 얘가 존재하기 때문에, Form 에서 POST요청을 할 때 {%  csrf_token %}을 넣지 않으면 `403 forbidden` 에러를 뿜는다. 403에러는 서버에는 정상적으로 접근을 하였으나, 권한이 없어서 접근하지 못하는 에러다.
- `get요청은`"야, HTML 파일 하나 내놔!" 라고 하는 단순한 정보 조회 로직이지만, ``post 요청`은 서버측 DB(리소스)에 변경을 요청하는 것이기 때문에 신원을 확인하는 절차가 없으면 임의의 공격을 통해 서버가 해킹당하게 된다.
- `{% csrf_token %}` 을 코드에 삽입하면, 실제 Form태그를 개발자도구로 찍어보면 hidden type의 input 태그가 생기고 그 안에 암호화된 hash값이 함께 전송되는 것을 확인할 수 있다.

```html
<!--user_new -->
<form action ="/user_create/" method = "POST">
    {% csrf_token %}
    <input type="text" name = "user_id">
    <input type ="password" name="user_pwd">
    <input type="submit" value="가입하기">
</form>


<!--user_create -->
<h1> {{user_id}} 님 안녕하세요~ 만나서 반갑습니다</h1>
<h1> pwd {{user_pwd}}</h1>
```

		- hidden type의 input 태그 확인 !	
		- 

## 3. 정적파일(Static Files)

### 3.1 기본 개념

- 정적 파일?
  -  별도의 가공 없이 사용자에게 그냥 전달만 해주면 되는 파일들, 예를들어 `이미지`,` css`, `JavaScript` 파일들이 있다 서버(프로그래머)가 미리 준비해두고, 사용자는 그냥 받아보기만 하면 된다.
  - 이미지의 경우 데이터베이스를 통해 저장한 것이 아니라면, 일정한 주소를 통해 이미지를 불러와야 하는데 로컬에 저장했을 경우 그냥 경로만 적어서는 이미지를 불러올 수 없다
    - 장고에서 제공하는 static 파일 관리 방법을 준수해서 이미지를 불러와야한다.

## 4. URL 로직 분리

###### 이때까지 프로젝트 폴더 안에 있는 `urls.py`에서 모든 URL경로를 관리했다. 근데 애플리케이션이 추가적으로 생기고, 관리해야할 URL경로가 많아지면 매우 복잡해진다. 각자의 애플리케이션에 해당하는 URL은, 애플리케이션이 직접 관리하도록 위임시켜보자.

### 4.1 애플리케이션 하나 더 만들어보기

```bash
$ python manage.py startapp utilities
```

```
#settings.py

INSTALLED_APPS = [
	'utilities',
	...
]
```

### 4.2 애플리케이션 urls.py생성

```
config/
	urls.py
pages/
	urls.py
utilities/
	urls.py
```



### 4.3 프로젝트 urls.py 로직 수정

###### include 메서드를 사용해서 일정한 경로로 오는 요청들을 애플리케이션의 urls.py에서 처리하도록 위임한다

```python
#config/urls.py
from django.urls import path, include



#사용자가 'pages/'로 시작하는 경로로 들어오면 ,
#pages 앱 안의 urls.py에서 처리해라! 
urlpatterns = [
    path('pages/', include('pages.urls')),
    path('utilities/', include('utilities.urls')),
    path('admin/', admin.site.urls),
]
```



### 4.4 애플리케이션 urls.py

```python
# pages/urls.py (-> 다른 애플리케이션도 형식 동일)

from django.urls import  path
from . import views

urlpatterns = [
    path('static_sample/',views.static_sample),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('make/', views.art),
    path('result/', views.result),    
    path('throw/', views.throw),
    path('catch/', views.catch),   #'http://localhost/pages/catch/' 라는 경로로 요청했을 경우
    path('',views.index),  #'http://localhost/pages/'라는 경로로 요청했을 경우
]

```

### 5. 이름공간(Namespace)정리

- 장고는 기본적으로 탬플릿(스태틱도 동일) 파일을 탐색할 때, 템플릿 폴더를 전부 모아놓고 순서대로 탐색한다

  ```txt
  [As-is 폴더구조]
  pages/
      templates/
          index.html
  utiliites/
      templates/
          index.html
  
  [As-is 뷰 함수 - pages]
  def index(request):
      return render(request, 'index.html')
  
  [settings.py]
  INSTALLED_APPS = [
      'utilities',
      'pages',
      ...
  ]
  ```

  - 탐색하는 순서는 settings.py 에 있는 INSTALLED_APPS=[] 리스트 위에서부터 차례대로 탐색한다.

  - 따라서 중간에 구분하는 폴더를 만들어주지 않은경우, 나는 pages의 index.html이라는 템플릿을 렌더링하고 싶었지만 앱 등록 순서상 상위에 있는 utilities의 index.html 템플릿이 렌더링 된다.

    ```
    [To-be 폴더구조]
    pages/
        templates/
            pages/
                index.html
    utiliites/
        templates/
            utilities/
                index.html
    
    [To-be 뷰 함수 - pages]
    def index(request):
        return render(request, 'pages/index.html')
    ```

  - 그냥 templates 폴더를 방문해서 파일을 찾지 않고 해당 애플리케이션에 맞는 코드를 찾기위해 중간데 폴더를 하나 더 생성한다.



## 6. 템플릿 상속(Template Inheritance)



### 6.1 기본 개념

- 상속은 기본적으로 `코드의재사용성` 에 초점을 맞춘다

  - 템플릿에서 반복되는 코드를 매번 일일히 치고 있을 여유는 없다. 반복되는 부분은 미리 만들어두고 가져다 쓰자!

  ### 6.2 `base.html` 생성



## 7. 개발환경 관리

- 프로젝트를 받아보는 다른 사람이 프로젝트에 필요한 파이썬 패키지들을 정확하게 설치하기 위해 현재 설치되어 있는 패키지 목록들을 넘겨준다.
  - 깃헙에 업로드시 불필요하게 패키지들을 같이 올려 용량을 높일 필요는 없다. 목록만 넘겨주고, 받는 사람이 본인컴퓨터에 알아서 설치할 수 있도록 환경설정까지만 한다
- 파이썬 버전의 경우 같이 올라가지 않기 때문에, 되도록 `READ.ME`에 명시해준다.

```bash
#현재 가상환경에 설치되어 있는 패키지 리스트 목록을 파일로 만들기
$ pip freeze > requirements.txt

# 패키지 리스트 목록을 읽어서, 없는 패키지를 자동으로 설치하기
$ pip install -r requirements.txt
```

