### Django-CSV파일 불러오기

#### Seed Data(Initial Data) 입력하기

###### 우리가 애플리케이션을 제작할 때 미리 준비해둔 데이터 혹은 애플리케이션 테스트용 데이터가 필요한 경우가 있다. 이때, 데이터를 하드코딩으로 일일이 넣을 수도 있다. **하지만 `fixtures`라는 기능을 이용해서 준비해둔 데이터를 쉽게 데이터베이스에 넣을 수 있다.**

##  1. Seed Data 활용

- Seed Data 활용하는 방법

  1. 애플리케이션의 데이터 베이스를 하드 코딩으로 미리 만든다.

     - 이후 `dump data` 명령어를 통해 fixture 데이터 형태로 만들어두고,

       데이터 베이스를 초기화시켜도 `loaddata` 명령어를 통해 다시 데이터를 불러와서 사용할 수 있다.

  2. 이미 Seed Data를 제공받았을 경우, 그냥 fixtures 폴더에 넣어두고 불러와서 사용한다.

- fixture 데이터 내용을 바꾸거나, 모델링 해둔 내용을 바꾸고 싶으면, 반드시 다시 `loaddata` 과정을 수행한다.

#### 1. 이미 데이터가 있을 경우

- `manage.py dumpdata > movies.json` 명령어를 통해서 현재 앱에서 가지고 있는 데이터를 빼낼 수 있다

- json 파일을 직접 작성하지 않고 현재  DB에 있는 데이터를 json으로 뽑아내고 싶을 경우 사용

- 이전 DB가 날아가더라도 `dumpdata`를 통해 빼둔 데이터들을 다시한번 활용할 수 있다

  ```shell
  (가상환경 확인 후)
  $ python manage.py dumpdata > movies.json
  
  #dump 뜨기 완료
  ```

  - `movies.json`

  ```python
  [
      {
          "model": "movies.movie",
          "pk": 1,
          "fields": {
              "title": "\uae00\ub798\uc2a4",
              "title_en": "Glass",
              "audience": 339707,
              "open_date": "2019-01-09",
              "genre": "\ub4dc\ub77c\ub9c8",
              "watch_grade": "15\uc138\uc774\uc0c1\uad00\ub78c\uac00",
              "score": 7.69,
              "poster_url": "https://movie-phinf.pstatic.net/20181227_126/1545900402100CiQHx_JPEG/movie_image.jpg",
              "description": "24\uac1c\uc758 \uc778\uaca9\u318d\uac15\ucca0 \uac19\uc740 \uc2e0\uccb4\u318d\ucc9c\uc7ac\uc801 \ub450\ub1cc \ud1b5\uc81c\ubd88\uac00\ud55c 24\ubc88\uc9f8 \uc778\uaca9 \ube44\uc2a4\ud2b8\ub97c \uae68\uc6b4 \ucf00\ube48, \uac15\ucca0 \uac19\uc740 \uc2e0\uccb4 \ub2a5\ub825\uc744 \uc9c0\ub2cc \uc758\ubb38\uc758 \ub0a8\uc790 \ub358, \ucc9c\uc7ac\uc801 \ub450\ub1cc\ub97c \uc9c0\ub2cc \ubbf8\uc2a4\ud130\ub9ac\ud55c \uc124\uacc4\uc790 \ubbf8\uc2a4\ud130 \uae00\ub798\uc2a4, \ub9c8\uce68\ub0b4 \uadf8\ub4e4\uc774 \ud55c \uc790\ub9ac\uc5d0 \ubaa8\uc774\uac8c \ub418\uace0 \uc774\ub4e4\uc758 \uc874\uc7ac\uac00 \uc138\uc0c1\uc5d0 \ub4dc\ub7ec\ub098\uba74\uc11c \uc608\uc0c1\uce58 \ubabb\ud55c \uc77c\uc774 \ubc8c\uc5b4\uc9c0\ub294\ub370..."
          }
      },
      {
          "model": "contenttypes.contenttype",
          "pk": 1,
          "fields": {
              "app_label": "movies",
              "model": "movie"
          }
      },
           
      .
      .
      .
          
      
      {
          "model": "auth.permission",
          "pk": 28,
          "fields": {
              "name": "Can view session",
              "content_type": 7,
              "codename": "view_session"
          }
      }
  ]
  ```

  

#### 2. 준비해둔 fixture 데이터들을 넣고 싶을 경우

- `csv`(Comma-Seperated Values)
  - 데이터들을 콤마(`,`)로 구분해서 비교적 간단한 텍스트 형태의 포맷으로 바꾼 형식
  - 스프레드시트, 엑셀에서 주로 활용한다 (데이터 크기 축소)

- `fixture` 는 장고가 데이터베이스에 import 할 수 있는 데이터의 모음

  - `json`,`xml`,`YAML` 포맷의 fixture들을 불러올 수있다.

- 장고에서 모델링 한 데이터가 어떻게 생겼는지 확인

  ```json
    {
          "model": "movies.movie",
          "pk": 12,
          "fields": {
              "title": "\ub0b4\uc548\uc758 \uadf8\ub188",
              "title_en": "The Dude in Me",
              "audience": 83244,
              "open_date": "2019-11-01T03:57:10.051Z",
              "genre": "\ud310\ud0c0\uc9c0",
              "watch_grade": "",
              "score": 8.0,
              "poster_url": "https://movie-phinf.pstatic.net/20190111_8/1547187739117rx7uW_JPEG/movie_image.jpg",
              "description": "\ub098 \ud604\uc815(\uc774\uc218\ubbfc)\uc744 \ub9cc\ub098\uac8c \ub418\ub294\ub370...?\ub300\uc720\uc7bc\uc758 \ud5a5\uc5f0, \ub10c \uc774\ubbf8 \uc6c3\uace0 \uc788\ub2e4!"
          }
      },
  ..
  }
  ```

  

- 프로젝트를 진행할 때 Seed Data(Initial Data)를 제공받았을 경우, Seed Data형식을 먼저 확인하고 형식에 맞게 모델링을 진행하자!
- Seed Data활용하는 방법 2가지
  	1. 애플리케이션의 데이터베이스를 하드코딩으로 미리 만든다. 이후dumpdata 명령어를 통해 fixture 데이터 형태로 만들어두고, 그 다음부턴 데이터베이스를 초기화시켜도 `loaddata` 명령어를 ㅗㅌㅇ해 다시 데이터를 불러와서 사용할 수 있다.
   	2. 이미 Seed Data를 제공받았을 경우, 그냥 `fixture`폴더에 넣어두고 불러와서 사용한다.
- `fixture`데이터 내용을 바꾸거나, 모델링해둔 내용을 바꾸고 싶으면 당연히 다시 `loaddata`과정을 거친다

### 3. 스프레드시트를 이용해서 csv파일로 빼기

#### 3.1 스프레드 시트를 이용해서 csv 파일로 빼기

- pk 추가 (Model과 같은 형식으로 구성해줌)
- 쉼표로 구분되는 csv 형식으로 저장한다

```
#google 스프레드시트

파일 - 다운로드 - 쉼표로 구분된 값(.csv, 현재 시트)
```

#### 3.2 fixtures 폴더 생성

 - fixtures 폴더를 생성하고, 위에서 생성한 csv 파일을 넣는다

   프로젝트 - app - fixtures - movies.csv

#### 3.3 csv2json -fixture

###### This script can be used to convert CSV data to Django fixtures JSON format.

	- csv2json-fixture 를 다운받아 movies.csv 파일을 넣는다
 - csv2json.py 의 내용변경 For 한글 인코딩 
   	- 87번 코드줄 : encoding=ENCODING `,` 추가
- csv2json.py 가 있는 곳에서 git bash 를 열어 csv 파일을 json 형식의 파일로 저장한다

```python
$ python csv2json.py movies.csv movies.Movie
```

   - 정상적으로 처리되었으면 

     		 - Converting movies.csv from CSV to JSON as movies.json 이라고 뜬다

- `movies.jsonv` 파일 생성을 확인한다 ( at `csv2json-fixture-master `폴더)

- fixtures  밑에 movies.json을 넣는다

- 데이터베이스에 데이터 넣는다

  ```shell
  $ python manage.py loaddata movies.json
  ```

  

### 4. 장고가 Fixture 파일을 찾는 방식

- 기본적으로 애플리케이션 안에 있는 `fixture`라는 디렉토리를 탐색한다
- 환경설정에 `FIXTURE_DIRS`옵션을 통해 장고가 바라보는 또다른 디렉토리를 정의할 수 있다
  - `loaddata`명령어를 수행할 때, 다른 경로보다 우선으로 탐색한다

```python
movies_pjt/
	config/
    movies/
    	fixtures/
        	movies.json
```





