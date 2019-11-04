### Django-CSV파일 불러오기

#### Seed Data(Initial Data) 입력하기

###### 우리가 애플리케이션을 제작할 때 미리 준비해둔 데이터 혹은 애플리케이션 테스트용 데이터가 필요한 경우가 있다. 이때, 데이터를 하드코딩으로 일일이 넣을 수도 있다. **하지만 `fixtures`라는 기능을 이용해서 준비해둔 데이터를 쉽게 데이터베이스에 넣을 수 있다.**



#### 1. 이미 데이터가 있을 경우

- `manage.py dumpdata > movies.json` 명령어를 통해서 현재 앱에서 가지고 있는 데이터를 빼낼 수 있다

  ```shell
  (가상환경 확인 후)
  $ python manage.py dumpdata > movies.json
  
  
  ```

  

- 이전 DB가 날아가더라도 `dumpdata`를 통해 빼둔 데이터들을 다시 한번 활용할 수 있다.

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



### 3. 장고가 Fixture 파일을 찾는 방식

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





