[TOC]

# 기본 정보

>##### API (어플리케이션 프로그래밍 인터페이스)
>
>**ex) 페이스북 로그인, 카카오톡, 네이버 지도, Riot(롤), 공공데이터API*
>
>*주소 (Url) 요청 -> 문서 (Xml...) 제공*



> **오픈소스-누구나 열람하고, 규정만 지키면 사용할 수 있는 소스**

##### 

>######  CLI(commend line interface) 명령 줄 인터페이스 
>
>종류
>1.유닉스 쉘
>2.CP/M
>3.DOS
>4.etc...

##### 

>윈도우 - 독자적이라서 프로그래밍 하기 어려움. (명령어도 다르고 복잡)
>
>-종류-
>윈도우즈
>리눅스
>유닉스 - 애플 라인







# Typora 사용법

#(v)글자h1 ->가장 큰 글씨

###### Ctrl+

> i - 기울기 * *
> b - 굵기 ** **
> (숫자) -크기

```Typora
>주석 달기

​```(v)파이썬, 자바 등 쓰기 -> 맞는 코드 적용 됨

``사이에 코드 넣기

[링크달기]+(주소)

ctrl+/ - 마크다운 실제 모습과 아웃풋의 전환

-(하이푼) -> 탭+엔터 이어서 

[TOC]+(enter)인덱스 만들어 줌

(enter)연타 해당 주석에서 벗어남

![]( 이미지 넣기 )
-> 이미지 사진을 넣을 때 타 컴퓨터에서 이미지를 불러 오면 또 다른 컴퓨터에서는 읽지 못한다. ->

Shift + enter -> 바로 밑단에 이어쓰기

Ctrl + z 되돌아 가기
Ctrl + y 되돌아 가기 취소

\(역슬래시) * - 등 역할로서 사라지는 문자들의 역할을 지우고 문자 자체로만 존재하게함
ex)\- => -
```



# 필요 파일 설치

```install
bash 설치하기
1. git bash (git for windows)

2.python 3.7.3(최신버전) (PATH 클릭)

3.visual studio code - 기본 ->windows
ctrl+shift+P -> defalt shell -> git bash로 선택하면 기본 터미널로 정해짐

```

![](https://user-images.githubusercontent.com/52684457/64659222-82aabb00-d475-11e9-9194-42120f25cc01.png)

- 자신의 컴퓨터 사양에 맞게 설치하는 것이 좋다. 
  *현재 img : windows 64비트*</u>

#### ++ 알고리즘 수업때의 글로벌 (파이썬 3.5.ver)

3.7.3버전과 번갈아 사용하기 위해서 하는 작업. 서로 독립적인 존재. (install 등 서로 개별, class와 instance개념을 생각하면 쉬움.)

![](https://user-images.githubusercontent.com/52684457/61937482-ec582e00-afc9-11e9-818b-753aca658b9a.JPG)

파이썬 3.5.ver 이상의 컴퓨터에서 3.7.3을 깐 상태 (환경 변수에서 3.7.3버전을 3.5보다 우선시로 올려준 상태)이기 때문에 버전을 확인해보면 3.7.3이 뜬다. 

venv라는 환경 변수를 입력하면 3.7.3을 켤수 있도록 설정 하는 방법이다. 3.7.3이라고 폴더명을 안해도 되지만 헷갈리지 않도록 하기 위해서 3.7.3이라 입력해준다.



![](https://user-images.githubusercontent.com/52684457/61937484-ecf0c480-afc9-11e9-91c8-9672755cd423.JPG)

설정이 끝나면 환경변수에서 3.5아래로  3.7.3의 위치를 내려준다. 

전부 확인을 하고, 다른 git bash가 켜져있는지 꼭 확인! 켜져있다면 꼭 꺼주도록 하자!

![](https://user-images.githubusercontent.com/52684457/61937485-ecf0c480-afc9-11e9-966b-77446ee77b98.JPG)

deacrivate를 입력하면 venv라는 환경변수를 끌 수있다.



# 파이썬(PYTHON)

### *프로그래밍 언어 3방식

1) 저장 =

2) 조건 if elif else

3) 반복 While, for i in (i- 대체 가능)



### *명령문

```python
#주석 달기 (명령 문이 적용 되지 않음)

A=0 (A에 0을 적용 시킨다, '저장'의 개념) / A==0 (A는 0이다) 

_(언더바)는 단어를 이어 붙일 때 사용 (ex.sample_number)

print() - 해당 x를 출력 / print('') - ''안의 내용을 출력

기본적으로 프로그래밍의 번호는 0부터 시작함

*네이밍 할 때 주의할 점
00으로 시작해야 1다음에 11로 순서 얽힐 일이 없다.

대문자 소문자를 확실히 구별할것, 그리고 코드 내에서는 최대한 영어만 사용한다. (오류가 날 가능성을 낮춰줌)

함수 이름은 신중히 지어주는 것이 좋다. (누가 봐도 알아 볼 수 있는 이름이 최상)

Ctrl+S 저장버튼 습관화 하는게 좋다. 제대로 저장하지 않으면 실행이 제대로 되지 않음.

(url + xx) - 합칠 수 있음.

mk - 만들기
mkdir - 디렉토리(폴더) 만들기

""(더블 쿼트)보다 ''(싱글 쿼트)를 습관 들이는게 좋음

-

뒤로가기
$cd ..

최상위 (루트) 디렉토리로 이동
$cd /

사용자의 홈 디렉토리로 이동
$cd ~

사용자의 Desktop(바탕화면) 디렉토리로 이동
$cd ~/Desktop

사용자의 Desktop의 A폴더로 이동
$cd Desktop/A

사용자의 현재 위치
$cd .

숨김파일이나 폴더를 보여줌
$ls -al

리스트를 보여줌
$ls 

가장 중요한것!!!)))) 자신이 늘 어느 위치 에서 터미널을 실행시키고 있는지 알아야 함!!
```



> #### While True:
>
> False가 될때 까지 반복
>
> ***ex*)**
> n=0
> While n <숫자:
>     print('')
>     n=n+1

> #### for i in:
>
> i - 아무의미가 x
> 정해진 범위 안에서 반복
>
> ***ex*)**
> for i in range(숫자):
>  print('')
>
> *for i in a **=>** a에 대한  i가 나올때 까지 i에 대해 반복 **=>** i가  for문의 값이 됨 **=>** a에 대한값 i *

#### 사용빈도 : for i in > While True



> #### random. (큰 개념, 모듈)
>
> ramdom.choice
>
> - 리스트에서 특정 요소 하나를 임의적으로 추출(리스트) -단일 선택
>
> random.sample(리스트, 개수)
>
> - 리스트에서 특정 수의 요소를 임의적으로 비복원 추출 (갯수 제한x)



```python
예시문)))

import random - 함수가 포함된 코드를 불러온다.
aaaa = ['a', 'b', 'c'] - 리스트를 만든다.
bbbb = random.choice(aaaa) - 함수를 통해 저장값을 만든다. 여기서 aaaa는 리스트
print(bbbb) - 그리고 출력
cccc = {
  'a':'A',
  'b':'B',
  'c':'C'
} - 딕셔너리{} 접근,딕셔너리 중괄호 닫을 시에는 중괄호 처음 열었을때의 문자열과 똑같이 맞춰 닫아야 해당 코드를 맞춰 해석한다.
print(cccc[bbbb])

(출력 결과)
aA 또는 bB 또는 cC
음식점 이름 + 음식점 번호 -> 이런 식으로 응용 가능

# 여러 종류를 값을 낼 때에는 random.sample(리스트, 개수) 개수는 숫자가 들어가는 자리.





예시문)))

1~45까지의 수를 일일히 적기 -> 비효율
aaaa = range(1,46)
를 이용하면 간편, range는 마지막 숫자에서 하나를 빼기 때문에 n+1로 해야함

ex) 1~45사이의 무작위 숫자 6을 출력
import random
number=range(1,46) - number을 정의
lotto=random.sample(number,6) - number사이 6개 숫자를 lotto로 정의
print(lotto)

(출력 결과)
1~45사이의 n수가 6가지 출력이 된다.
```





```python
예시문)

1) 식당메뉴 저장하기
menu = ['새마을식당', '순남시레기', '롯데리아', '일당감자탕', '성심당']
print(menu)



2) 미세먼지 값 범위 조정하기
if dust>150:
    print('매우 나쁨')
elif 80<dust<=150:
    print('나쁨')
elif 30<dust and dust<=80: / or을 쓰면 조건을 만족x
    print('보통')
else:
    print('좋음')
```



#### 사이트 열기

```python
>>>import webbrowser
>>>webbrowser.open('주소')
->열림

opne()
open_new() - 새로운 창을 엶
opne_new_tap()

point!) 반복문을 사용하면 여러 창을 띄울 수 있다!
```



#### 사이트의 인기 검색어 뽑기

```python
import requests
from  bs4 import BeautifulSoup

url = 'https://www.naver.com/' -> 깔끔하게 html을 정리 할 수 있음
html = requests.get(url).text -> 문서를 정리 요청
soup = BeautifulSoup(html, 'html.parser')
search = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')
for i in search:
    print(i.text)
    
    
-

.select_one('경로')
.select('경로') 리스트를 뽑아냄
.text - 소스를 빼고 텍스트만 뽑아냄
    
여기서) 크롤링 할 때 - (인기 검색어)
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(4) > a > span.ah_k

#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(9) > a > span.ah_k

중복되는 단어를 잘 살펴봐야 한다.

Ctrl+Shift+i ->크롬 개발자 도구
```



### 문자열(string) 삽입

```python
#과거
'%s %s' % ('one', 'two')

#pyfotmat(ver.~3.5)
'{}, {}, {}'.format('one', 'two', 'three')

#f-string(new in 3.6)
a = 'one'
b = 'two'
print(f'{a}, {b}')
->f는 format의 약자

예시)
name = '이해인'
print(f'안녕하세요, {name}입니다.')

예시))
name = '이해인'
print(f'안녕하세요, {name}입니다.')

점심 메뉴 추천
import random
menu = ['초밥', '돈까스', '양고기']
lunch = random.choice(menu)
print(f'오늘의 저녁은 {lunch}입니다.')

로또 추천
import random
numbers = range(1, 46)
lotto = random.sample(numbers, 6)
print(f'오늘의 당첨 번호는 {lotto}입니다.')

name = '이해인'
print(f'안녕하세요,' + name + '입니다.')
```



### 파일명 바꾸기

```python
import os
# 1. 해당 파일들이 있는 위치로 이동
os.chdir(r'C:\Users\student\Desktop\TIL\00_startcamp\02_day\change_filenames')
->\(역슬래쉬) - 그대로 내보내는 기능. 바로 앞에 쓰면 바로 뒷자리 문자가 기능을 하지 않고 그대로 출력
  (ex. \"안녕\" - "안녕")
-> 여기서 r은 역슬래쉬의 기능을 국한시킨다. (윈도우즈에만 해당되는 명령 코드)
   
# 2. 폴더 안에 모든 파일 이름을 수집
filenames = os.listdir('.') -> 이미 현재 위치에 있기 때문에 .으로 입력
print(filenames)

# 3-1). 각각의 파일명을 돌면서 수정한다.
 for filename in filenames:
     os.rename(filename, f'samsung_{filename}') -> os.rename(이전 파일/수정 후 파일)

# 3-2). samsung을 ssafy로 변환 (이미 입력한 이름을 수정 할 때)
for filename in filenames:
    os.rename(filename, filename.replace('samsung_', 'ssafy_'))
```



### 500개 무작위 이름의 텍스트 파일 만들기

```python
import os
import random

family = ['김','이','박','최','황','오','강','한','제갈','하','정','송','현','손','조']
given = ['길동','준','민준','소미','수진','지은','동해','민태','준호','세정','지훈','성우','성원']

for i in range(500):
    cmd = f"touch {i+1}_{random.choice(family)}{random.choice(given)}.txt"
    print(cmd)
    os.system(cmd)
```





# Visual  Studio Code

확장자 설치해야 함 - Python - install



윗창으로 코드 만들고, 아래 터미널에서 해당 파일로 이동(cd) 후 해당 파일(.py) 실행

해당 폴더 -> 우클릭(깃베스) -> code 해당파일.py 
비쥬얼 스튜디어 코드로 열림



### *명령문

> ctrl+shift+X -> 확장자 설치 (파이썬 인스톨)
>
> ctrl+shift+P -> 검색창
>
> ctrl+/ -> 주석처리
>
> ctrl+` -> 터미널(bash) 껐다 켜기
>
> ctrl+s 코드저장 (습관화 필요)
> 저장안되면 o라고 떠있고 저장되면 x라고 뜸.
>
> **git bash**에서 -> code 파일이름.(형식) - ex) code A.py 파이썬 형식으로 생성



### *Install

> ###### pip install requst
>
> request.get('주소') -> 주소에 요청을 보내서 응답을 받음
>
> request.get('주소').text -> 주소에 대한 텍스트
>
> request.get('주소').status_code
>
> ***http status code***
> 200->성공
> 404->페이지x (요청 오류)
> 500->서버의 에러
>
> **pip install bs4** (bs4를 전체 설치)
> or
> import requests -> soup = bs4.BeautifulSoup 이렇게 불러 주어야 함.
> from bs4 import BeautifulSoup *(bs4중 BeautofulSoup만 설치) * -> soup = BeautifulSoup()
>
> BeatifulSoup (문서, 타입)
> 받은 문서를 보기좋게 만들어주는 것



#### 확장자

terminal here -> install
검색창에서 preferences: Open Keyboard Shortcut -> 키보드 모양 클릭해서 Ctrl + `(백쿼트)

- 나온 키 값 지우고 terminal here을 검색해서 추가

=>**Ctrl + ` 사용하면 해당 파일의 위치에서 터미널을 열어줌**



###### 이 외 추천 확장자

![image](https://user-images.githubusercontent.com/52684457/65212379-d2742c80-dadc-11e9-9214-bc6034c66436.png)

- 코드를 이미지로 깔끔하게 저장이 가능하다.

# GIT BASH

1. 해당 폴더에서 git bash를 우클릭으로 실행 'git bash here'

2. code 만들파일_이름.py + (enter)

3. Visual Studio Code가 열림

### *명령문

>**ls** 현재 디렉토리의 내용들을 나열
>**cd** 체인지 디렉토리 현재 작업하는 디렉토리(위치, 폴더)를 변경
>**mkdir** 메이크 디렉토리 새로운 디렉토리 생성
>**echo** 문자열 출력 > 파이썬의 print와 유사
>**rm** 리무브, 파일을 지우는 것
>**exit** 터미널 종료 
>
>**ctrl+L** - clear 지우기
>철자 몇개 치고 tab을 누르면 자동완성
>
>**파일이름 -V** 버전
>
>**git pull** - 수정된 사항만 불러오기
>
>**git remote -v** 현재 폴더에 연결된 레파지토리를 확인 할 수 있음 + 레파지토리를 연결 할 때 쓰는 명령어
>
>**touch**  vs코드로 열고싶지 않고 바로 만들고 싶을때
>
>**q** 응답이 너무 길어서 작동하지 않을때
>
>**rm** **-rf .git** git을 지우는 것
>
>**-f** git push -f 강제푸쉬



# GIT

#### (분산)버전 관리 시스템

코드의 History를 관리하는 도구.

개발된 과정과 역사를 볼 수 있으며,

프로젝트의 이전 버전을 복원하고 변경 사항을 비교, 분석 및 병합도 가능

**차이가 무엇이고 이유를 남길 수 있다. 작은 차이점만 저장해서 용량을 최소한으로 줄이고 언제든지 복원 할 수 있다.**

> 유닉스가 14일만에 만듦 GIT HUB와는 연관이 없으며 깃허브는 GIT의 오픈소스를 사용하여 탄생



>**add** - 커밋할 목록에 추가 / 작업(수정)한 파일 - Working directory
>
>
>
>**commit** - 커밋(creat a snapshot)만들기 - 커밋할 목록 INDEX(staging area)
>
> ->이 과정 까지 와야 git이 적용 될 수있음
>
>
>
>**push** - 현재까지의 역사(commit)가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기 - 쌓인 커밋들 HEAD
>
>
>
>->**GitHub**



**자격증명 관리자** - GitHub 정보 삭제 할 수 있음 - 전 사용자의 기록이 있으면 사용 불가



> #### GitBash로 Github 사용자 입력하기
>
> git config --global user.name "github ID" (enter) - 커밋이 쌓이는 과정 유저네임은 달라도 저장 됨 ""더블포트
>
> git config --global user.email  gmail넣기 (enter) - 이메일이 다르면 사용자를 다르게 인식해서 잔디(기록)가 심어지지 않음
>
> git config --global --list (enter) -자신이 입력한 사용자 정보가 한번 더 뜸
>
> 
>
> git init (enter) - git을 부여 - 내부적으로 한번 더 들어가면 복구가 안됨 **(주의)** -**master가 뜸**
>
> -당시  TIL폴더에 들어가서 실행 시켜주었음
>
> ![](https://user-images.githubusercontent.com/52684457/60943111-dbe45a00-a31f-11e9-9a8b-a944d9c9001d.PNG)
>
> (master)이 붙는다 - git이 부여됨
>
> git status (가장 많이 쓰게 될 코드) -> **error**가 남 - Index를 확인 할 수 있음.
>
> #### WHY?
>
> 아직 Working Directory 상태여서 그렇다 (add를 하지 않음)
>
> -> git add **TIL에있는폴더** 
>
> git status -> **TIL에있는폴더의 파일 목록**들을 불러옴 (초록색)
>
> -
>
> git commit -m "commit 이름" -> 커밋을 생성 git status 를 치면 찾지 못한다. add로인해 만들었던 Index가 commit으로 변환되었기 때문 (nothing to commit)
>
> - Index 확인은 git status
> - commit 확인은 git log
>
> 
>
> **git log**  -> 생성된 커밋들을 확인 가능 함
>
> ![](https://user-images.githubusercontent.com/52684457/60943063-ca9b4d80-a31f-11e9-8636-03fb8b2fdf59.PNG) 
>
> $ gitbash에 넣어서 (enter)
>
> 
>
> git remote -v ->한번 연결하면 계속 연결되기 때문에 한번 더 적용 시킬 필요 X (등록)
>                            하지만 해당 폴더가 어떤 Repositories에 연결되어 있는지 확인 할때 사용
>
> 
>
> git push **-u** origin master -로그인 하는 창이 뜸 (-u 때문에 껐다 켜도 계속 연결이 되어있음)
>
> 
>
> 해당 폴더 안에있는 파일을 Visual Studio Code로 **수정** 했을 때 **git status**를 입력하면
>
> ![](https://user-images.githubusercontent.com/52684457/60943068-cbcc7a80-a31f-11e9-86c3-a32900a1dc66.PNG)  
>
> 수정되었다는 메세지가 뜬다. -> **git add .** 를 사용해서 수정본을 add해주자! -> git status를 치면 수정된 **초록 글씨**가 뜬다. 
>
> 
>
> git commit -m "second commit" ->두번째 커밋을 만듦으로서 이전파일과 다른 수정본을 저장 되었다. **이름이 같아도 OK** 컴퓨터가 읽어내는 commit의 코드는 따로 있음.
>
> 
>
> **git push** -> 연결된 github로 업로드 됨



commit 로컬을 계속 쌓아가다가 push하면 한꺼번에 올라감 (일일히 푸쉬할 필요 없다는 것)



안의 파일들을 수정하면 빨간글씨로 바뀌었다고 오류가 뜸

**git add .** ->이 코드를 사용하면 수정된것에서 add가 부여됨 -> Index상태가 되어서 다시 commit 해줘야 함



-u 계속 등록 되는 코드 복잡한 코드를 생략 할 수 있다.

*git remote -한번만 연결하면 됨*



> ###### master 중복하기
>
> github가 연결된 상태의 폴더에서 gitlab으로 연결을 하기 위해서...
>
> ![capture72](https://user-images.githubusercontent.com/52684457/61687036-4b187000-ad5c-11e9-9850-939be709e42a.PNG)
>
> 
>
> ![](https://user-images.githubusercontent.com/52684457/61687035-4a7fd980-ad5c-11e9-81fb-ec5cab4e89a4.PNG)
>
> git remote -v 을 쳤을때 두가지의 master가 생긴것을 볼 수 있다.
>
> master가 붙는것은 똑같지만 origin으로 넣으면 같은 이름이 붙어서 각 git에서 혼동하기 쉽다. 그래서 gitlab에서는 gitlab으로 이름을 지정해서 넣어주었다. 
>
> git push -u ---- master 할 때 gitlab의 유저네임(또는 이메일)과 비밀번호를 틀리지 않도록 조심한다. 만약 틀리면 숨김파일 .git을 지우는것만으로는 부족하다. 
>
> 시작 검색창에, 자격증명관리자를 찾아 들어가서 gitlab주소를 지워야 한다.
>
> (삼성 gitlab에서 아이디 비밀번호를 틀리면 자격증명이 막히도록 함)
>
> * git config--list 에서 제대로 깃랩(또는 깃헙)의 아이디가 일치하지 않으면 잔디가 깔리지 않는다.
>
> 
>
> ###### 2개 이상의 git master중에서 특정 하나에 push 할 때
>
> git push 깃이름 master
>
> ex) git push gitlab master
>
> 
>
> 또한 제대로 커밋이 올라갔는지 확인하려면 git log를
> master가 어디에 remote 되어있는지 확인하려면 git remote -v로 확인해보면 된다.
>
> 
>
> ###### 새로운 폴더에 git lab연결하기
>
> ![](https://user-images.githubusercontent.com/52684457/61687322-1a850600-ad5d-11e9-99b4-6e3efe329a50.PNG)
>
> 비록 master은 하나지만 다른 폴더와 헷갈리지 않기 위해 gitlab으로 이름을 바꿔서 설정해주었다.



> ###### 다른 사용자의 github 또는 gitlab을 지우고 본인 자격증명하기.
>
> ![](https://user-images.githubusercontent.com/52684457/61936355-84a0e380-afc7-11e9-9d1a-348196efa13a.jpg)
>
> 자격증명을 지워준 뒤, 
>
> ![](https://user-images.githubusercontent.com/52684457/61936354-84a0e380-afc7-11e9-93e3-95661dde1568.JPG)
>
> 자신의 계정으로 연결
>
> 
>
> gitlab같은 경우에는 쓸모없는 Repository (새 프로젝트) 를 만든 후, 한번 git push -u gitlab master 을 해서 계정 로그인을 하면 다시 push pull과 같은 기능을 사용 할 수 있다.







###### 참고 자료

![](https://user-images.githubusercontent.com/52684457/60943121-e141a480-a31f-11e9-9f12-9b2fc66ef164.PNG)

##### push 링크를 이용 했을 때

![](https://user-images.githubusercontent.com/52684457/60943124-e1da3b00-a31f-11e9-84ad-c5a8d3f21c1f.PNG)







> #### 불러오기
>
> *여기서 수정된 파일을 다시 다른곳에서 불러오기 하면 버전이 달라서 겹쳐서 에러가 남. (하나를 버려야 하는 상황이 옴)
>
>  *ex) ssafy <<<TIL>>> home 서로 공유하려면 버전을 맞춰 줘야 함*

> ![](https://user-images.githubusercontent.com/52684457/60943072-ce2ed480-a31f-11e9-8892-db5b4793dd53.PNG)
>
> **Shift + insert** 를 눌러도 git bash에 붙여넣기가 됨.



> #### 협동 하기
>
> *game-폴더 이름
>
> *상황 : 상대방이 github에 저장한 파일 클론을 불러오기 -> 수정해서 상대방에게 보내주기
>
> ![](https://user-images.githubusercontent.com/52684457/60943073-cf600180-a31f-11e9-8141-fa6509a96cb0.png)
>
> ![](https://user-images.githubusercontent.com/52684457/60943079-d0912e80-a31f-11e9-86e7-3e2b255921ca.png)
>
> ![](https://user-images.githubusercontent.com/52684457/60943080-d129c500-a31f-11e9-99d1-2480370ff164.PNG)
>
> git log를 확인하면 Author(저자)를 알 수 있다. / 또한 어떤 커밋이 저장 되었는지 알 수 있다.
>
> denied되는 이유는 단순하다 : 저자가 같지 않기 때문에 (권한이 x) - 권한이 없어도 수정은 가능하긴 함.
>
> 
>
> 이때 Author가 공유 허락을 해줘야 한다. 
>
> ![](https://user-images.githubusercontent.com/52684457/60943081-d1c25b80-a31f-11e9-8f22-0be029877190.png)
>
> 공유가 되고 Author이 수정본을 받게 되면 pull 작업을 해준다. (보내는 것은 push)
>
>  - 본인 컴퓨터에 수정된 것을 덮어 씌우려면 다시 수정된 파일을 클론으로 받는다. -> git clone 링크 /  클론 자체는 이 작업만 실행 해주면 된다. / 클론이 아닌 수정전의 파일 위에 수정된 사항의 파일을 불러 올 때는 git pull만 해주면 됨.
>  - 수정 본을 받은 것 이기 때문에 git add . 로 한번 실행
>    수정된 파일이 안에 새로 생성되기 때문에 폴더위치를 잘 확인 해준다.
>  - 수정된 파일을 다시 수정하고 git add . 으로 수정 완료 
>  - git commit -, "새로운 수정 커밋 이름" -> git status로 제대로 했는지 확인
>  - git log를 확인하면 서로 주고 받은 것을 확인 할 수 있다. -> 너무 길어서 작동에 오류가 날 때가 있다. q키 누르면 됨. (quit의 약자)
>
> ![](https://user-images.githubusercontent.com/52684457/60943082-d25af200-a31f-11e9-9aee-e16f093cba79.PNG)
>
> - 마지막으로 git push를 하면 완료.



###### Git 재 부여 하기 + 복습하기

![](https://user-images.githubusercontent.com/52684457/61012569-fc60f280-a3b9-11e9-9501-bb0893e2abe6.png)



### Git Ignore

git hub에 중요한 정보다 토큰이 들어가면 안됨 (개인 정보나 중요 정보 유출을 막기 위한 코드)

![](https://user-images.githubusercontent.com/52684457/60943111-dbe45a00-a31f-11e9-9a8b-a944d9c9001d.PNG)

**(master)** - github와 **연결**되어 있음을 알림



![](https://user-images.githubusercontent.com/52684457/60943116-df77e100-a31f-11e9-8903-143d026d1a17.png)

- 여기서 .ignore파일 내에 아래의 코드를 찾아 적용 시켜 준다.
- 선 처리를 미리 해주어야 보안에 좋다.



>![](https://user-images.githubusercontent.com/52684457/60943113-dd158700-a31f-11e9-9853-7ca5e38ad82b.PNG)
>
>https://gitignore.io/
>
>![](C:\Users\student\Desktop\study_files\capture\capture11.PNG)
>
>https://github.com/github/gitignore/blob/master/Python.gitignore



공부할 때 도움 되는 site

1) 코딩 도장

![](https://user-images.githubusercontent.com/52684457/60943119-e0a90e00-a31f-11e9-9b2b-95f7243ff12d.PNG)

2) 러닝 파이썬 (파이썬 심화)

![](https://user-images.githubusercontent.com/52684457/60943117-e0107780-a31f-11e9-9f8f-6e86ef8c7ba1.jpg)

3) 스택플로우 https://stackoverflow.com/ 

![](https://user-images.githubusercontent.com/52684457/60943131-e43c9500-a31f-11e9-835f-713cfffc567d.PNG)