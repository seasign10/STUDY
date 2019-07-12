#### Lotto 추첨 만들기

###### Json (구글 크롬 확장자 설치)

- 특정 링크 소스를 읽어줌

![](https://user-images.githubusercontent.com/52684457/61094707-2e8e5500-a48b-11e9-9e58-e5e143b41e94.png)



```python
# 로또 회차 / 내 번호 입력 페이지 / 결과 페이지
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():                           
    return 'Hello World!'

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    # 회차 번호를 받아온다.
    num = request.args.get('num')
    # 동행복권에 요청을 보내 응답을 받는다.
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
    # json 형태로 바꿔준다. (우리가 크롬에서 보고있는 결과와 동일한 모습)
    lotto = res.json()

    # 당첨번호 6개만 가져오기
    winner = []
    # append가 리스트에 요소를 추가 해줌. 빈 [] 에 넣어줌
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])
    
    # 내 번호 리스트 만들기
    numbers = []
    for num in request.args.get('numbers').split():
        numbers.append(int(num))


    # 등수 가리기(몇 개 맞았는지 교집합이 필요)
    # 내 번호 요소를 뽑아서 당첨번호 리스트에 있는지 확인
    matched = 0
    # 예제)
    # winner = [1, 2, 3, 5, 8, 7]
    # my_number = ['1', '3', '22', '8', '12'] 하지만 서로 비교 될수 없음 (숫자와 문자열끼리x)
    # number = [1, 3, 22, 8, 12] 로바꿔서 비교해줌
    # 내 번호 리스트를 돌면서 / 뽑은 번호 하나하나가 각각 winner 리스트에 있는지 확인
    for num in numbers:
        if num in winner:
            matched += 1
    if matched == 6:
        result = '1등 입니다!'
    elif matched == 5:
        # 보너스 번호가 내 로또번호 리스트에 존재하면,
        if lotto['bnusNo'] in numbers:
            result = '2등 입니다!'
        else:
            result = '3등 입니다!'        
    elif matched == 4:
        result = '4등 입니다!'
    elif matched == 3:
        result = '5등 입니다!'
    else:
        result = '꽝 입니다!'

    return render_template('lotto_result.html',
                            winner=winner,
                            numbers=numbers,
                            result=result)

```

```html
#lotto_check.html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
    <h1>로또로또로또</h1>
    <form action="/lotto_result">
        로또회차 : <input type="number" name="num"><br>
        로또번호 : <input type="text" name="numbers"><br>
        <input type="submit" value="submit">
    </form>
</body>
</html>
```

```html
#lotto_result.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    당첨 번호 : {{ winner }}
    내 번호 : {{ numbers }}
    결과 : {{ result }}
</body>
</html>
```

숫자 사이 공백으로 처리해주는 작업 **.split**

```python
# set 집합 연산자로서, 합집합, 교집합, 차집합 연산을 할 수 있음.

matched = len(set(winner) & set(numbers))
# 쉽게 winner와 numbers를 비교 할 수 있음.

if len(numbers) == 6 # 으로 전제를 놓아야 함.
.elif
..elif
...elif
else:
    result = '번호의 수가 6개가 아닙니다.'
```

```python
    res = requests.get(f'https://www.dhlottery.co.kr/<token>common.do?
```

**token** : 신분증 악성 이용자가 아니라는것을 알려야 함. 특정 토큰이 있어야 접속 가능

int

string

list

dic

set

tuple

