from flask import Flask,render_template, request
import random, requests
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/dohyeon')
def dohyeon():
    return '저는 무술가 입니다!'

@app.route('/html')
def html():
    return '<h1>태그 사용할 수 있어요!</h1>'

@app.route('/html_multiline')
def html_multiline():
    return """
    <ol>
        <li>ㅎㅇㅎㅇ</li>
        <li>ㅇㅎㅇㅎ</li>
    </ol>    
    """

# 동적 라우팅 (Variable Routing)
@app.route('/greeting/<string:name>')
def greeting(name):
    #return f'안녕, {name}?'
    return render_template('greeting.html', html_name = name)


@app.route('/cube/<int:number>')
def cube(number):
    # oea = str(number*number*number)
    # return oea
    result = number ** 3
    return render_template('cube.html',result=result,number=number)

@app.route('/movies')
def movies():
    movie_list = ['82년생 김지영','조커','엔드게임','궁예']
    return render_template('movies.html',movies=movie_list)

# ping : 사용자로부터 입력을 받을 Form 페이지를 넘겨준다.
@app.route('/ping')
def ping():
    return render_template('ping.html')

#pong : 사용자로부터 Form 데이터를 전달받아서 가공한다
@app.route('/pong')
def pong():
    user_name = request.args.get('user_name')
    return render_template('pong.html' , user_name=user_name)


# fate naver
@app.route('/naver')
def naver():
    return render_template('naver.html')


# fate google
@app.route('/google')
def google():
    return render_template('google.html')

#사용자로부터 이름을 입력받을 Form 페이지
@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

#전달받은 이름을 기준으로 넘겨줄 각종 정보를 가공해서 돌려주는 (응답)로직
@app.route('/godmademe')
def godmademe():
    #1. 사용자가 입력한 데이터를 가져온다 (Flask의 request 기능 사용)
    user_name = request.args.get('user_name')
    #2. 사용자에게 보여줄 각종 여러가지 재밌는 특성들을 보여준다
    first_list = ['병아리','강아지','고양이','조각남','강다니엘']
    second_list =['마동석','정우성','권상우','메기','꼴뚜기','넙치','황민승','서혁진','오징어']
    third_list = ['마동석','정우성','권상우','메기','꼴뚜기','넙치','황민승','서혁진','오징어']
    #3. 리스트에서 랜덤으로 하나씩을 선택한다. 
    first = random.choice(first_list)
    second = random.choice(second_list)
    third =  random.choice(third_list)

    #4. 가공한 정보를 템플릿에 담아서 사용자에게 보여준다.
    return render_template('godmademe.html', user_name=user_name, first_html=first, second_html=second, third_html=third)



# 1. 사용자로부터 일정한 텍스트를 입력 받아서, 아스키 아트로 변환해서 돌려준다.
# 이때, 아스키 아트 폰트는 랜덤으로 하나를 지정해서 변환한다.

@app.route('/catch')
def catch():
    return render_template('catch.html')

@app.route('/result')
def result():
    #1. 사용자가 입력한 Form 데이터를 가져온다
    word =  request.args.get('word')
    #2. ASCII API 로 요청을 보내서 응답 결과를 변수에 담는다 (폰트 정보를)
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text 
    #3. 가져온 폰트들을 리스트 형태로 바꾼다    
    fonts= fonts.split('\n')
    #4. 폰트 하나를 랜덤으로 선택한다
    font=random.choice(fonts) 
    #5. 사용자가 입력한 단어와 랜덤으로 선택한 폰트 정보를 API에게 요청한다
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    #6. 최종 결과물을 사용자에게 돌려준다.
    return render_template('result.html', result=result)


# end of file !!!!
# debug 모드를 활성화해서 서버 새로고침을 생략한다.
if __name__ == '__main__':
    app.run(debug=True)