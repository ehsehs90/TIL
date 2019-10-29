

# Flask

## 1. Start Flask

### 1.1 Install

- 첫 시작은 무조건 [공식문서](http://flask.palletsprojects.com/en/1.1.x/)를 참고하자!

  ```python
  # hello.py
  
  from flask import Flask
  app = Flask(__name__)
  
  @app.route('/')
  def hello():
      return 'Hello World!'
  ```

### 1.2 개발용 서버 실행하기

- 일단 그냥 실행해보기 - flask app 을 hello.py 로 하고 flask를 실행한다

  ```bash
  $ FLASK_APP=hello.py flask run
  ```

- 여기서 생기는 두 가지 문제

  - 서버를 실행하는 명령어가 너무 길다.
  - 코드 내용이 바뀌면 서버를 껐다 켜야된다.

- 간단한 서버 실행 코드로 바꿔보기

  - `hello.py` -> `app.py` : 플라스크는 기본적으로 폴더에서 app.py를 실행하려고 한다.

  - 실제 개발단계에서도 이름을 app.py로 하는 것을 권장한다.

  - 코드 추가하기

    ```python
    # app.py
    
    ...
    
    # end of file
    if __name__ == '__main__':
        app.run(debug=True)
    ```

  - 명령어 실행

    ```bash
    $ python app.py
    ```

### 1.3 간단한 페이지 렌더링하기

> 단순한 문자열 리턴, HTML 태그 리턴이 모두 가능하다.

- Flask import 하기

  ```python
  from flask import Flask
  app = Flask(__name__)
  ```
  
- **문자열** 리턴

  ```
  @app.route('/')
  def hello():
      return 'Hello World!'
  ```

- **HTML 요소** 사용해서 리턴

  ```python
  @app.route('/')
  def hello():
      return '<h1>Hello World!</h1>'
  ```

### 1.4 동적 라우팅(Variable Routing)

> 사용자가 URL을 통해 입력한 값을 받아서 사용할 수 있다.

```python
@app.route('/greeting/<string:name>')
def greeting(name):
    return f'안녕, {name}?'
```

### 1.5 Render Template

> 템플릿을 미리 만들어두고 사용자에게 보여줄 수 있다.

- flask에서 제공하는 `render_template` 모듈을 불러온다.

  ```python
  from flask import Flask, render_template
  ```

- `templates` 폴더를 생성한다.

  - 플라스크는 render_teamplate 메서드를 사용할 때 기본적으로 루트 디렉토리에 있는 `templates`라는 폴더를 탐색해서 html 파일을 찾는다.

    ※ 뒤에 s 빼먹으면 jina2 관련 에러를 뿜어내니 조심하자!

    ```
    03_Flask/
    	templates/
    		index.html
    		...
    	app.py
    ```

- 사용해보자.

  ```python
  @app.route('/')
  def hello():
      return render_template('index.html')
  ```

- **render_template + parameters**

  ```python
  # app.py
  
  @app.route('/greeting/<string:name>')
  def greeting(name):
      return render_template('greeting.html', html_name=name)
  ```

  ```html
  <!-- greeting.html -->
  <body>
    <h1>당신의 이름은 {{ html_name }}입니다.</h1>
  </body>
  ```









### 1.6 Jinja2 템플릿 엔진 활용하기

> 플라스크가 가지고 있는 jinja2라는 템플릿 엔진을 활용해서 꾸며보자.

- **조건문**

  ```html
  <!-- greeting.html -->
  <body>
    {% if html_name == '도현' %}
      <p>어서오세요, 유단자여...</p>
    {% else %}
      <p>제발 무술을 배우세요...</p>
    {% endif %}
  </body>
  ```


- 반복문 문법

```python
{% for i in array_list %}

{% endfor %}
```

- 영화 목록을 받아 list로 출력하기

  - app.py

    ```python
    @app.route('/movies')
    def movie():
        movie_list = ['82년생 김지영', '조커', '엔드게임', '궁예']
        return render_template('movies.html', movies=movie_list)
    ```

  - movies.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
    
        <h2>영화 목록</h2>
        <ul>
            {% for movie in movies %}
                <li>{{movie}}</li>
            {% endfor %}
            
        </ul>
    
    </body>
    </html>
    ```

## 2. 응답-요청 (Request-Response)

### 2.1 Ping / Pong

#### Ping

- 사용자가 일정한 주소로 요청을 보내면, 사용자가 어떠한 값을 입력할 수 있는 Form이 담겨있는 페이지를 보여준다.

#### Pong

- 사용자로부터 Form 입력 데이터를 전달받고, 데이터를 가공해서 다시 보여준다.

- Ping / Pong

- Method="GET" : 서버 측에 어떤 OO를 달라고 요청을 보냄

  - 요청 코드 : user_name = request.args.get('user_name')

  - app.py

    ```python
    # ping : 사용자로부터 입력을 받을 Form 페이지를 넘겨준다. 
    @app.route('/ping')
    def ping():
        return render_template('ping.html')
    
    # pong : 사용자로부터 Form 데이터를 전달받아서 가공한다. 
    # ping에서부터 데이터를 받음
    # request 추가
    @app.route('/pong')
    def pong():
        user_name = request.args.get('user_name')
        return render_template('pong.html', user_name=user_name)
    ```

  - ping.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    
    <body>
        <!-- 사용자가 submit을 누르면 데이터가 pong에서 가공됨 -->
        <form action="/pong" method="GET">
            이름 : <input type="text" name="user_name"><br>
            <input type="submit"><br>
        </form>
    </body>
    
    </html>
    ```

  - pong.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <h2>{{user_name}} 님 안녕하세요! 데이터가 저희 서버로 들어왔어요.</h2>
    </body>
    </html>
    ```

### 2.2 Fake Naver & Google

> 위 Ping / Pong 구조에서 온전히 우리 웹 서비스 내에서 요청과 응답 프로세스를 구현했다. 하지만, 사용자로부터 요청만 받은 뒤, 데이터를 처리해서 돌려주는 응답 프로세스를 다른 서버 측에 넘겨줄 수 있다.

#### Fake naver

- Form에서 검색어를 입력받아 naver 검색 수행

  - app.py

    ```
    # fake naver
    @app.route('/naver')
    def naver():
        return render_template('naver.html')
    ```

  - naver.html

    ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <form action="https://search.naver.com/search.naver">
            <input type="text" name="query">
            <input type="submit">
        </form>
    </body>
    </html>
    ```

#### Fake google

- Form에서 검색어를 입력받아 google 검색 수행

  - app.py

    ```python
    # fake google
    @app.route('/google')
    def google():
        return render_template('google.html')
    ```

  - google.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <form action="https://www.google.com/search">
            <input type="text" name="q">
            <input type="submit">
        </form>
    </body>
    </html>
    ```

### 2.3 GodMadeMe (신이 나를 만들 때)

> [신이 나를 만들 때](https://kr.vonvon.me/quiz/2998) 를 구현해보자.

- 사용자로부터 이름을 입력받아, 랜덤으로 특성 3개를 사용자에게 보여준다.

  - app.py

    ```python
    import random
    
    # 사용자로부터 이름을 입력받을 Form 페이지
    @app.route('/vonvon')
    def vonvon():
        return render_template('vonvon.html')
    
    
    # 전달받은 이름을 기준으로 넘겨줄 각종 정보를 가공해서 돌려주는 (응답) 로직!
    @app.route('/godmademe')
    def godmademe():
    
        # 1. 사용자가 입력한 데이터를 가져온다. (Flask의 request 기능 사용)pytho
        user_name = request.args.get('user_name')
    
        # 2. 사용자에게 보여줄 여러가지 재밌는 특성 리스트를 만든다.
        first_list = ['잘생김', '못생김', '많이 못생김', '많이 잘생김', '앙주']
        second_list = ['자신감', '귀찮음', '쑥쓰러움', '열정적임']
        third_list = ['허세', '물욕', '식욕', '똘기']
    
        # 3. 특성 리스트에서 랜덤으로 하나씩을 선택한다. 
        first_choice = random.choice(first_list)
        second_choice = random.choice(second_list)
        third_choice = random.choice(third_list)
    
    
        # 4. 가공한 정보를 템플릿에 담아서 사용자에게 보여준다.
        return render_template('godmademe.html', user_html=user_name, first_html=first_choice, second_html=second_choice, third_html=third_choice)
    ```

  - vonvon.html

    - text form의 속성을 `name="user_name"`으로 설정했기 때문에 서버에서 user_name이라는 이름으로 받을 수 있다.

      - form 의 action 설정하기! `form action="/godmademe"`

      ```html
      <!DOCTYPE html>
      <html lang="en">
      
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <title>Document</title>
      </head>
      
      <body>
          <form action="/godmademe">
              <input type="text" name="user_name" placeholder="당신의 이름을 입력해주세요.  :) ">
              <input type="submit">
          </form>
      </body>
      
      </html>
      ```

  - godmademe.html

    - 랜덤으로 생성된 3개의 parameter를 전달받아 화면에 출력한다.

      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <title>Document</title>
      </head>
      <body>
          <h1>신이 {{user_html}} 을 만들 때</h1>
          <p>{{first_html}}</p>
          <p>{{second_html}}</p>
          <p>{{third_html}}</p>
      </body>
      </html>
      ```

### 2.4 아스키 아트 (ASCII Art)

> [ASCII Art API](http://artii.herokuapp.com/) 를 이용해 문자를 넘겨 그림을 그린다.
>
> - 파이썬 requsets 모듈 숙달하기 (API요청)

- API를 사용하기 위해 가상환경 (venv)에서 requests 모듈을 설치한다.

  ```bash
  $ pip install requests
  ```

- 설치된 requests 모듈을 import 한다.

  ```
  import random, requests
  ```

- 사용자로부터 입력을 받은 text 입력받고, 랜덤으로 font를 설정하여 ASCII ART로 변환해서 돌려준다.

  - app.py

    ```python
    # 1. 사용자로부터 임의의 텍스트를 입력받아서, 아스키 아트로 변환해서 돌려준다.
    # 이때, ASCII Art의 폰트는 랜덤으로 하나를 지정해서 변환한다.
    @app.route('/catch')
    def catch():
        return render_template('catch.html')
    
    
    @app.route('/result')
    def result():
        # 1. 사용자가 입력한 Form 데이터를 가져온다.
        text = request.args.get('word')
    
        # 2. ARTII API로 요청을 보내서, 응답 결과를 변수에 담는다. (폰트 정보)
        # requests.get([URL]) 을 통해 가져온 데이터를 text 로 담는다.
        fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    
    
        # 3. 가져온 폰트들을 리스트 형태로 바꾼다.
        fonts_list = fonts.split('\n')
    
        # 4. 폰트 하나를 랜덤으로 선택한다.
        my_font = random.choice(fonts_list)
    
        # 5. 사용자가 입력한 단어와 랜덤으로 선택한 폰트 정보를 담아서 API에게 요청한다.
        result = requests.get(f'http://artii.herokuapp.com/make?text={text}+art&font={my_font}').text
    
        # 6. 최종 결과물을 사용자에게 돌려준다.
        return render_template('result.html', result=result)
    ```

  - catch.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    
    <body>
        <form action="/result">
            <input type="text" name="word" placeholder="텍스트를 입력해주세요.  :) ">
            <input type="submit">
        </form>
    </body>
    
    </html>
    ```

  - result.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    
    <body>
        <pre>
                {{result}}
        </pre>
    </body>
    
    </html>
    ```