## Start Django 2



### 1. HTML Form Tag

- 스태틱웹 vs 다이내믹 웹
  - 스태틱 웹 : 단순히 html 페이지 여러개로 구성되어있는 사이트
  - 다이내믹 웹  : 데이터베이스에 변동을 주어서 데이터베이스에 따라 웹 사이트의 내용이 바뀌는 웹서비스
- Form 를 통해서 사용자로부터 정보를 받거나 정보를 가공하거나 하는 로직을 구현했었는데, 결국 다이내믹 웹을 구현하기 위해서는 Form 을 통해서 정보를 요청하는 절차가 반드시 필요하다.

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

- 서버의 데이터(리소스)를 변경시키지 않는 요청이고, HTML 파일을 조회할 때 사용한다. 우리는 서버에 GET요청을 하면, HTML 문서 한장을 받는다

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
```



### 3. HTML Form - POST 요청

- CRUD
  - Create
  - Read
  - Update
  - Delete

### 3.1 기본 개념

- POST 요청은 GET 요청처럼 쿼리스트링에 데이터가 노출되는것이 아니라, **HTTP Body에 담겨서 전송** 된다
  - GET 요청 -> Read
  - POST 요청 -> Create, Update, Delete
- POST 요청은 데이터(리소스)를 수정/삭제 시키는 로직이기 때문에, 똑같은 요청을 여러번 시도하게되면 서버에서 응답하는 결과는 다를 수 있다.

- 원칙적으로 POST요청을 보냇는데 HTML 파일을 그려주는(render)응답은 해서는 안된다. HTML 파일을 그려주는 응답은 GET요청에서만 사용한다
  - 사용자가 로그인을 하는 로직은 POST요청을 통해서 이루어진다. 로직 마지막에 어떤 정보를 변수로 넘겨서 HTML파일을 넘겨주는 로직을 구현하는 것이 아니라, 로그인이 끝나면 메인페이지(`'/'`)등으로 redirect 시켜주는 로직을 구현해야한다. 

- `{% csrf_token %}`

  - CSRF 공격을 막기 위한 최소한의 신원 확인 장치
  - 장고 내부적으로 CSRF 공격을 막기 위해서

  

```python
#setting.py

<MIDDLEWARE = [
    ...
    'django.middleware.csrf.CsrfViewMiddleware',
    ...
]
```

- 얘가 존재하기 때문에, Form 에서 POST요청을 할 때 {%  csrf_token %}을 넣지 않으면 `403 forbidden` 에러를 뿜는다. 403에러는 서버에는 정상적으로 접근을 하였으나, 권한이 없어서 접근하지 못하는 에러다.
- `get요청은"야, HTML 파일 하나 내놔!" 라고 하는 단순한 정보 조회 로직이지만, `post 요청`은 서버측 DB(리소스)에 변경을 요청하는 것이기 때문에 신원을 확인하는 절차가 없으면 임의의 공격을 통해 서버가 해킹당하게 된다.
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

