### Telegram chat Bot

- BotFather 랑 인연 끊기
  - /deletebot
  - /dhjjang_bot - 도현짱 봇 삭제
  - Yex. I totally sure.



- BoFather 한테 봇 만들어달라 하기

  - /start
  - /newbot
  - dohyun (bot이름)
  - dohyyun_bot (username)
  - 

- 여기까지 하면 BotFather 가 <토큰> 값을 넘겨준다

- telegram api를 참고해서 메소드 활용방법을 찾는다

  - 요청URL + 내 토큰/getMe
  - 요청URL + 내 토큰/getUpdates
    - 이곳에서 id 번호를 알 수 있다



###### url로sendmsg하기

- sendMessage?chat_id=숫자&text=문자열

  - chat_id & text : (&) 파라미터랑 파라미터를 구분하는 역할

  - 기본 url ? 쿼리스트링 : (?) 쿼리스트링 비교

     

```python
from flask import Flask, render_template, request
from decouple import config
import requests
import random

app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = ' 토큰 값 '
chat_id =' id 값 '

requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')


```





### 토큰 숨기기

- 가상환경 진입
  - source ~/venv/Scripts/activate

- .env 직접 수정

  - vi. env

  - i ( insert 모드) 누르고 토큰값과 id 입력후 esc 2번 :wq( 저장하고 나가기)

- import decouble

  - decouple 에러나면 
    - pip install python-decouple
    - python -m pip install --upgrade pip 

  - 이래도 에러나면
    - deactivate (가상환경 나가기)
    - pip install python-decouple
    -  후 다시 가상환경 진입(source ~/venv/Scripts/activate)
  - 이래도 에러나면 그 상태에서
    - pip install requests 다시 설치



### ngrok 다운로드

- student 폴더에 넣고
- cmd 켜서
  - ngrok http 5000
  - ngrok 서버 실행 끝!
  - ngrok 설정
    - setWebhook?url=https://db3ead36.ngrok.io
    - /telegram 토큰 값



#### Pythonanywhere 서버로 배포하자!

- 회원가입
- create > Flask > python 3..7? 클릭
- Consoles > bash 클릭
  - pip3 install python-decoub
- Web > code > Go directory
  - .env 복붙
  - app.py 복붙

### 기존서버(egrok)를 없애고 pythonanywhere 서버로 연결하기

- /deleteWebhook
- /setWebhook
  - telegram url + /setWebhook?url=pythonanywhere url /telegram 토큰 값
- Reroad

- 이제 cmd창은 꺼도 된답니다^.^