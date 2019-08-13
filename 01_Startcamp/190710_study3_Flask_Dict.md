

> ### Python
>
> 
>
> ###### flask (플라스크)
>
> 마이크로 프레임 워크
>
> 용량이 작고 기초 이해에 도움이 됨 - 일일히 코드를 쳐야함
>
> 
>
> ###### Dyango (쟝고)
>
> 풀스텍 프레임 워크
>
> 자동화가 되어 더 편리 **But**, 원리와 결과 도출에 대한 이해도가 낮아 바로 실습하기 어려움
>
> 







## Flask

#### Flask를 이용하여 주소 뒤에 /ssafy붙이기 => This is ssafy 문구 나오기





```python
from flask import Flask, render_template, request
```

플라스크에 있는 플라스크, 랜더탬플릿, 리퀘스트를 불러오는 작업







```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'
    
from flask import Flask
app = Flask(__name__)

@app.route('/ssafy')
def hello():
    return 'This is ssafy'
```

**def** define 정의하다, 함수 값



![](https://user-images.githubusercontent.com/52684457/60954223-992f7b80-a339-11e9-839e-ec237621f4d7.png)

표시된  **install과 flask run**을 flask 터미널에 입력하지 않으면, flask라는 코드가 실행이 되지 않는다. 혹여나 두줄을 한꺼번에 복사 붙여넣기 하는 일은 없도록 하자.

```python
위의
def hello():
    return '페이지에서 표시될 말'
에서 ''안의 글을 바꾼 후 Ctrl+C로 서버를 끊고 flask run으로 다시 실행시켜주어야 바뀐 글이 수정이 되어 보인다.


*flask run을 입력할 시 아래에서 2번째줄 링크는 Ctrl+Lclisk 을 해줘야 열린다.
*여기서 들어간 flask서버는 개개인마다 서버가 달라서 남의 서버는 들어가지 못한다.
*hello는 대체되어도 상관없는 문자
*hello의 ()가 입력됨으로서 호출이라는 의미를 부여함

```





###### ~/.bash_profile** 파일을 만들기 (Debug mode를 on시켜 주기 위함)

```bash
export FLASK_APP=hello.py
export FLASK_ENV=development
```

**export(v)**띄고\_공백\_전혀_있으면\_안됨.

**ECV** environment의 약자, 환경 개발모드

**source ~/.bash_profile** 컴퓨터 전원을 재부팅 하듯이 배시를 다시 켜줌 (이 작업이 있어야 활성화 되는 작업들이 있다.) 위의 export작업들은 이 코드를 입력해줘야 제대로 적용이 된다.



![](https://user-images.githubusercontent.com/52684457/60954217-9896e500-a339-11e9-9c20-695e1d866129.png)

*하는 중에 오류가 나거나 제대로 실행이 되지 않는다면 **많은 터미널**을 사용하고 있지는 않은지 확인 할 것!

### Windows에서의 ~/.bash_profile 설정 시

![](https://user-images.githubusercontent.com/52684457/61018801-ffb4a800-a3d2-11e9-985f-6df57b01445d.PNG)

![](https://user-images.githubusercontent.com/52684457/61018802-004d3e80-a3d3-11e9-9fa2-1353e7c09e70.PNG)

앞에서 설정한 ~/.bash_profile은 버그가 많이 생기기 때문에 ~/.bashrc로 바꿔준다.



###### Flask를 연결 할 때에는 flask run 명령어를 입력하면 되고, 끊기 위해서는 Ctrl+C 키를 입력하면 된다.



#### variable routing (변수 라우팅)

```python
from flask import Flask, render_template
#플라스크에서 플라스크와 랜더 템플릿을 불러줘.
from datetime import datetime -> datetime.datetime.now 명령어를 단순화 시키기 위함

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'
# route 길을 열어줌


@app.route('/ssafy')
def ssafy():
    return 'This is SSAFY'
    
    
    
@app.route('/dday')
def dday():
    # 오늘 날짜
    today_time = datetime.now() => 현재 시간을 불러와줌
    # 수료 날짜
    endgame = datetime(2019, 11, 29)
    # 수료 날짜 - 오늘 날짜
    dday = endgame - today_time
    return f'{dday.days} 일 남았습니다.'



@app.route('/html')
def html():
    return '<h1>This is HTML TAG</h1>'



@app.route('/html_line')
def html_line():
    return """
    <h1>여러 줄을 보내 봅시다</h1>
    <ul>
        <li>1111</li>
        <li>2222</li>
    </ul>
    """


@app.route('/greeting/<name>')
#name이라는 값을 그대로 출력하고 싶을 때 => def xxx(): 에서 ()안에 값을 넣어줘야 함.
# @app.route('/greeting/<string:name>') 위 아래 같음
def greeting(name):
    return f'반갑습니다 {name}'
# f'' => f str => 따옴표 안에 있는 글을 전부 문자열로 인식. 변수값을 가지고 있는 출력 값은 {}를 사용



@app.route('/cube/<int:number>')
#int:문자열을 숫자로 인식하게 만들어줌 \<number> 문자열 \<int:number>숫자로 읽음 *꼭 number로 기입 안해도 됨.
def cube(number):
    return f'{number} 세제곱은 {number**3}입니다.'
#**제곱 *곱하기 /나누기


# # /lunch/몇명이 식사하는지 인원
# # 플라스크는 여러 메뉴 중에서 인원 수만큼의 메뉴를 응답합니다.
import random
@app.route('/lunch/<int:number>')
def lunch(number):
    menu = ['계란말이', '고등어 조림', '카레', '칼국수', '게장']
    lunch = random.sample(menu, number)
    return f'오늘의 점심은 {lunch}'
    #return str(lunch)를 해도 됨

```

<!DOCTYPE html>

```html

```



![](https://user-images.githubusercontent.com/52684457/61018806-017e6b80-a3d3-11e9-8687-d1ade6c13c02.PNG)





#### render template

여러문서들이 있음.  페이지를 넘겨주는 것. 우리(클라이언트)가 특정 페이지를 달라고 플라스크에 요청하면 플라스크에서 템플릿에서 페이지를 가져와서 작업하는것. 무수히 많은 페이지들중 하나를 매칭 시켜서 클라이언트에게 뿌려주는 것.

=> 템플릿을 랜더링 한다는 말을 씀.





**꼭 templates 라고 폴더를 작성해야 불러올수 있음**

![](https://user-images.githubusercontent.com/52684457/61021682-78b8fd00-a3dd-11e9-9760-c20803758b38.PNG)

template에 html문서를 작성 해주면 적용이 된다.

tamplate 파일은 app.py과 같은 위치로 지정하는게 좋다.





#### jinja2 활용

![](https://user-images.githubusercontent.com/52684457/61018807-02170200-a3d3-11e9-93e6-ea18f2291860.PNG)

홈페이지에 들어가면 진자 코드에 대한 설명을 볼 수 있다.



```python
from flask import Flask, render_template

@app.route('/greeting/<name>')
def greeting(name):
    return render_template('greeting.html', html_name=name)



#greeting.html

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <!-- 해인이라는 이름으로 값이 오면 인사하고 아니면 누구세요-->
    {# 여기안에 넣어야 주석 처리가 됨, (진자에서만) #}
    {% if html_name == '해인' %}
       <h2>{{ html_name }}아 왔니?</h2>
    {% else %}
       <h2>누구세요?</h2>
    {% endif %}
</body>
</html>
```

![](https://user-images.githubusercontent.com/52684457/61024171-b9b60f00-a3e7-11e9-92eb-2b71447051f5.png)





```python
from flask import Flask, render_template

@app.route('/cube/<int:number>')
def cube(number):
    #연산을 모두 끝내고 변수만 cube.html로 넘긴다.
    result = number**3
    return render_template('cube.html', result=result, number=number)



#cube.html

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    {{ number }}의 세제곱은 {{ result }}
</body>
</html>
```



```python

@app.route('/movie')
def movie():
    movies = ['어벤져스', '저스티스', '메이즈러너', '라라랜드', '위대한 쇼맨']
    return render_template('movie.html', movies=movies )


#movie.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>영화 목록</h1>
    <ol>
    {% for movie in movies %}
       <li>{{ movie }}</li>
    {% endfor %}
    </ol>
</body>
</html>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


```





**Jinja에서의 명령어는 또 다른 언어**임.

{% %}로 명령을 시작하면 {%end명령어%}로 닫아줘야함.

print를 사용 할 필요없이 바로 출력되지만, {}을 사용해서 명령을 실행하거나 리스트를 인식시킴

{{}}문자가 아닌 app.py 가 주는 코드값으로 인식함

- 계산은 서버(.py)에서 실행시키고, 출력은 탬플릿(.html)에서 => 계산은 서버에서 다 끝내야함. 출력만 탬플릿에서





### Flask Request & Response

이전 작업 처럼 url에서 받는게 아니라 특정 폼(form) 안에서 작성해서 넘겨주는 작업을 할것

```python
from flask import Flask, render_template, request
@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    # print(request.args)
    name = request.args.get('data') #ping에서 입력한 문자가 들어있음
    return render_template('pong.html', name=name)
```

**args** arguments의 약자. - request.arus.get(AAA)는 AAA에 관한 값을 다음페이지에서 불러올 수 있도록 하는 것.

여기서 name=name은 서로 같다는 뜻이 아님 (주의!) name을 name이라는 것으로 정해준 것이지 같지X

```html
>>ping.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="/pong">
        <input type="text" name="data">
        <input type="submit" value="버튼">
    </form>
</body>
</html>





>>pong.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>{{ name }} 받았음!!</h1>
</body>
</html>
```

위를 보면 pong에서 text를 받으려면 이름이 필요해서 text에 이름을 붙여야함. 
**=>** text라는 타입에 data라는 이름을 붙여 줌 **=>** data라는 상자에 text가 담겨서 pong으로 넘어가는 형식 

- 입력한 문자가 문자로 바로 넘어가는게 아니라 딕셔너리 형태 (키, 값)으로 넘어가서 키가 중요함!!



###### 실행 경로

ping **요청** -> ping.html **응답** -> pong으로 **요청** - > pong.html **응답**
요청과 응답의 반복



```html
  <input type="submit" value="버튼">

-> input:submit -> Tap키를 누르면 자동 완성되는 구문
```



#### fake naver / fake google



```python
@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

```



```html
>>naver.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>네이버 검색!!!</h1>
    <form action="https://search.naver.com/search.naver?" >
        <input type="text" name="query">
        <input type="submit" value="검색">
    </form>
</body>
</html>

{# query는 네이버의 일정한 값 #}







>>google.html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <h1>구글 검색!!!</h1>
        <form action="https://www.google.com/search?" >
            <input type="text" name="q">
            <input type="submit" value="검색">
        </form>
    </body>
    </html>

    {# 구글의 일정한 값은 q / action의 주소 ?은 생략해도 됨. 구분짓기 위한 도구일 뿐임. #}
```

> ###### 주소 값 따기
>
> ###### 
>
> ![](https://user-images.githubusercontent.com/52684457/61033195-e70db780-a3fd-11e9-92de-6125f0a825c3.PNG)
>
> 포털 사이트에서 문자를 검색 했을때 기본적으로 주소에서 첫번째로 나오는 '검색한 문자'를 포함한 뒤는 전부 잘라내도 주소에 영향이 없다. 
>
> 
>
> ![](https://user-images.githubusercontent.com/52684457/61033196-e70db780-a3fd-11e9-9b82-57b968fe1419.PNG)
>
> 그리고 그 값을 이용해서 FAKE사이트에서 검색을 했을때 
>
> 
>
> ![](https://user-images.githubusercontent.com/52684457/61033197-e70db780-a3fd-11e9-8df3-3b80ae2a0988.PNG)
>
> search?뒤의 문자가 상당히 생략 된 것을 볼 수 있는데, search?~뒤의 값도 필요 없다는걸 알 수 있다.
>
> 뒤에 붙은 q는 특정 사이트에 검색 값이란것 또한 알 수 있다.
>
> 





###### vonvon사이트와 같은 페이지 만들기

- 이름을 받을 페이지 + 결과가 나올 페이지 => 함수도 2개



나의 답 - 여기서 생략되어 있지만 flask에서 request를 불러오고 import random이 적용 되어있다.

```python
@app.route('/recieve')
def recieve():
    return render_template('recieve.html')


import random
@app.route('/print_answer')
def answer():
    name = request.args.get('data')
    past = ['부자집 고양이', '가난뱅이 머릿속의 이', '이루어질 수 없는 사랑의 줄리엣', '레고를 밟고 사망한 귀족']
    life = random.choice(past)
    return render_template('print_answer.html', life=life, name=name)

```

```html
>>recieve.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>이름을 입력하세요.</h1>
    <form action="/print_answer">
        <input type="text" name="data">
        <input type="submit" value="입력">
</body>
</html>
    
    
    
    

>>print_anwer.html
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>{{ name }}}님의 전생은 ... </h1>
    {{ life }} 였다!!!
</body>
</html>
```



선생님의 답

```python
@app.route('/godmademe')
def godmademe():
    name = request.args.get('name')
    first_list = ['잘생김', '못생김', '어중간한']
    second_list = ['자신감', '쑥스러움', '애교', '잘난척']
    third_list = ['허세', '돈복', '식욕', '물욕', '성욕']
    
    first = random.choice(first_list)
    second = random.choice(second_list)
    third = random.choice(third_list)
    
    return render_template('godmademe.html', name=name, first=first, second=second, third=third)
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>

<body>
  <h1>신이 {{ name }}님을 만들 때..</h1>
  <p>{{ first }} 한 스푼</p>
  <p>{{ second }} 두세 스푼</p>
  <p>{{ third }} 한 스ㅍ.. 으아아아아아아아악</p>
</body>

</html>
```



### Dictionary

리스트는 나중에가서 쓸일이 거의 없어지고, 딕셔너리의 중요도가 상당히 높아지기 때문에 **딕셔너리에 대한 이해도가 필요**하다.

딕셔너리를 작성 할 때, **인벤테이션(줄)을 잘 맞춰써야 한다**. 키벨류를 확실히 보기 위해 엔터를 권장한다. 반점 띄워쓰기로 잘 쓰지 않기는 하지만 엔터를 해야 더 확실하게 앞줄에 맞춰 쓰기 작업을 할 수 있기 때문.

```python
A = {
    a(키):(벨류)
    b:
    c:
} =>딕셔너리 닫음

딕셔너리⊂키⊂벨류 임을 알 수 있다.
```

###### 자세히

![](https://user-images.githubusercontent.com/52684457/61035317-eb3bd400-a401-11e9-888e-002da1cbe6dd.png)



```python
# 딕셔너리 만들기 -1
# 딕셔너리는 {}
lunch = {
  '중국집': '02-0000-0000'
}

# 딕셔너리 만들기 -2
# 1번 보기 보다 더 빨리 만들 수 있다.
dinner = dict(증국집='02', 일식집='031')


# 딕셔너리에 내용 추가하기
lunch['분식집'] = '031-123-1234'
print(lunch)

# 딕셔너리 내용 가져오기
idol = {
    'bts':{
        '지민': 25,
        'RM': 24,
    }
}

# RM 의 나이는?
idol['bts']['RM']
idol.get('bts').get('RM')

# idol의 key는 bts 하나, bts의 키는 지민과 RM 둘, 지민의 value는 25, RM은 24 
# get을 계속 연결 시켜 줌으로서 몇 겹을 들어가야 하는 키까지 들어갈 수 있다.
# 위의 딕셔너리에서 첫번째로 접근해야하는 bts를 넘겨서 bts안의 키인 지민과 RM까지 한꺼번에 들어갈 수 없다.



# dict["key"]로 존재하지 않는 key를 접근할 경우 key error가 발생하지만, dict.get('key')으로 존재하지 않는 key를 접근할 경우 None값을 넘겨준다

idol['exo']
# or
print(idol.get('exo'))

#차이점을 잘 아는 것이 중요. 아래 코드는 None이라는 값을 출력 함으로서 오류가 나지 않도록 해준다.

```

```python
# 딕셔너리 반복문 활용하기

lunch = {
  '중국집': '02-0000-0000',
  '분식집': '031-123-1234',
  '일식집': '02-987-6543'
}

# 기본 활용
for key in lunch:
    print(key)
    print(lunch[key])


# .items() 한방에 뽑아올 수 있음 key, value는 바뀌어도 되지만 통상적으로 저렇게 씀.
for key, value in lunch.items():
    print(key, value)

# value 만 가져오기 .values()
for value in lunch.values():
    print(value)

# key 만 가져오기 .keys()
for key in lunch.keys():
    print(key)
```



###### Dictionary의 응용 문제

```python
"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
scores = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

# total_score = 0 에서 시작,
total_score = 0

# for 문에서는 score.values()를 사용함으로서, score의 values값인 80, 90, 100을 전부 얻을 때까지 for문 명령이 반복되어 values값을 산출한다.
for subject_score in scores.values():
    # 0에서 시작한 total_score에서 80을 쌓고, 쌓인80에서 또 90을 쌓는 과정을 반복하는것을 아래식으로 정의
    total_score = total_score + subject_score
    # total_score += subject_score 위의 식과 동일, 너무 길어서 나온 식
    # 위의 식을 만듦으로서 for문이 반복되는 동안 같이 식을 반복하고 total_score은 점점 산출된 values값 만큼 더해지는 값이 된다. 
    
#최종적으로 나온 total_score을 아래의 식처럼 나누기 3을하면 평균 점수가 나오는 것이다.
avg_score = total_score / 3
#avg_score = total_score / len(socres) => length은 길이. 해당 "Key의 갯수"만큼 설정 됨. => '수학', '국어', '음악' 총3개
print(avg_score)



# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')

total_score = 0
count = 0
# for 문을 카운트 하기 위해 만듦

for person_score in scores.values():
    for indivisual_score in person_score.values():
        total_score = total_score + indivisual_score
        count = count + 1

avg_score = total_score / count
print(avg_score)




# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# value가 list임
for name, temp in city.items():
    # name = 서울
    # temp = [-6, -10, 5] len(temp) => 3
    avg_temp = sum(temp) / len(temp)
    print(f'{name} : {avg_temp:.1f}')
    # .1f => 소수점 하나만 출력하겠다. - 찾아서 씀 외우기 x




# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

# for을 첫번째로 돌 때, 기준 지역, 기준 온도 : 서울
# 두번째 for문이 들어왔을 때, 서울과 비교하게 될 것.
# 첫 for문 때 서울이 가장 온도가 높은 곳은 서울 이었다가 2번째 3번째 for문이 계속 돌면서 가장 높은 온도인 지역으로 값을 갈아치움

count = 0
for name, temp in city.items():
    # 첫 번째 시행 때
    # name = '서울'
    # temp = [-6, -10, 5]
    # 계속 갈아치우는게 아닌 비교한 다음에 갈아 치우는 코드가 필요하기 때문에 단 한번만 실행되는 조건이 필요함.
    if count == 0:
        # count가 0일 때만 도는 코드
        hot_temp = max(temp)
        cold_temp = min(temp)
        got_sity = name
        cold_city = name
    else:
        # 계속 돌지 않고 else문 안에서만 돌것, 기준점은 서울로 했기 때문에 서로 비교만 되면 끝날 것.
        # 최저 온도가 cold_temp 보다 낮으면, cold_temp 에 값을 넣는다.
        if min(temp) < cold_temp:
            cold_temp = min(temp)
            cold_city = name

        #서울 끝나고 이제 대전값 도는중. 이 조건이 만족되면 name에 대전으로 갈아 치워지고 만족하지 못하면 서울 그대로.
        # 최고 온도가 hot_temp 보다 높으면, hot_tem 에 값을 새로 넣는다.
        if max(temp) > hot_temp:
            hot_temp = max(temp)
            hot_city = name
    count += 1

print(f'최고로 더웠던 지역은{hot_city}이고 온도{hot_temp}도 였고 최고로 추웠던 지역은 {cold_city}이고 온도{cold_temp}도 였다. ' )



# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
# = 서울 온도 리스트에 2가 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
if 2 in city['서울']:
    print('네 있어요')
else:
    print('아니요 없어요')
```

```python
ssafy = {
    'location': ['서울', '대전', '구미', '광주'],
    'language': {
        'python': {
            'python standard library': ['os', 'random', 'webbrowser'],
            'frameworks': {
                'flask': 'micro',
                'django': 'full-functioning'
            },
            'data_science': ['numpy', 'pandas', 'scipy', 'sklearn'],
            'scraping': ['requests', 'bs4'],
        },
        'web' : ['HTML', 'CSS']
    },
    'classes': {
        'dj': {
            'lecturer': 'harry',
            'manager': '노구하',
            'class president': '박나율',
            'groups': {
                'A': ['이길현', '우동균', '이승현', '이가경', '이병재'],
                'B': ['차진권', '박성진', '심규현', '남승현'],
                'C': ['신승호', '조현호', '이병주', '박홍은'],
                'D': ['조규홍', '조수지', '임소희', '이해인'],
                'E': ['박상원', '고병권', '김준호', '신정우', '박나율']
            }
        },
        'gj': {
            'lecturer': 'change',
            'manager': 'pro-gj'
        }
    }
}


"""
난이도* 1. 지역(location)은 몇 개 있나요?
출력예시)
4
"""
# 해당 value에 대한 len이 필요함 => 즉 value값도 필요
loc = len(ssafy.get('location'))
print(loc)
#or
print(len(ssafy['location']))

# => get.()을 []로 대체해서 쓸 수 있음.

"""
난이도** 2. python standard library에 'requests'가 있나요?
출력예시)
False
"""
if 'requests' in ssafy.get('language').get('python').get('python standard library'):
    print(True)
else:
    print(False)

#or

print('requests' in ssafy['language']['python']['python standard library'])

"""
난이도** 3. dj 반의 반장의 이름을 출력하세요.
출력예시)
박나율
"""

print(ssafy['classes']['dj']['class president'])

"""
난이도*** 4. ssafy에서 배우는 언어들을 출력하세요.
출력 예시)
python
web
"""

for lang in ssafy['language'].keys():
    print(lang)

"""
난이도*** 5 ssafy gj반의 강사와 매니저의 이름을 출력하세요.
출력 예시)
change
pro-gj
"""

for name in ssafy['classes']['gj'].values():
    print(name)

"""
난이도***** 6. framework 들의 이름과 설명을 다음과 같이 출력하세요.
출력 예시)
flask는 micro이다.
django는 full-functioning이다.
"""
#key value, key value를 뽑는거라 .items를 사용해야함
for name, attr in ssafy['language']['python']['frameworks'].items():
    print(f'{name}는 {attr}이다.')

# arrt은 attribution의 약자

"""
난이도***** 7. 오늘 당번을 뽑기 위해 groups의 E 그룹에서 한명을 랜덤으로 뽑아주세요.
출력예시)
오늘의 당번은 김준호
"""
# E의 벨류 값이 필요함
import random
lucky = random.choice(ssafy['classes']['dj']['groups']['E'])
print(lucky)
```





