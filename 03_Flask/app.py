from flask import Flask,render_template, request

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


# end of file !!!!
# debug 모드를 활성화해서 서버 새로고침을 생략한다.
if __name__ == '__main__':
    app.run(debug=True)