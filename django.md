## django

- Dynamic Web Web Application program(Web APP)

웹서비스를 제작하는 두가지 방법

- A-Z 다 하기
-  프레임워크



### MTV

- Model  - M : 데이터를관리
- Template - T : 사용자가 보는 화면
- View - V : 중간 관리자



### Application 폴더구조

```
pages/
	admin.py
	apps.py
	models.py
	tests.py
	views.py
	
```

- admin.py
  - 관리자용 페이지를 커스터마이징 하는 파일
- app.py
  - 애플리케이션의 구성 정보가 담긴 파일
- models.py
  - 애플리케이션에서 사용하는 데이터베이스 정보가 담긴 파일
- test.py
  - 테스트 코드가 담긴 파일
- views.py
  - 사용자에게 보여줄 데이터를 가공하는 뷰 함수가 담긴 파일
  - Flask 에서 app.py 에 정의했던 함수가 담기는 장소



#### 코드 작성 순서 (권장) 

- views.py  : ﻿보여주고자 하는 페이지의 뷰 함수를 작성한다
- templates :  ﻿사용자에게 보여줄 템플릿 페이지를 작성한다
- urls.py  : ﻿ 해당 경로로 들어왔을 때 뷰 함수를 실행시킨다



## Django Template

### 템플릿 변수 ( Template Variable )

- 세번째 인자로 딕셔너리 형태 변수 넘겨주기



### 동적 라우팅( Variable Routing ) 

- 왜 동적 라우팅이 필요할까?



###### 실습 1 : 템플릿 변수를 2개이상 넘겨서, 이름/나이/취미/특기 등 여러가지 정보를 표현해 보자

```python
def introduce(request):
    name = '감자'
    age = '19'
    hobby = '감자깎기'
    good = '고구마깎기'

   
    context = {
        'name' : name,
        'age' : age,
        'hobby' : hobby,
        'good' : good
    }

    #render 메서드의 세번째 인자로 변수를 딕셔너리 형태로 넘길 수 있다.
    return render(request, 'introduce.html', context)
```



###### 실습 2 : 숫자 2개를 동적 라우팅으로 전달 받아서, 두 개의 숫자를 곱해주는 페이지를 만들자 !

`<views.py>`

```python
def times(request,num1,num2):
    a = num1 * num2
    context ={
        'a' : a
    }
    return render(request, 'times.html',context)
```

`<urls.py>`   :  url 을 통해 동적 라우팅으로 전달받을 수 있다

```python
path('times/<int:num1>/<int:num2>',views.times),
```



######  [추가실습] 동적 라우팅으로 이미지 너비, 높이를 받아서 이미지 출력하는 페이지!

`<views.py>`

```python
def image(request,width,height): 
    number = random.randint(1,100)
  
    context = {
        'number' : number,
        'width' : width,
        'height' : height
    }
    return render(request, 'image.html',context)
```

`<urls.py>`

```python
path('image/<str:width>/<str:height>/',views.image),
```

`<image.html>`

```html
<body>
 <h1>랜덤이미지</h1>
 <img src = "https://picsum.photos/id/{{number}}/{{width}}/{{height}}" alt = "picsum">
</body>
```

