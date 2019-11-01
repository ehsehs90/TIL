## 2019 -10-31 (목) 전생직업 APP

###### Faker API 를 활용한 전생직업 App을 만들어보자



### [flow]

<1. 사전 작업>

	- Faker API 사용법 익히기 -> Shell Plus  이용
	-  `jobs` Application 생성

```shell
$ python manage.py startapp student
	- setting.py에 출생신고
	- student 디렉토리에 urls.py 파일 생성 / urls작성 (import 주의)
	- config > urls.py 에 student 앱 경로 바인딩 (import 주의)
	- `Template` 에 student 디렉토리 생성
    - student > models.py 모델 생성
$ python manage.py makemigration
$ python manage.py migrate
$ python manage.py shell
	from student.models import Student
	데이터 등록 student = Studnet()
	student.title = '이도현'
	student.content = '마크다운'
	student.save()
	exit()
Ctrl +Shift + p
open database > sqlite3 : 내가 작업하는 디렉토리 선택
아까 migrate 한 모델Table 잘 있는지 확인
student > view.py (앞으로 student 모델 객체 사용하려면 `임포트` 꼭!)

```







<2. 기능 구현>

- 사용자 이름을 입력받는 함수 (HTML Form 을 통해 건네줌)

  [기본]

   - 이름에 따라 전생의 직업을 알려주는 함수

     - Faker API 를 통해 직업 정보 가져오기

     - 해당 이름을 처음 조회할 때 이름 - 직업정보를 DB에 저장

       즉, 이름을 여러번 조회하더라도 처음 저장된 직업이 바뀌지 않음

  [심화]

  - GIPHY API 를 사용해서 직업에 따른 움짤도 함께 보여주기
  - GIPHY API 회원가입 & API KEY 발급 바딕
    - 공식 문서 보며 요청 보내서 움짤 받아보기
      - 사전에 주소창에 URL + 쿼리 스트링 직접 넣어보면서 사진 정보가 잘 오는지 먼저 테스트하기
  
  ​     
  
  