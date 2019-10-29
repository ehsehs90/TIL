from django.shortcuts import render
import random
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

# 정보를 던져줄 페이지
def throw(request):
    return render(request, 'throw.html')
# 사용자로부터 정보를 받아서 다시 던져줄 페이지
def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    return render(request, 'catch.html', context)
#아스키 아티 ASCII ARTII
#사용자로부터 텍스트 입력받는 페이지
def art(request):
     
    return render(request,'art.html')
 
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
    return render(request, 'result.html', {'result':result})


#회원가입 폼을 보여주는 페이지
def user_new(request):
    return render(request,'user_new.html' )
#회원가입 요청을 처리하는 페이지(로직)
def user_create(request):
    user_id = request.POST.get('user_id')
    user_pwd = request.POST.get('user_pwd')
    context = {
        'user_id' : user_id,
        'user_pwd' : user_pwd,
    }
    return render(request, 'user_create.html',context)


def static_sample(request):
    return render(request, 'static_sample.html')