### Telegram

![](https://user-images.githubusercontent.com/52684457/61094753-71502d00-a48b-11e9-9fb1-fd6e840f28da.PNG)

telegram 에서 가장 밑에 Window/,Mac/Linux 클릭 후 다운



![capture42](https://user-images.githubusercontent.com/52684457/61094703-2df5be80-a48b-11e9-96ac-a138417210f4.PNG)

**@BotFather** 사용자를 찾기

![](https://user-images.githubusercontent.com/52684457/61094704-2df5be80-a48b-11e9-9f3c-9a383050d830.PNG)

![](https://user-images.githubusercontent.com/52684457/61094705-2df5be80-a48b-11e9-85fa-d27c8c00e57c.PNG)

시작-> /newname -> 사용할이름 -> 사용할이름_bot

그러면 나의 토큰 값을 보내준다.  (유출 조심!)
실행 될때마다 토큰값이 적용됨.



https://core.telegram.org/bots/api#authorizing-your-bot

페이지 내 아래에  정해진 메써드 네임이 있으니 잘 적용하면 됨.

![](https://user-images.githubusercontent.com/52684457/61110794-176b5980-a4c3-11e9-884a-2a9464cc7dc1.png)

```
https://api.telegram.org/bot나의_토큰_값/getMe
```

getUpdate - 봇이 자신이 받은 메세지 정보를 다 보여줌

sendMasssage - 봇이 보낸 메세지를 볼 수 있음



https://api.telegram.org/bot<token>/sendMessage?chat_id=<chat_id>&text=안녕하세요

```python
import requests

api_url = 'https://api.telegram.org'
token = '나의 토큰 값'
chat_id = 'chat_id'
text = '안녕하세요'

send_message = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

print(send_message.text)
```

**pip install python_decouple**

유출되면 위험한 코드들을 따로 숨김파일을 설정해서 ( **.env**) 코드가 유출되지 않도록 해주는 것.

```python
TELEGRAM_BOT_TOKEN='나의 토큰 값'
CHAT_ID='chat_id'
```







![](https://user-images.githubusercontent.com/52684457/61099053-0f4bf380-a49c-11e9-9f0a-5c00234905c5.png)

### **webhook**

Telegram 서버와 Flask서버, 우리가 Telegram에게 메세지를 보내면 응답하는 코드가 Flask에 있다. (Flask에 작성하고 있기 때문에.) 그래서 유저가 들어왔다고 전달해 줄 메세지를 Flask로 전송해주는 것이 **Webhook**.

Flask 서버에 유저가 말을 걸었다고 Telegram에서 전달 => 함수를 찾아 Flask가 특정 대답을 해주면 된다고 Telegram에 데이터를 전송.



**webhook 등록주소**

https://api.telegram.org/bot<token>/setWebhook?url=<ngrok-forwarding-http-url>/<token>

![capture52](https://user-images.githubusercontent.com/52684457/61099778-7ec2e280-a49e-11e9-8469-e61053f32e5f.png)

- 크롬에서 주소를 입력하면 연결이 된 것을 확인 가능하다. (**json**)
- 여기서 <ngrok-forwarding-http-url> 라는 값이 필요한데 ngrok을 이용면 된다.





### ngrok 

- 방화벽을 뚫어줘야 다른사람도 개인의 서버에 접근 가능 *(개방의 의미)*
- 로컬에 있는 주소를 밖으로 열어주는 것 => **ngrok** => 다른 여러 사용자들이 사용할 수 있게 만듦
- ngrok에서 가입을하면 유지 세션이 무제한, 비회원은 8시간



명령프롬포트 **=>** ngrok 실행 **=>** 사용자 폴더에 ngrok.exe를옮겨놓고 실행 시키는것이 편리하다.
                                                  ㅡ명령프롬포트를 켜면 위치 ~에서 시작되기 때문 (~가 사용자)
                                                  ㅡ사용자 파일에 들어가면 바탕화면, 사진, 문서 등의 파일이 있다.



**ngrok http 5000 + (enter)**

![](https://user-images.githubusercontent.com/52684457/61099052-0f4bf380-a49c-11e9-99bc-b982e16d4cfc.png)

500은 서버에러, 200은 연결 성공임을 알 수 있다.

![](https://user-images.githubusercontent.com/52684457/61099305-ccd6e680-a49c-11e9-8fe7-2a6b857e4d7e.png)

빨간 밑 줄이 쳐져있는 것이 우리가 필요한 <ngrok-forwarding-http-url> 값이다.

매번 켤 때 마다 바뀌니 서버를 연동중이라면 명령 프롬프트를 끄지 않는 것이 좋다.



```python
from flask import Flask, render_template, request 
import requests
from decouple import config

app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')



@app.route('/')
def hello():
    return 'Hi there!'

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('message')

    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

    return render_template('send.html')

@app.route(f'/{token}', methods=['POST'])
def telegram():
    # step 1. 데이터 구조 print 해보기
    print(request.get_json())
    from_telegram = request.get_json()

    if from_telegram.get('message') is not None:
        # step 2. 그대로 돌려보내기
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return '', 200
    # 200을넘겨야 200이란 값만 받기때문에 요청성공이 된다.
    # 아무주소나 받으면 안됨 => requests.get에서 {token}을 넣은 이유
```

request 와 request**s**는 다름!! => 구분 주의!! 

request는 **Flask**의 명령어
request**s**는 **Python**의 명령어



**requests.get** - 보내는 것

**requests.args.get** - 받는 것

**requests.post** - 코드가 새어나가지 않는 상태로 보내는 숨김 코드

get 코드는 보통 f('') (f string)으로 쪼개서 보낸다.

request.get의 get과 .get은 **다름**



```html
#write.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <from action="/send">
        <input type="text" name="message">
        <input type="submit" value="메세지 전송!">
    </from>
</body>
</html>
```

```html
#send.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>메세지가 성공적으로 전송되었습니다.</h1>
</body>
</html>
```



#### 네이버 파파고를 이용한 번역 Telegram

네이버 개발자 센터를 이용한다.

- papago API 사용 신청을 한 후, 특정 코드 값을 받는다. => 여기에도 **개인정보**

- 어떻게 사용해야 할지에 대한 내용이 담겨있다.

- NAVER_CLIENT_SECRET 번호는 한번만 발급이 되므로, 잃어버리면 재 발급 해야함

  

![](https://user-images.githubusercontent.com/52684457/61110131-80ea6880-a4c1-11e9-8b1a-61ba99b8f2fa.png)



```python
from flask import Flask, render_template, request 
import requests
from decouple import config

app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

@app.route('/')
def hello():
    return 'Hi there!'

@app.route(f'/{token}', methods=['POST'])
def telegram():
    # step 1. 데이터 구조 print 해보기
    # print(request.get_json())
    from_telegram = request.get_json()

    if from_telegram.get('message') is not None:
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')

        # 한글 키워드 받기

        #/번역 (띄어쓰기 한 칸 중요!)으로 입력이 시작된다면, 파파고로 번역이 동작한다.
        if text[0:4] == '/번역 ':
            headers = {
                # 네이버에서 주는 링크들과 아이디, 등은 개인의 중요 정보가 포함되어 있으므로, env대체 해준다.
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            data = {'source': 'ko', 'target': 'en', 'text': text [4:]}
            # requests.post를 쓰는 이유는 개인 정보가 담긴 headers와 data가 있기 때문이다. 왼쪽의 https:// 주소 아래로 코드가 들어가게 되어 드러나지 않게 한다.
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            # print(papago_res.json()) => 출력을 해서 json으로 이 구문에 대한 딕셔너리를 얻어낸다. 따로 정리해서 .get()을 좀더 쉽게 사용할 수 있다.
            # 여기서 왼쪽의 headers와 date는 네이버가 부여해준 각 코드, 오른쪽은 우리가 부여한 이름.
            
            text = papago_res.json().get('message').get('result').get('translatedText')


        # requests.get은 한 줄만 써주면 된다. 번역을 늘리고 싶으면 위의 if문을 복사해서 추가하면 된다.
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')


    return '', 200
```

'h'e'l'l'o'

0 1 2 3 4 5 

**A[0:2]** == 'hello' :

=> he

**A[3:]** == 'hello'

3 이후로의 모든 텍스트를 불러온다.

=> llo

###### json 코드 정리

```json
{
    'message': {
        '@type': 'response', 
        '@service': 'naverservice.nmt.proxy', 
        '@version': '1.0.0', 
        'result': {
            'srcLangType': 'ko', 
            'tarLangType': 'en', 
            'translatedText': 'apple'
        }
    }
}
```

```env
TELEGRAM_BOT_TOKEN='token'
CHAT_ID='chat_id'
NAVER_CLIENT_ID='naver_client_id'
NAVER_CLIENT_SECRET='naver_client_secret'
```

```python
        # 로또 당첨 봇

        if text[0:4] == '/로또 ':
            # 회차 번호를 받아온다.
            num = text[4:]
            # 동행 복권에 요청을 보내 응답을 받는다.
            res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
            # json 형태로 바꿔준다. 
            lotto = res.json()

        # 당첨번호 6개만 가져오기
        winner = []
        for i in range(1, 7):
            winner.append(lotto[f'drwtNo{i}'])
        bonus_num = lotto['bnusNo']
        text = f'로또 {num} 회차의 당첨 번호는 {winner}입니다. 보너스 번호는 {bonus_num}입니다.'




        # requests.get은 한 줄만 써주면 된다. 명령을 늘리고 싶으면 위의 if문을 복사해서 추가하면 됨
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

```



###### 배포(deploy) - pythonanywhere에 배포 작업을 할 것

Flask를 끄면 연결이 끊기기 때문에, Flask 서버를 죽지않는 곳으로 옮겨서 하루종일 서버가 돌아가도록 만드는 것.
flask run 할 필요 없이 항상 켜져있는 서비스를 사용 가능

=> ngrok을 사용했으나 이제 pythonanywhere에 연결해 죽지않는 서버가 생김. 이제 ngrok으로 연결한 명령프롬포트를 지우고, flask 서버를 끊어도 됨. 



(**주의!!** 아래의 **pythonanywhere서버로 연결하는 작업을 확인하기도 전**에 **끄면** **안됨!!!**)



######  ngrok서버를 끊는 방법

https://api.telegram.org/bot<token>/setWebhook?url=pythonanywhere.com/<token>

<ngrok-forwarding-http-url>가 들어있던 자리에 pythonanywhere_ID.pythonanywhere.com을 주소창에 입력해준다. pythonanywhere_ID 는 본인의 아이디. 

=>true라는 초록색 글씨가 뜨는 것을 확인하면 서버가 연결 되어있다. 



**pythonanywhere**의 files에서의 **/myfile/flask_app.py**를 눌러 안의 내용을 여태 작성한 Telegram_chat_bot.py내용을 그대로 **옮겨 붙이고 save**하면, **wdbhook에 연결되어 있는 이상**은 계속 열려있는 서버를 확인 할 수 있다. (files에 처음 들어가면 새로운 files를 만드는 메뉴가 나오는데,  flask3.7(현재 사용한 flask 버전)으로 설정해서 만든다.)



![](https://user-images.githubusercontent.com/52684457/61108449-454d9f80-a4bd-11e9-813b-05a0cda21a14.PNG)

files와 같이 상단의 **web**에서 Reload를 하는 것을 잊지 말자 => 그래야 **적용**이 됨.




