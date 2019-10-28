from django.shortcuts import render
import random

# Create your views here.

# view 함수 -> 중간관리자
# 사용자가 접속해서 볼 페이지를 작성한다. 즉, 하나하나의 페이지를 'view'라고 부른다.
# 'view' 함수 내에서 사용자에게 보여줄 데이터 정보를 가공한다


def index(request):         # 첫번째 인자 반드시 request!
    return render(request, 'index.html')      # 첫번째 인자 반드시 request !

# 실습 1 : 템플릿 변수를 2개이상 넘겨서, 이름/나이/취미/특기 등 여러가지 정보를 표현해 보자

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

def dinner(request):
    menu = ['가라아게','통오징어구이','후토마키','모둠사시미','금태사시미']
    pick = random.choice(menu)

    #넘겨줄 변수가 2개 이상일 때
    context = {
        'pick' : pick
    }
    return render(request, 'dinner.html' , context)


# [기본]Lorem Picsum 사용해서 랜덤 이미지 보여주는 페이지 만들기!
# [추가실습] 동적 라우팅으로 이미지 너비, 높이를 받아서 이미지 출력하는 페이지!
def image(request,width,height): 
    number = random.randint(1,100)
  
    context = {
        'number' : number,
        'width' : width,
        'height' : height
    }
    return render(request, 'image.html',context)

#동적 라우팅
def hello(request, name):
    menu = ['가라아게','통오징어구이','후토마키','모둠사시미','금태사시미']
    pick = random.choice(menu)
    context = {
        'pick' : pick,
        'name' : name
        }
    return render(request, 'hello.html', context)

#실습 2 : 숫자 2개를 동적 라우팅으로 전달 받아서, 두 개의 숫자를 곱해주는 페이지를 만들자 !
def times(request,num1,num2):
    a = num1 * num2
    context ={
        'a' : a
    }
    return render(request, 'times.html',context)



#실습 3 : 반지름을 인자로 받아서 원의 넓이를 구해주는 페이지를 만들자
def area(request,num):
    b = num*num*3.14
    context ={
         'b': b
    }
    return render(request, 'area.html',context)